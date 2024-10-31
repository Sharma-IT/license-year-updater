import os
import re
import requests
from dotenv import load_dotenv
from datetime import datetime
import git

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

# Headers for GitHub API requests
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_repositories(username):
    """Fetch all repositories for a given GitHub username."""
    url = f'{GITHUB_API_URL}/users/{username}/repos'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_license_content(repo_name):
    """Fetch the content of the LICENSE file from a repository."""
    url = f'{GITHUB_API_URL}/repos/{repo_name}/contents/LICENSE'
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    content = response.json()
    return content['content']

def update_license_year(content):
    """Update the year in the LICENSE content to the current year."""
    current_year = datetime.now().year
    updated_content = re.sub(r'Copyright \(c\) \d{4}', f'Copyright (c) {current_year}', content)
    return updated_content

def update_license_file(repo_name, updated_content):
    """Update the LICENSE file in the repository with the new content."""
    url = f'{GITHUB_API_URL}/repos/{repo_name}/contents/LICENSE'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()
    
    # Decode the content from base64
    current_content = content['content']
    current_content_decoded = current_content.encode('utf-8')
    
    # Encode the updated content to base64
    updated_content_encoded = updated_content.encode('utf-8')
    
    # Prepare the request payload
    payload = {
        'message': f'Update LICENSE to {datetime.now().year}',
        'content': updated_content_encoded.decode('utf-8'),
        'sha': content['sha']
    }
    
    # Send the update request
    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f'Updated LICENSE in {repo_name}')

def clone_repository(repo_url, local_path):
    """Clone a repository to a local path."""
    repo = git.Repo.clone_from(repo_url, local_path)
    return repo

def commit_and_push_changes(repo, repo_name):
    """Commit and push changes to the repository."""
    repo.git.add('LICENSE')
    repo.index.commit(f'Update LICENSE to {datetime.now().year}')
    origin = repo.remote(name='origin')
    origin.push()
    print(f'Committed and pushed changes to {repo_name}')

def main():
    username = 'your_github_username'
    repositories = get_repositories(username)
    
    for repo in repositories:
        repo_name = repo['full_name']
        license_content = get_license_content(repo_name)
        
        if license_content:
            updated_content = update_license_year(license_content)
            update_license_file(repo_name, updated_content)
            
            # Clone the repository locally
            repo_url = f'https://{GITHUB_TOKEN}@github.com/{repo_name}.git'
            local_path = f'./temp/{repo_name.split("/")[-1]}'
            repo = clone_repository(repo_url, local_path)
            
            # Commit and push changes
            commit_and_push_changes(repo, repo_name)
            
            # Clean up local clone
            repo.close()
            os.system(f'rm -rf {local_path}')
        else:
            print(f'No LICENSE file found in {repo_name}')

if __name__ == '__main__':
    main()
