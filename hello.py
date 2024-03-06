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
# git push --all to push all at the same time
print("Ragav")
print("alex")
# git pull will get online commits
# if u delete online, it wont delete offline.
# git pull --rebase origin master gives the feature branch you are working on the updated code from the master


# what is a daabase
# special software to store data
# Can i keep twitter DB in a laptop
# yes but-- It is not a storage issue. If a lot of people requesting,
# it wont be able to handle that much people
# Where does database live?


# Cloud
# Renting PC
# examples of people who give them include microsoft azure, aws, google cloud platforms, IBM cloud, Alibaba cloud
# AWS came first and is double the size of azure
# netflix is one of their biggest customers. since they came first, they were able to trap the client

# Why use AWS
# why not buy instead of rent
# high initial cost
# rent room
# A/C
# Power bill
# maintenance
# Spares
# Generator

# if your renting
# disaster management like cyclones or tsunamis etc
# they will not keep computers in places that are disaster proned


# PC
# you choose specs but rent will increase as specs get better
# everything will be a drop down
# charge for how much you are using

# What OS in cloud
# Linux is 250mb
# Windows is roughly 30gb
# It is called aplhine Linux
# linux is free,
# open source(if theres a security vulnerability, everybody would jump to fix it),
# google will pay you to fix the bugs (only if it becomes big), it is secure,
# it has a small footprint
# its' automation. everything can be done through command prompt.
#  some linux software include ubuntu, manjaro, linux mint, arch (everything is a command line)
# in linux we have flavours/distribution/distros as they each solve one problem. arch has a store for useful tools
# Manjaro looks like windows and its very user friendly
# Kali linux is one of the very popular linux used for hacking

# Scaling
# Whenever customers grow the more you scale up
