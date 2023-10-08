# Creating a Pull Request Workflow

### Step 1: Create a branch from an issue

- Identify the issue you want to work on and note its issue number (e.g., 123).
- Use the `gh issue develop <issue-number>` command to create a branch based on the issue.
- Specify the name of the base branch using the `-b` or `--base` flag.
- Example command: `gh issue develop 123 --checkout --base main`
- To list linked branches for the issue, use the **`-l`** or **`--list`** flag.
- Example command: **`gh issue develop 123 --base main --list`**

### Step 2: Make changes and commit

- Make the necessary changes in the branch.
- Use descriptive commit messages that reference the issue number.
- Example command: `id=123; git commit -m "Resolve #${id}: Update feature XYZ"`
- Push the branch to your remote repository using `git push origin <branch-name>`.
- Example command: `git push origin feature-123`

### Step 3: Create a pull request

- Use the `gh pr create` command to create a pull request.
- Specify the base branch and the title of the PR.
- By default, the current branch will be used as the head branch.
- Example command: `gh pr create --base main --title "Feature XYZ"`

### Step 4: Merge the pull request

- Once the pull request is approved and ready to be merged, use the `gh pr merge <pr-number>` command to merge it.
- Example command: `gh pr merge 456`
- Another example which is quick is to be merged, use the **`gh pr merge <pr-number> --delete-branch --body "<body-text>"`** command to merge it, delete the branch, and add body text.
  **-** Replace **`<pr-number>`** with the actual pull request number.
  **-** Replace **`<body-text>`** with the desired body text for the pull request.

### Step 5: Close the pull request

- Use the `gh pr close <pr-number>` command to close the pull request.
- Example command: `gh pr close 456`

### Step 6: Delete the local branch

- Delete the local branch using `git branch -d <branch-name>`.
- Example command: `git branch -d feature-123`

**Note**: When making commits, you can use keywords to link an issue and pull request or mark an issue or pull request as a duplicate. Here are some suggested GitHub keywords:

- Close
- Closes
- Closed
- Fix
- Fixes
- Fixed
- Resolve
- Resolves
- Resolved

For example, you can use a commit message like: `id=123; git commit -m "Resolve #${id}: Update feature XYZ"`

Let me know if there's anything else I can assist you with!
