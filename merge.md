# Assignment: What is squash and merge , rebase and merge, how are they different from normal merge, and what are Forks and why they are used

## Squash and merge
[Article Used](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges)

- Opting for the "Squash and merge" feature on GitHub.com condenses all the commits within a pull request into a single commit. Rather than displaying numerous individual contributions from a contributor's topic branch, these commits are consolidated into one and then merged into the main branch.

## Rebase and merge
[Article used](https://www.simplilearn.com/git-rebase-vs-merge-article#:~:text=considerably%20more%20profound.-,What's%20the%20Difference%20Between%20Merge%20and%20Rebase%3F,one%20branch%20onto%20another%20branch.)

- 
- Git merge and git rebase differ primarily in their approach to integrating changes between branches. Git merge combines changes from one branch into another, maintaining the existing commit history, while git rebase moves the changes from one branch onto another, essentially rewriting the commit history.

| Merge | Rebase |
|-------|--------|
|Git Merge lets you merge different Git branches.| Git Rebase allows you to integrate the changes from one branch into another.|
|Git Merge logs show you the complete history of commit merging. | Git Rebase logs are linear. As the commits are rebased, the history is altered to reflect this.|
|All the commits on a feature branch are combined into a single commit on the master branch.| |
| | All commits are rebased, and the same number of commits are added to the master branch.|
|Merge is best used when the target branch is supposed to be shared.| |
| | Rebase is best used when the target branch is private.|
|Merge preserves history.| |
| | Rebase rewrites history.|



## Forks

[Article used](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/command-line-GitHub-fork-CLI-terminal-shell#:~:text=A%20fork%20in%20Git%20is,that%20of%20the%20original%20project.)

- In Git, forking involves creating a duplicate of an existing repository, with the new owner effectively severing ties with the previous contributors. Forking commonly occurs when a developer disagrees with or loses faith in the project's direction and decides to separate their work from the original project.

### git rebase -i
- git rebase -i is a command used in Git to perform an interactive rebase. Rebase is a Git operation that allows you to change the base commit of a branch, typically to incorporate changes from another branch or to clean up the commit history. The -i flag stands for "interactive," which means it opens an editor with a list of commits to be rebased, allowing you to reorder, edit, squash, split, or drop commits interactively before applying them to the new base commit. This provides more control over the rebase process and allows you to craft a cleaner and more organized commit history.