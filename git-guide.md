- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
    - Connects your repo folder to the system you are using
    - `git clone`
- add
    - adds file(s) for tracking by git
    - `git add filename`
- rm
    - Remove files matching pathspec from the index, or from the working tree and the index
    - `git rm`
- commit
    - commits changes to the file(s) and forces a changelog where you write messages about what changed.
    - `git commit`
- push
    - Syncs cmmits with Github
    - `git push`
- fetch
    - Fetch branches and/or tags (collectively, "refs") from one or more other repositories, along with the objects necessary to complete their histories
    - `git fetch`
- merge
    - Incorporates changes from the named commits (since the time their histories diverged from the current branch) into the current branch
    - `git merge`
- pull
    - Retrieves content from your remote and merges it into your local repo
    - `git pull`
- branch
    - Pointer to a snapshot of your changes in your repo
    - `git branch`
- checkout
    - Updates files in the working tree to match the version in the index or the specified tree
    - `git checkout`

## git files & folders

- .git folder
    - Hooks: Folder that contains script files. They are executed before or after events like commit, push, etc.
    - Objects: Folder represents an object database of Git
    - Config: Local config file
    - Refs: Folder shares info about tags and branches
    - HEAD: File stores reference to the current branch. It points to the master branch by default
    - Index: Binary file and stores staging info

- .gitignore file
    - File that holds a list of files/directories you want ignored. Git status will no longer show them as files to be added

## GitHub

- Pull requests
    - Forum like interface on Github where you can request changes be merged
- SSH authentication to repositories
    - You can connect and authenticate to remote servers and services (like Github) using the SSH protocol. When you set up SSH, you will need to generate a new SSH key and add it to the ssh-agent. You must add the SSH key to your account on GitHub before you use the key to authenticate.
