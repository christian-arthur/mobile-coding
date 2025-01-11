# This script creates a new file in a GitHub repository using the GitHub API.
import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# GitHub API base URL
api_url = "https://api.github.com"

# Get credentials from environment variables
username = os.getenv("GITHUB_USERNAME")
repo_name = os.getenv("GITHUB_REPO")
token = os.getenv("GITHUB_TOKEN")

# Headers for authentication
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to create a new file
def create_file(path, content, commit_message):
    url = f"{api_url}/repos/{username}/{repo_name}/contents/{path}"
    data = {
        "message": commit_message,
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8")
    }
    response = requests.put(url, headers=headers, json=data)
    return response.status_code == 201

# Example usage
file_name = "example_file_name.py"  # Replace with the name of your new file

# Read the content from your local file
with open(file_name, 'r') as file:
    content = file.read()

# Replaces with your choice of commit message
commit_message = "Create new file from script"

if create_file(file_name, content, commit_message):
    print(f"File '{file_name}' created successfully")
else:
    print(f"Failed to create file '{file_name}'")
