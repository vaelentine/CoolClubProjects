
<p align="center">
<img src=https://user-images.githubusercontent.com/26351860/121793566-37c35780-cbb5-11eb-9bcc-d33b76aea973.jpg width="100" height="100"  />
</p>

# CoolClubProjects
### This repo is intended to be used for coding projects primarily written in (but not limited to) python, javascript and various frameworks including django, vue and react. 
We use something like github flow for version control. Read more about that here: https://githubflow.github.io/


### Prerequisites:
1. A github account.
1. Install and set up git on the command line with your account. 
1. choose a folder where you want this repo to live and clone it (click the green "code" button and copy the repo link onto your clipboard. on the command line type `git clone <repository link`)

### Make changes in this repo:
1. make a new branch (recommended) starting with "feature/", thus the full name would be  "feature/<your-branch-name>" (without the arrow brackets, kebab case) (on the command line this would be `git checkout -b "<feature/your-branch-name>"` (note that this will automatically switch you into your branch)
 
2. Create a folder under your name if you haven't already, then edit code within your folder. Notes on this: You may also update update the .gitignore but make sure to submit your changes in a pull request. If you want to add a "requirements.txt" file do so within your personal folder, so that different devs can set up different requirements for their apps. If you add a virtual environment folder (recommended to keep your packages contained and not pollute your global scope), this should be gitignored, so feel free to add as many as you want either at the repo directory root or in your folder.
 
3. Commit and push code on your branch (using `git add <filenames>` then `git commit -m "<your commit message>"` then `git push`)

4. Make a pull request (navigate to your branch on github, use the dropdown on the left side of the repo page on github, then click the "create pull request" button)

5. Get someone to review/approve your PR + merge it into the master branch or appropriate feature branch.
  

### Working on branches:

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
`git commit -m "<your commit message>"`

FINALLY
'git push origin <your-branch-name>`

This will push code onto your branch.
View it on github.
Now you're ready to make a pull request!

Go onto github and look for the green button for pull request.
Click it, which will make a new pull request.

Get someone in this repo to review and approve your code changes, and then test in their environment. 

Once it is approved, a repository maintainer can merge it onto master (if the option isn't available to you, you either haven't been invited yet or accepted your permissions.)
