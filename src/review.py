import argparse
from github_api import fetch_pr_diffs
from gpt_agent import review_diff
from rich import print

def main():
    parser = argparse.ArgumentParser(
        description="Review a GitHub PR using GPT and print suggestions."
    )
    parser.add_argument(
        "url",
        help="GitHub Pull Request URL (ex. https://github.com/user/repo/pull/123)"
    )
    parser.add_argument(
        "--model",
        default="gpt-4",
        help="OpenAI model to use (default: gpt-4)"
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=8000,
        help="Max patch  byte kenght to process (default: 8000)"
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print summary stats after review"
    )

    args = parser.parse_args()

    pr_url = args.url
    model = args.model
    max_bytes = args.max_bytes
    show_summary = args.summary

    print(f"[cyan]Fetching diffs from [/cyan] {pr_url}")
    diffs = fetch_pr_diffs(pr_url)

    reviewed = 0
    skipped = 0

    for filename, patch in diffs.items():
        print(f"\n[bold]Reviewing: {filename}[/bold]")

        if not patch.strip():
            print("[gray]No changes detected.[/gray]")
            skipped += 1
            continue
        
        if len(patch.encode("utf-8")) > max_bytes:
            print(f"[yellow]Skipped patch too large ({len(patch)} bytes)[/yellow]")
            skipped += 1
            continue

        comments = review_diff(filename, patch, model=model)
        print("[green]AI Comments:[/green]")
        print(comments)
        reviewed += 1

    if show_summary:
        print(f"\n[bold cyan]Summary:[/bold cyan] Reviewed {reviewed} files, Skipped {skipped}")

if __name__ == "__main__":
    main()