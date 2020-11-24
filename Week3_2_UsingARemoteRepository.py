#%%
"""
Introduction to Git and GitHub, by Google

WEEK 3 - Working with Remotes

3.2 Using a Remote Repository
    3.2.1 What is a remote?
    3.2.2 Working with Remotes
    3.2.3 Fetching New Changes
    3.2.4 Updating the Local Repository
    3.2.5 Git Remotes Cheat-Sheet
    3.2.6 Practice Quiz

MY SYNOPSIS

a user creates a remote repository (on GitHub or on a server of a private network-Linux OS/Window OS)
other users clone the remote repository and they have local repositories
then, all users collaborate

When working on my local repository, the sequence of steps is:
    modify file
    stage file
    commit file
    pull changes made on the remote (Git lets me know I must update my local if changes have been made to the remote)
    merge
    push changes I made on my local repository to the remote
    FIRST PULL THEN PUSH!
    (merges are done automatically gy Git unless there is a conflict)
    creator of remote repository can have me read-only the remote or give me access

COMMAND "git clone URL":
    I clone/copy the remote repository(URL) to my machine and what I get is a local repository

COMMAND "git remote" 	
    Lists remote repositories
    output to this command is "origin"

COMMAND "git remote -v":   
    Lists remote repositories verbosely (with more details, more words)
    displays configuration of the remote repository
    I see two URL's, one to fetch data from the remote, one to push data to the remote 

COMMAND "git remote show":
    displays remote repositories
    Output to this command is "origin"
    
COMMAND "git remote show origin": 
    "git remote show <repository>" : "git remote show origin"
    displays information about the remote repository e.g. the 2 URL's for fetch and push
    lets us know if those changes are not reflected to our local repository
    
Remote repositories have the name "origin" assigned to them
I can have more than one repository in one directory


COMMAND "git fetch": 
    -fetches changes from the remote repository BUT DOES NOT merge them to our local repository
    -displays commits made on the remote branches but those commits are not reflected yet on our local branches
    -with git fetch we only display the changes done to the remote, 
    if we want those changes applied to our local we have to do it ourselves with git merge
    -Instead of using git fetch then git merge, we can use one command, the git pull

I do not understand the difference of "git fetch" and "git remote update" ADD EXPLANATION ++++++
(on Git Bash, git fetch output is empty and git remote update output is Fetching origin)

COMMAND "git pull": 
    fetches changes from the remote repository AND merges them to our local repository
    (git pull = git fetch + git merge)
                                                                   
COMMAND "git log origin/master": 
    displays history of commits on the remote repository
    displays commits done on the remote master branch (master branch is now named main branch)
                                 
COMMAND "git status": 
    displays status of our changes both in remote and local repository
    lets us know if local branches are behind the remote branches
                      
COMMAND "git merge origin/master":  
    merges the origin/master branch (the remote), into our local master branch

COMMAND "git log": 
    displays history of commits in our local repository
    
COMMAND "git branch -r":
    lists remote branches 
    can be combined with other branch arguments to manage remote branches
    remote branches are read-only
    If we want to make a change to a remote branch, then
    -Pull the remote branch
    -merge it with the local branch
    -push it back to its origin  
    
What TYPE OF MERGE creates a new merge commit?
An explicit merge creates a new merge commit. 
This alters the commit history and explicitly shows where a merge was executed.
"""
#%%
"""
3.2.1 What is a remote?

first I create a Remote Repository on GitHub
then I clone it as a Local Repository on my machine

then I can do whatever changes I like on my Local Repository
if more people clone the Remote Repository on their machine:
    we can use git push to update changes made to the local repository TO the remote
    we can use git pull to update changes made to the remote repository TO our local

Ways to host remote repositories
1) Use GitHub, GitLab (online hosting of the remote repositories)
2) We can set up a Git server in our own network  
    a Git server can run on any OS, Linux, Windows, Mac
    a Git server on our own network offers privacy, control and customization

Using Git to manage a project helps us collaborate successfully. 
Everyone will develop their piece of the project independently, in their own local repositories
Occasionally they'll push finished code into a central remote repository 
where others can pull it and incorporate it into their new developments.
If someone has updated a repository since the last time you synchronize your local copy, 
Git will tell you that it's time to do an update

we push code to the remote repository
we pull code from the remote repository
Git merges branches to the main branch automatically 
if there is a confilct, Git asks us to give instructions for the merge

steps:
modify file
stage file
commit file
then pull code from remote repository, (fetch any changes made), merge if necessary
then push code to the remote repository
SO, first pull and then push

In-Video question
What will happen if the master repository receives a major update since the last local copy was synced?
Git will let you know it is time for an update

How to connect to a remote repository 
HTTP protocol   allows read access to the remote repository
                lets people clone it BUT does not allow them to push changes to it
                
HTTPS protocol allows push by other people but after authenticating them, after creator of remote repository gives access
SSH protocol    same as HTTPS
"""
#%%
"""
 3.2.2 Working with Remotes
 
git clone URL       # I have cloned the remote repository health-cheks 
                      to my local machine.
                      Now I have a local repository in a directory named "health_checks"
cd health-checks   # navigate to the local repository
git remote -v      # displays configuration of the remote repository
                    origin  https://github.com/FoteiniRodi/health-checks.git (fetch)
                    origin  https://github.com/FoteiniRodi/health-checks.git (push)
                    we see the URL's associated with the remote repository
                    there are 2 URL's: one to fetch data from the remote
                                       one to push data to the remote
in some cases, you can have the fetch URL use HTTP for read only access, and the push URL use HTTPS or SSH for access control. 
This is fine as long as the contents of the repo that you read when fetching 
are the same that you write to in pushing. 

Remote repositories have a name assigned to them, by default, the assigned name is origin. 
This lets us track more than one remote in the same Git directory.
(I can have more than 1 repositories in the same Git directory)

git remote show origin # displays information about the remote repository
                        * remote origin
                          Fetch URL: https://github.com/FoteiniRodi/health-checks.git
                          Push  URL: https://github.com/FoteiniRodi/health-checks.git
                          HEAD branch: main
                          Remote branch:
                            main tracked
                          Local branch configured for 'git pull':
                            main merges with remote main
                          Local ref configured for 'git push':
                            main pushes to main (up to date)
For now we only have a main branch that exists locally and remotely
Once you start having more branches, especially different branches in the local and remote repo, this information starts becoming more complex.

git branch -r          # displays remote branches 
                       Git uses remote branches to keep copies of the data that's stored in the remote repository.
                        origin/HEAD -> origin/main
                        origin/main
                        remote branches are read-only
                        we can look at their commit history BUT we can't make changes to them directly
                        To modify the content of remote branches we have to
                        use the steps we mentioned before: 
                            1 pull new changes to our local branch
                            2 merge them with our changes
                            3 push our changes to te remote repository

In-Video question
If we want to make a change to a remote branch, what must we do?
Pull the remote branch
merge it with the local branch
push it back to its origin

git status           # displays status of our changes both in remote and local repository
                       we can use  git status to display the status of our changes in remote branches as well.
                    Now that we are working with a Remote repository AND our Local repository,
                    git status gives us additional information:
                    It tells us that 
                    our branch is up to date with the origin/master branch, 
                    which means that the master branch in the remote repository called origin, has the same commits as our local master branch.
                    On branch main
                    Your branch is up to date with 'origin/main'.
                    
                    nothing to commit, working tree clean
"""
#%%
"""
3.2.3 Fetching New Changes

git pull AND git fetch difference:
git pull fetches and merges / git fetch fetches but does not merge

We can use git fetch to review the changes that happen in the remote repository. 
If we're happy with them, we can use git merge to integrate them into the local branch. 

Fetching commits from a remote repository and then merging them into your local repository 
is such a common operation in Git that there's a handy command to let us do it all in one action, the git pull command

In_Video question
What’s the main difference between git fetch and git pull?
git fetch, fetches remote updates but DOES NOT MERGE.
git pull, fetches remote updates AND MERGES


EXAMPLE
I have the directory health-checks
I cloned before the remote repository health-checks
so I have a local repository

colleague Blue kale added 2 files to the remote repository
I could see the changes on GitHub but I will do it through my command line

git remote show origin # displays information about the remote repository
                        I see: "local branches out of date" 
                        This happens when there are commits done to the remote repository
                        not yet reflected to the local repository
                        
Git does not synchronize remote branches and local branches automatically                        
It waits for us to do it when we are ready
To synchronize we use the "git fetch" command
This command copies the commits done in the remote repository to the remote branches, 
so we can see what other people have committed.

git fetch             #  fetches changes from the remote repository
                         those changes are NOT automatically mirrored to our local branches
                        Fetched content is downloaded to the remote branches on our repository. 
                        So it's not automatically mirrored to our local branches. 

git checkout <branch> # switch to a certain branch

git log origin/master # git log displays history of commits
                        git log origin/master displays commits done on the remote master branch
                        origin is used to look at the remote branch
                        master is the branch
                        -latest commit is on remote master branch (indicated by HEAD) (origin/master)
                        -previous commit is on local master branch (indicated by HEAD)

git status            # displays status of our changes both in remote and local repository
                      Git tells us 
                      Your branch is behind rigin/master by 1 commit
                      Now we can merge the origin/master branch (the remote),
                      into our local master branch

git merge origin/master # merges the origin/master branch (the remote),
                      into our local master branch
                      updating
                      Fast-Forward
                      all_checks.py
                      disk_usage.py+++

git log               # displays history of commits in our local repository
                      latest commit contains local and remote branch both indicated by HEAD                   
                      now our local master branch is up to date with the remote master branch (origin/branch)
"""
#%%
"""
3.2.4 Updating the Local Repository

git pull
Running git pull will fetch the remote copy of the current branch and automatically 
try to merge it into the current local branch.
git pull precedes git push!


Let's see if any changes are made to the remote repository with git pull

git pull       # fetches changes from the remote to the local
               and tries to merge them into the local repository
               Output contains output of git fetch and git merge commands

git log -p -1  # display history of commits
               p is patch (displays more info)
               -1 is latest one commit
               text editor opens, we see the info
               exit the editor with q
               there was a new remote branch called experimental
               that means our colleague Blue Kale started working on a new feature on that branch
               
git remote show origin # displays information about the remote repository
                       we see the new branch called "experimental"
                       we do not have a local branch that reflects the "experimental"
                       
git checkout experimental # with git checkout we switch into a branch
                          Git copies the contents of the remote "experimental" branch
                          to a local branch
                          Branch 'experimental" set up to track remote branch "experimental" from "origin"
                          Switched to a new branch 'experimental'.
                          So we copied it to our local repository and switched into it
                          Now we're all set to work on the experimental feature together with our colleague. 

In-Video question
Assuming no merge conflicts, which type of merge does git pull perform automatically?
Fast-Forward merge

with git pull,
we got the contents of the "experimental" branch
we got the contents of the master branch
merged changes onto the master branch

with git remote update
get the contents of the "experimental" branch
get the contents of the master branch
NO AUTOMATIC merging though

git fetch / git remote update / git pull


"""
#%%
"""
3.2.5 Git Remotes Cheat-Sheet

Git Remotes Cheat-Sheet
Command	Explanation & Links
git remote 	                Lists remote repos
git remote -v	            List remote repos verbosely
git remote show <name>	    Describes a single remote repo
git remote update	        Fetches the most up-to-date objects
git fetch	                Downloads specific objects
git branch -r	            Lists remote branches; 
                            can be combined with other branch arguments to manage remote branches

You can also see more in the video Cryptography in Action from the course IT Security: Defense against the digital dark arts.
"""
#%%
"""
3.2.6 Practice Quiz

Question 1
In order to get the contents of a remote branch without automatically merging, 
which of these commands should we use?

-git pull
-git remote update CORRECT
You got it! 
git remote update will fetch the contents of all remote branches and allow us to merge the contents ourselves.
-git checkout 
git checkout switches branches but will not download remote updates.
-git log -p -1

Question 2
If we need to find more information about a remote branch, which command will help us?

-git fetch 
git fetch will download remote updates, such as objects and refs, from the remote branch.
-git checkout
-git remote update
-git remote show origin CORRECT
Right on! 
If you want to see more information about a particular remote branch, 
you can use the git remote show command. Don't forget the commit ID!

Question 3
What command will download remote branches from remote repositories 
without merging the content with your current workspace automatically?

-git checkout
-git pull
-git fetch CORRECT
Nice work! 
git fetch will download remote updates, such as objects and refs, from the remote branch, without merging the content with your current workspace automatically
-git remote update 
Not quite. 
git remote update will fetch the contents of all remote branches, and allow us to merge the contents ourselves.

Question 4
What type of merge creates a new merge commit?

-Fast-forward merge 
Not quite. Fast-forward merges are a type of implicit merge, which do not create new commits
-Implicit merge
-Explicit merge CORRECT?
Woohoo! An explicit merge creates a new merge commit. 
This alters the commit history and explicitly shows where a merge was executed.
-Squash on merge

Question 5
What method of getting remote contents 
will automatically merge the remote branch with the current local branch?

-git fetch
-git checkout
-git remote update
-git pull CORRECT
Great job! git pull automatically merges the remote branch with the current branch.
"""
