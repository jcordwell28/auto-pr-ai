from github_api import fetch_pr_diffs

pr_url = "https://github.com/jcordwell28/auto-pr-ai/pull/1"
diffs = fetch_pr_diffs(pr_url)

for filename, patch in diffs.items():
    print(f"\n {filename}:\n{patch[:300]}..\n")