# Open Web Page to Most Recent Commit Using `gh` CLI

1. Install the `gh` command-line interface if you haven't already. You can find installation instructions in the official GitHub CLI repository: [github.com/cli/cli](https://github.com/cli/cli).

2. Authenticate `gh` CLI with your GitHub account.

3. Open your terminal or command prompt.

4. Run the following command to view the most recent commit in the current state: `latest_commit=$(git rev-parse HEAD) && open $(gh api repos/:owner/:repo/commits/${latest_commit} --jq ".html_url" -H "Accept: application/vnd.github.v3+json")`
