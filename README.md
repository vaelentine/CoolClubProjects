﻿# CoolClubProjects
 
<img src=https://res.cloudinary.com/teepublic/image/private/s--Hn9fiFxx--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_630,q_90,w_630/v1515213242/production/designs/2257873_1.jpg width="100" height="100" />

### This repo is intended to be used for python projects

### Prerequisites:
1. A github account.
1. Install and set up git on the command line with your account. 
1. choose a folder where you want this repo to live and clone it (click the green "code" button and copy the repo link onto your clipboard. on the command line type `git clone <repository link`)

### Make changes in this repo:
1. make a new branch starting with "feature-", thus the full name would be  "Feature-<your branch name>" (without the arrow brackets) (on the command line this would be `git branch -b "<feature-your branch name>"` (note that this will automatically switch you into your branch)
2. Create a folder under your name if you haven't, then edit code within your folder.
3. Commit and push code on your branch (using `git add <filenames>` then `git commit -m "<your commit message>" then git push)
4. Make a pull request (navigate to your branch on github, use the dropdown on the left side of the repo page on github, then click the "create pull request" button)
5. Get someone to review/approve your PR + merge it into the master branch or appropriate feature branch.
  

### How to make a new branch:
(make sure you have git installed and the repository)
`git checkout -b <your-branch-name>`

Make changes within the repository folder. 
Commit your code as soon as possible (tip, make sure your code is working before committing).

note:
`git status` to see what changes are present

How to commit and push your code:
`git add <filename>`
OR 
`git add .` to add all files
THEN
`git commit -m "<your commit message>"

FINALLY
'git push origin <your-branch-name>`

This will push code onto your branch.
View it on github.
Now you're ready to make a pull request!

Go onto github and look for the green button for pull request.
Click it, which will make a new pull request.

Get someone in this repo to review and approve your code changes. 

Once it is approved, someone with permissions (vaelentine) can merge it onto master.
