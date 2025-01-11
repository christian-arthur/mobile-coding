# This script updates the content of an existing file in a GitHub repository using the GitHub API.

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

# Function to get file SHA
def get_file_sha(path):
    url = f"{api_url}/repos/{username}/{repo_name}/contents/{path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["sha"]
    return None

# Function to update file content on GitHub
def update_file_content(path, new_content, sha, commit_message):
    url = f"{api_url}/repos/{username}/{repo_name}/contents/{path}"
    data = {
        "message": commit_message,
        "content": base64.b64encode(new_content.encode("utf-8")).decode("utf-8"),
        "sha": sha
    }
    response = requests.put(url, headers=headers, json=data)
    return response.status_code == 200

# Example usage
file_name = "example_file_name.py"  # Replace with the name of your file
commit_message = "Update file from script"

# Read the new content from your local file
with open(file_name, 'r') as file:
    new_content = file.read()

sha = get_file_sha(file_name)

if sha is not None:
    if update_file_content(file_name, new_content, sha, commit_message):
        print(f"File '{file_name}' updated successfully on GitHub")
    else:
        print(f"Failed to update file '{file_name}' on GitHub")
else:
    print(f"Failed to get SHA for file '{file_name}' from GitHub")

