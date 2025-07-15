from github import Github
import os

import re # for URL parsing

github_token = os.getenv("GITHUB_TOKEN")
g = Github(github_token)

def parse_pr_url(pr_url):
        pattern = r"https:\/\/github\.com\/([a-zA-Z0-9_-]+)\/([a-zA-Z0-9._-]+)\/pull\/(\d+)"
        match = re.search(pattern, pr_url)
        if not match:
            raise ValueError("Invalid GitHub PR URL")

        owner = match.group(1)
        repo = match.group(2)
        pull_num = int(match.group(3))

        print(f"Owner: {owner}")
        print(f"Repo: {repo}")
        print(f"Pull Number: {pull_num}")

        return owner, repo, pull_num

def fetch_pr_diffs(pr_url):
    owner, repo_name, pull_number = parse_pr_url(pr_url)

    repo = g.get_repo(f"{owner}/{repo_name}")
    pr = repo.get_pull(pull_number)

    diffs = {}

    for file in pr.get_files():
         if not file.patch:
              continue
         diffs[file.filename] = file.patch
    return diffs