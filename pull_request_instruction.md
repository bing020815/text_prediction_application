# Pull Request Instruction
This is the simplest version of pull request tutorial.   
Many steps have been skipped in order to save time on solving conflicts.  

## Table of Contents
* <a href="#definition">Definition</a>
* <a href="#workflow">Standard Fork & Pull Request Workflow</a>
	- <a href="#step0">Step 0. Locate the directory for downloading the repo in your Local Machine</a>
	- <a href="#step1">Step 1. Creating a Fork on Github</a>
	- <a href="#step2">Step 2. Keep Your Fork Up To Date With Upstream Repo</a>
	- <a href="#step3">Step 3. Do Your Work</a>
	- <a href="#step3">Step 4. Pull Request to Update the Original Repository</a>
* <a href="#updatefork">Update Your Fork</a>



## <span id="definition">Definition</span>
Term | Explanation
:--|:--
repo |Repository
Fork |A copy version of repo from the original repository 
upstream repo| The original repository  


__There are two ways to pull request through github__  
  1. Pull Request from a forked repository  
  2. Pull Request from a branch within a repository  

> Because __method 1__ is a better approach in our case. Thus, we only focus on __method 1__ approach.
    
<p><br></p>

## <span id="workflow">Standard Fork & Pull Request Workflow</span>
### <span id="step0">Step 0. Locate the directory for downloading the repo in your Local Machine</span>

Create a folder under the root directory to store repo in local machine. Here, the folder name is called 'Github': 
```
 $Terminal: mkdir Github     
```

Re-direct to the folder just created:
```
 $Terminal: cd Github
```
  
You can also check a list of folder or files by having the command:
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



### <span id="step1">Step 1. Creating a Fork on Github</span>
Click fork on the github web page to make sure there is a Fork under your github repository pools.  

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




### <span id="step2">Step 2. Keep Your Fork Up To Date With Upstream Repo</span>
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
*  Make a copy of your repo in local machine to other place if you have done some modifications already. 
*  Any file modification or adding new file actions can be done after syncing the local repo from original repository.




### <span id="step3">Step 3. Do Your Work</span>
In this step, you are free to update your file or add files into your local repo.

Once you have finished your modification. You are ready to stage changes and push to your Fork.
The `git status` shows the info about any changes in your local repo:
```
 $Termimal: git status
```

Stage all the modified files:
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

Here, you should able to see the changes on your github webpage.  


### <span id="step4">Step 4. Pull Request to Update the Original Repository</span>
Go to your Fork on the Github webpage. Click on the __Pull requests__ tab.   
There is a __New pull request__ button. Click on the __New pull request__ button and follow the steps.  
Then, you have finished the whole __Pull Request__ process.  

<p><br></p>


## <span id="updatefork">Update Your Fork</span>

1. Add the remote (the original repo that was forked) and call it `upstream`.
```
 $Termimal: git remote add upstream https://github.com/bing020815/text_prediction_application.git
```

2. Fetch all branches of remote upstream.
```
 $Termimal: git fetch
```

3. Rewrite your master with master from upstream using `git rebase`.
```
 $Termimal: git rebase upstream/master 
```
3.1 <strong>Note: </strong> If you have edited or updated any file in your local machine previously, please either copy those files to other places for backup or just use the `git restore` command to restore your repo.
```
 $Termimal: git restore . 
```

4. Make updates on your repo. Push your updates to master.
```
 $Termimal: git push origin master 
```




[<p align='center'>Top</p>](#pull-request-instruction)
