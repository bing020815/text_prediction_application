# Pull Request Instruction
This is the simplest version of pull request tutorial.   
Many steps have been skipped in order to save time on solving conflicts.  


## Definition
* repo: Repository
* Fork: a copy version of repo from the original repository 

__There are two ways to pull request through github__  
  1. Pull Request from a forked repository  
  2. Pull Request from a branch within a repository  

__Method 1__ is a better approach in our case. Thus, we focus on __method 1__ 


## Standard fork & Pull Request Workflow
### Step 0. Locate the directory for downloading the repo in your Local Machine

Create a folder to store repo in local machine. Here, the folder name is called 'Github': 
```
 $Terminal: mkdir Github     
```

Re-direct to the folder just created:
```
 $Terminal: cd Github
```
  
You can also check a list of folder by having the command:
```
 $Terminal: ls 
```
or 
```
 $Terminal: ls -la
```
  
To go back to the root directory:
```
 $Terminal: cd
```


### Step 1. Creating a Fork on Github
Click fork on the github web page to make sure there is a fork under your github repository pools.  

Normally, you all have done this step. Then, clone the Fork to your local machine:
```
 $Termimal: git clone https://github.com/__YourUserName__/text_prediction_application.git
```

Here, you have cloned the repo to your local machine.
To check everything in your local machine about the repo, re-direct to the repo folder
```
 $Termimal: cd text_prediction_application
```
Now, you are just half-ready to update your Fork



### Step 2. Keep Your Fork Up To Date With Upstream Repo
In order to do any modification, you will want to make sure you keep your Fork up to date to avoiding any conflict by tracking the original 'upstream' repo.

__Add 'upstream' repo to list of remotes__:
```
 $Termimal: git remote add upstream https://github.com/bing020815/text_prediction_application.git
```

__Verify the new remote named 'upstream'__:
```
 $Termimal: git remote -v
```


__Pull any new commit updates into your repo__
```
 $Termimal: git pull upstream master
```

__ATTENTION!!__:

*  To avoid any conflict, make sure there are no changes in your local repo. 
*  Make a copy of your repo in local machine if you have done some modification already.
*  Any file modification or adding new file actions should be done after syncing the local repo from original repository.



### Step 3. Do Your Work
In this step, you are free to update you file and add files into your local repo.

Once you have finished your modification. You are ready to staging changes and push to your Fork.
The `git status` shows the info about any changes in your local repo:
```
 $Termimal: git status
```

Staging all the modified files:
```
 $Termimal: git add .
```

Add commit comment:
```
 $Termimal: git commit -m "__put your comment here__"
```

Push to the Fork:
```
 $Termimal: git push origin master
```


### Step 4. Pull Request to Update the Original Repository
Go to your Fork on the Github webpage. Click on the __Pull requests__ tab.   
There is a __New pull request__ button. Click on the __New pull request__ button and follow the steps.  
Then, you have finished the whole __Pull Request__ process.  