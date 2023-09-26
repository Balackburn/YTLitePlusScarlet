import requests
import json
import re

# GitHub repository information
repo_owner = "Balackburn"
repo_name = "YTLitePlus"

# Fetch latest release information from GitHub API
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
response = requests.get(api_url)
release_data = response.json()

# Extract relevant information from the release data
body = release_data["body"]
changelog = re.search(r"YTLitePlus Release Information(.*)", body, re.DOTALL).group(1).strip()
changelog = re.sub(r'`', '"', changelog)
download_url = release_data["assets"][0]["browser_download_url"]
tag_name = release_data["tag_name"]
version = re.search(r"v(\d+\.\d+\.\d+)", tag_name).group(1)

# Update the scarlet.json file
with open("scarlet.json", "r+") as file:
    data = json.load(file)
    data["Tweaked"][0]["changelog"] = changelog
    data["Tweaked"][0]["down"] = download_url
    data["Tweaked"][0]["version"] = version
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()

