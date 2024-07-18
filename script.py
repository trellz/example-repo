import os
import requests
import base64
import json

# Retrieve GitHub credentials from environment variables
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

# Check if the environment variables are set
if not GITHUB_USERNAME or not GITHUB_TOKEN:
    raise EnvironmentError("Please set the GITHUB_USERNAME and GITHUB_TOKEN environment variables.")

# GitHub API URL
GITHUB_API_URL = 'https://api.github.com'

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Script continues here...