# CLI tool that takes a PR URL
# fetches code diffs
# prints GPT-generated review comments to the terminal

import sys
from github_api import fetch_pr_diffs
from gpt_agent import review_diff
from rich import print # console output will be cleaner

# check for PR URL argument
if len(sys.argv) != 2:
    print("[red]Usage:[/red] python src/review.py <GitHub PR URL>")
    sys.exit(1)

pr_url = sys.argv[1]

print(f"[cyan]Fetching diffs from: [/cyan] {pr_url}")
diffs = fetch_pr_diffs(pr_url)

for filename, diff_text in diffs.items():
    print(f"\n[bold] Reviewing: {filename}[/bold]")
    if not diff_text.strip():
        print("[gray]No changes detected.[/gray]")
        continue

    comments = review_diff(diff_text)
    print("[green]AI Comments:[/green]")
    print (comments)