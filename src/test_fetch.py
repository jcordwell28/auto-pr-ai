from github_api import fetch_pr_diffs

pr_url = pr_url = "https://github.com/python/cpython/pull/116412"
diffs = fetch_pr_diffs(pr_url)

for filename, patch in diffs.items():
    print(f"\n {filename}:\n{patch[:300]}..\n")