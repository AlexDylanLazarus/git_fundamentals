print("Hello")


def double(n):
    return n * 2


# git init creates a folder that'll track everything like changes etc.
# type explorer .
# then click view show hidden items to see folder

# to stage from command line
# git add . for all files
# git add file name just for that file

# git commit -m "This is my first project with git"
# to see commits you've done so far
# git log will show this is my first project with git
# to see previous commit say git checkout 51567fb3
# You get the number from the log
# to go back you say git checkout -
#  if you say it again itll take you back to the 5156 thing
# Master always points to latest commit you have
#  space to scroll down press Q to exit the git log


# git init
# git add .
# git commit -m "This is my first project with git"
# git add .
# git commit -m "Created double function"
# git log
# git add .
# git commit -m "Cool file with awesome msg"
# git log
# git checkout c7f9f09860
# git checkout -
# git log
# git checkout 4b8be
# git checkout c7f9
# git checkout -
# git checkout master
#  git revert id --no-edit this will reverse the commit. replace the id with the number of the logid
# git reset --soft HEAD~1 this will keep it in the stage area. You can use this to review it/edit it
# git reset --hard HEAD~1 this will completely remove it and not keep it in the stage area
# git log --help
# to search for something in commit (the file not the message) you can say git log -Sdouble this is known as the pick-asxe command
# git log -Sdouble -p will show changes/when it was added
# git log -2 will tell you the last 2 commits
# git log --graph (graph commit(s))
# /map
# press n to go to the next match
# git checkout -b dev creates a new branch named dev
# when you want to merge, go to the master branch (git checkout master)
# git merge dev
# Merge conflict (happens when people change the same line)
# 1. resolve it
# 2. stage it
# 3. commit
# git push --set-upstream origin dev
