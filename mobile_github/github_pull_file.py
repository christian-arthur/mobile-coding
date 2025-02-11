# This script retrieves the content of an existing file in a GitHub repository using the GitHub API.
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

# Function to get file content from GitHub
def get_file_content(path):
    url = f"{api_url}/repos/{username}/{repo_name}/contents/{path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8")
        return content
    return None

# Example usage
file_name = "example_file_name.py"  # Replace with the name of your file
content = get_file_content(file_name)

if content is not None:
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' created/overwritten successfully with content from GitHub")
else:
    print(f"Failed to get content for file '{file_name}' from GitHub")
