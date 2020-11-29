#%%
"""
Introduction to Git and GitHub, by Google

WEEK 3 - Working with Remotes

3.3 Solving Conflicts
    3.3.1 The Pull-Merge-Push Workflow
    3.3.2 Pushing Remote Branches
    3.3.3 Rebasing Your Changes
    3.3.4 Another Rebasing Example
    3.3.5 Best Practices for Collaboration
    3.3.6 Conflict Resolution Cheat Sheet
    3.3.7 Practice Quiz

MY SYNOPSIS
when working with a remote repository on GitHub and its clone/copy local repository on my machine:
    first pull then push
    pull changes from the remote (fetch changes and merge them to my local repository)
    Git will try to do all possible automatic merges and only leave manual conflicts for us to resolve when the automatic merge fails.

MERGE CONFLICT MARKERS
when a merge happens Git alters our file and adds the following markers:
1   <<<<<<< HEAD
2   =======
3   >>>>>>>

explanation:
we have the branch "main" and the branch "new branch"
we try to merge the new branch to the main (and produce one branch, the updated main)
we cannot merge because there was a change.
In the file Git made some changes eventhough merge was not successful:
1   All the content between the center and the <<<<<<< HEAD line 
    is content that exists in the current branch master which the HEAD ref is pointing to
2   The ======= line is the "center" of the conflict
3   all content between the center and >>>>>>> new branch
    is content that is present in the new branch we want to merge into the main

EXPLANATION, see 2.3.5 script free_memory.py: 

INITIAL SCRIPT ON       SCRIPT ON BRANCH "MAIN"                                 SCRIPT ON BRANCH "NEW BRANCH"
LOCAL REPOSITORY
#!/usr/bin/env python3  #!/usr/bin/env python3                                  #!/usr/bin/env python3
def main():             def main():                                             def main():
    pass                    Checks if there is enough memory in the computer        print("Everything is OK.")
main()                  main()                                                  main()

-So, we had an identical script in both branches
-we modified the script while on the main branch
-we also modified the script while on the new branch
-then we tried to merge the new branch to the main,
but we failed because the change was different but exactly on the same part of the script
-we see the message:
    CONFLICT (content): Merge conflict in free_memory.py
    Automatic merge failed; fix conflicts and then commit the result.
- Git cannot merge automatically because it cannot choose which change to apply on the same part of the script
-So, we must intervene manually
-open editor to see the script, Git has changed it and added conflict markers!
 Git tells us what we did and where
 the altered script looks like this:
                    #!/usr/bin/env python3
                    def main():
                    <<<<<<< HEAD
                        "Checks if there is enough memory in the computer"
                    =======
                        print("Everything is OK.")
                    >>>>>>> even-better-feature
                    main()
                    
                    #!/usr/bin/env python3
                    def main():                
                        "Checks if there is enough memory in the computer"                 
                        print("Everything is OK.")
                    main()




COMMAND "git log -p <branch>": shows commit history for a certain branch
                               e.g git log -p origin/master shows commit history 
                               for the branch "master" of the remote repository
                               
PUSH A BRANCH FROM LOCAL TO MAIN BRANCH ON REMOTE, FOR THE FIRST TIME!
the first time we push a branch to the remote repository, we add a few more parameters to the command "git push"
this is not merging, we add a branch of our local to the main branch of the remote for revision by others
COMMAND "git push -u <remote branch> <new local branch>": -u is up-stream
                                                          remote branch to which we are pushing
                                                          local branch being pushed
COMMAND "git push -u origin refactor": # add the -u flag to create the branch up-stream 
                                        (which is another way of referring to remote repositories)
                                       # add origin, to push this to the remote repository 
                                        ("origin" is used to specify the remote repository)
                                       # add name of the branch we are pushing 
                                        (name of the branch we are "sending" to the remote repository)

GIT MERGE AND GIT REBASE (see also word file with pictures)

git merge and git rebase do the same thing: they merge a new branch into the main branch
BUT they do this differently: git merge preserves commit history while git rebase re-writes it as a linear commit history

Initially, Git searches for 3 commits:
(1):    the common ancestor commit
        at this point in time, both branches had the same content (and then evolved differently)
(2):    latest commit on one branch
(3):    latest commit on the other branch

git merge
"git merge <branch b>": merges the new branch b into the main branch b
    fast-forward merge, when main branch a does not have new commits since the branching happened
                        and new branch b has two new commits since the branching happened
                        finally we have branch ab, commit history: C1, C2, C3
                        C1 common ancestor commit
                        C2, C3 commits of branch b
    three-way merge     when main branch a has one commit since the branching happened
                        and new branch b has two new commits since the branching happened
                        finally we have branch ab, commit history: C1, C2, C3, C4, C5
                        C1 common ancestor commit
                        C2, C3 commits of branch b
                        C4 commit of branch a
                        C5 is the MERGE COMMIT

git rebase
git rebase does the merge in THREE STEPS
when main branch a has one commit C3 since the branching happened
and new branch b has two new commits C2, C4 since the branching happened

git checkout <branch b>: switch into branch b
git rebase <branch a>  : change the base of branch a
                         substitute base of branch a with base of branch b
                         base  = history of commits
                         STEP 1, remove C3 commit of branch a
git checkout <branch a>: switch into branch a
                         apply the commits from branch b that we want to integrate 
                         add base of branch b
                         we have temporary branch ab, commit history: C1, C2, C4
                         C1 common ancestor commit
                         C2, C4 commits of branch b
                         STEP 2, add commits of branch b
git merge <branch b>:   merge changes of branch b to branch a
                        add base of branch a on top of the base of branch b
                        commit C3 of branch a is now re-applied BUT ON TOP of the commits from branch b
                        we have final branch ab, commit history: C1, C2, C4, C3
                        C1 common ancestor commit
                        C2, C4 commits of branch b
                        C3 commit of branch a
                        STEP 3, add commits of branch a on top of commits of branch b

switch into branch b
remove the base of branch a
paste the base of branch b (use base of branch b as a base for branch a), temporary branch ab is produced
on the temporary branch ab, paste again the base of branch a after the base of branch b
"""
#%%
"""
3.3.1 The Pull-Merge-Push Workflow

I have the remote repository health_checks
I cloned/copied it to my machine as a local repository

I apply changes to the local
when trying to push them to the remote I get an error because
someone else also made changes to the remote
So, first pull, manage any merge conflicts and then push

(Git will try to do all possible automatic merges and 
only leave manual conflicts for us to resolve when the automatic merge fails.)

merge conflict marker = >>>

EXAMPLE 
cd health-checks # I am on my local
nano all_checks.py # open editor, apply changes to this file 
CTRL O, ENTER, CTRL X # save changes
git add -p            # review changes before adding them to the staging area
git commit -m 'renamed a function'
                      # commits the change to my local repository
                      and also adds a commit message
git push              # pushes changes to the remote repository (updates the remote with the changes we did on our local)
                      # we see that git push FAILED
                      WHY? because "the remote contains work that you do not have locally.
                      'first integrate remote changes before pushing again'
                      
git pull              # updates local repository for changes made to the remote repository  
                      # I see the message: 'Merge conflict in all_checks.py
                      fix conflicts and then commit the result'
                      So, there is a merge conflict that Git cannot resolve by itself,
                      maybe it is done on the same part of the file "all_checks.py" and Git does not know which change to apply (change in the remote or change in the local?)
                      Other merges were done without this message
                      Only the change happening at the same line in the file, produced this conflict and needs our input
git log --graph --oneline --all
                      # display all commits
                        --graph for displaying commits as a graph
                        --oneline for displaying one line per commit   
                        --all for 
                        we see all commits in all branches (the main and the other branches)
                        main branch (our local repository)
                        origin/main branch (the remote)
                        the branch 'origin/experimental' (on the remote repository) 
                        we will do a three-way merge

git log -p origin/master # 
                          git log -p shows associated patches, text is longer
                          we choose to see commits on the branch "origin/master", the main branch of the remote repository
                          remember, I am investigating the merge conflict
                          exit with q
nano all_checks.py  # open editor, display the script in this file
                     I see the conflict marker >>>>>>>                   
                    So, I open this on my local and see the conflict markers on the py file?
                    WE FIX THE CONFLICT HERE (keep the change I want), after that I will do: git add and git commit to finish the merge
                    If we want to search for other conflicts search for >>>
CTRL O, ENTER, CTRL X
git add all_checks.py   # add the modified file to the staging area
git commit              # commit the file to the local repository
                        # this command opens the editor
                        I see the health-check/.git/COMMIT_EDITMSG
                        so I see the commit message
                        it tells me that this is a MERGE:)
                        'it looks like you may be commiting a merge.'
                        The editor message shows that it is performing a merge of the remote branch with the local branch
                        We can add extra information to this message
                        The merge is ready, we can push this merge to the remote again
git push                # pushes changes to the remote repository (updates the remote with the changes we did on our local)
                        # now this push is successful
                        
git log --graph --oneline # we see all commits in all branches (the main and the other branches)                     
                           the latest commit is the merge

when Git needs to do a three-way merge, 
we end up with a separate commit for merging the branches back into the main tree.

"""
#%%
"""
3.3.2 Pushing Remote Branches

LOGIC: I have remote on GitHub, local on my machine
There is the origin/main branch on the remote
There is the main branch on my local
I create another branch on my local called "refactor"
I push the branch "refactor" on the remote for others to see, to test and tell me if they like it.
So I am adding a new branch to the origin/main branch on the remote with a special git push command
See next section on what to do 1) if the collaborators like the new branch 2) if they do not like it


I have the remote repository health_checks
I cloned/copied it to my machine as a local repository

I have the main branch on my local repository
then I can create other branches to do my tests again on my local repository

code refactoring =  is the process of restructuring existing computer code

EXAMPLE
cd health-checks
git checkout -b refactor  # creates a new branch and switches into it
                            I created a new branch called "refactor"
                            I switched to this branch
nano all_checks           # open the nano editor, I am making changes to this file
CTRL O, ENTER, CTRL X     # save the changes
./all_checks              # run the file, it works
git commit -a -m 'I corrected a function'
                          # stage and commit in one step
                          so, this happens on my local repository, on the branch "refactor"
nano all_checks           # do additional changes                           
CTRL O, ENTER, CTRL X     # save the changes
./all_checks              # run the file,it still works
git commit -a -m 'add an iteration'
                          # stage and commit in one step
nano all_checks           # open the nano editor, I am making changes to this file
CTRL O, ENTER, CTRL X     # save the changes
./all_checks              # run the file,it works
git commit -a -m 'print more errors'
                          # stage and commit in one step

so, we have 3 commits in the branch "refactor"
before merging the branch "refactor" to the main branch,
we will push this to the remote so our collaborators can view it, test it and tell us if it is ready for merging

the first time we push a branch to the remote repository,
we add a few more parameters to the command "git push"

git push -u origin refactor # add the -u flag to create the branch up-stream ( which is another way of referring to remote repositories)
                            # add origin, to push this to the remote repository ("origin" is used to specify the remote repository)
                            # add name of the branch we are pushing (name of the branch we are "sending" to the remote repository)
I get the message "create a pull request for 'refactor' on GitHub by visiting: ...
The branch "refactor" has been created in the remote repository!! It is a new branch for the remote repository

Now that our branch "refactor" is pushed to the remote repository,
it can be reviewed by our collaborators
                        
"""
#%%
"""
3.3.3 Rebasing Your Changes

please see previous section 3.3.2
Our collaborators APPROVE the new branch "refactor" that we created on our local and we pushed to the remote,
SO 
now we will merge this new branch into the origin/main branch of the remote repository

See theory for merging on Week 2

we can merge two branches with:
1) git merge <branch>: merges one branch into another, creates a new commit called Merge Commit                      
                       (Remember: when I want to merge a new branch into the main branch,
                       first I have to switch to the main branch and THEN do the merge)
                       
2) git rebase <branch>: merges a new branch to the main branch, re-arranges sequence of commits
                        after the merge, on the updated main branch we see,
                        first the commits of the new branch then the commits of the main branch 
                        (we disrupted the chronological order).
                        git rebase re-writes the commit history to produce a straight, linear succession of commits.
git rebase <branchname>: to change the base of the current branch to be branchname                       
Rebasing means changing the base commit that's used for our branch.

Difference between git merge and git rebase: 
git merge creates a new merge commit
git rebase re-writes sequence of commits

The golden rule of git rebase is to never use it on public branches.

In-Video Question
what does the git rebase refactor do?
It moves the current branch on top of the refactor branch

My notes for git rebase
git rebase main         step 1 "cut" commit history of branch main
git checkout refactor   step 2 "copy" commit history of branch refactor
git merge refactor      step 3 "paste" commit history of branch refactor, then commit history of branch "main" into the branch "main"

EXAMPLE

git checkout main      # we switch into the main branch on our local
                       switched to branch 'main'
                       Your branch is up to date with 'origin/main'
git pull              # updates local repository for changes made to the remote repository                       
                        Git tells us it updated our local main branch with changes that a colleague made on the origin/main branch on the remote repository
at this point, the changes that we have in the branch "refactor" can no longer be merged 
through fast forwarding into the main branch. 
That's because there's now an extra commit in the master that's not present in the refactor.                      
Lets see how this looks like with git log --graph --oneline --all

git log --graph --oneline --all
                       # displays commits on all branches in local and remote
                       we see a complex history tree
To make history of commits LINEAR we will use git rebase

git checkout refactor # we switch into the branch "refactor"
                       Switched to branch 'refactor'
                       Your branch is up to date with 'origin/refactor'
                       
git rebase main      # rebases commit history of branch "main" STEP 1
                     First, rewinding head to replay your work on top of it...
git log --graph --oneline --all
                     # displays commits on all branches in local and remote
                     now we can see the main branch and linear history of the commits
git checkout main    # switch to branch " main" STEP 2

git merge refactor   # merge changes of branch refactor" into the branch "main"
                      the commits on branch main are now reapplied - but on a new position, 
                      on top of the integrated commits from branch refactor
                      (the commits on branch main are re-based).
we were able to merge our branch through a fast forward merge and keep our history linear.

Now that we have merged the branch refactor into the brach main,
we can get rid of it both remotely and locally

git push --delete origin refactor
                     # delete a branch in a remote repository
                     # removes the remote branch
                     
git branch -d refactor # delete a branch in my local repository
                       # removes the local branch

git push             # apply changes done to our local TO the remote repository

WE USED GIT REBASE TO INTEGRATE A NEW BRANCH TO THE MAIN BRANCH, BY KEEPING A LINEAR HISTORY OF COMMITS
"""
#%%
"""
3.3.4 Another Rebasing Example

In 3.3.3, we used git rebase in order to 
merge/integrate a new branch into the main branch by keeping commit history linear.

Here, we will merge our changes to the main branch WITH the changes of another person on the main branch,
by also keeping the commit history linear

EXAMPLE
remote repository on GitHub: health-checks
cloned local repository on my machine: health-checks
both repositories are updated, no difference between them

nano all_checks.py # open this and make changes
CTRL O, ENTER, CTRL X # save changes
git commit -a -m 'Added a function' # this adds and commits in one step
                                    we commited a change in our local
git fetch          # fetches changes from the remote repository BUT DOES NOT merge them to our local repository             
                   # we want to update our local with the changes from the remote
                     but we will not use git pull to do  git fetch + git merge  
                   IN THIS CASE WE WANT TO KEEP COMMIT HISTORY LINEAR, SO WE'LL USE GIT REBASE BELOW!                                 
                   Indeed there are changes to the remote
git rebase origin/main # rebases commit history of branch "origin/main" STEP 1  "cut" commit history                 
                       WE HAVE A CONFLICT, WE NEED TO FIX IT
nano all_checks.py # open this and remove conflicts manually
./all_checks.py    # run this , it works
git add all_checks.py # add it to the staging area on my local

git rebase --continue # NOW CONTINUE WITH THE REBASE
                       rebase has finished successfully

git log --graph --oneline # see commit history
                          we see we've applied our change on top of the other changes without needing a three-way merge

git push              # apply changes to our local TO the remote

WE KEPT COMMIT HISTORY LINEAR
"""
#%%
"""
3.3.5 Best Practices for Collaboration

1) always synchronize your branches before starting any work on your own.
2) avoid having very large changes that modify a lot of different things
make many small changes and commit them 
3) when working on a big change, it makes sense to have a separate feature branch.
4) regularly merge changes made on the master branch back onto the feature branch.                      
5) have the latest version of the project in the master branch and 
   a stable version of the project on a separate branch.
6) do not rebase changes that have been pushed to remote repositories
7) write good commit messages
                           
"""
#%%
"""
3.3.6 Conflict Resolution Cheat Sheet

Merge conflicts are not uncommon when working in a team of developers, or on Open Source Software. Fortunately, GitHub has some good documentation on how to handle them when they happen:

https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts
https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line
You can also use git rebase <branchname>: to change the base of the current branch to be branchname

The git rebase command is a lot more powerful.  Check out this link for more information.
"""
#%%
"""
3.3.7 Practice Quiz

1.
Question 1
If you’re making changes to a local branch 
while another user has also made changes to the remote branch, 
which command will trigger a merge?

git push
git pull CORRECT
git rebase
git fetch

Nice job! The git pull command runs git fetch with the given parameters, then calls git merge to merge the retrieved branch heads into the current branch.
2.
Question 2
Which of the following is a reason to use rebase instead of merging?

When you want to keep a linear commit history CORRECT
When you want a set of commits to be clearly grouped together in history
When you are on a public branch
When pushing commits to a remote branch

Way to go! git rebase is useful for maintaining a clean, linear commit history.
3.
Question 3
Where should we keep the latest stable version of the project?

The master branch
A separate branch from the master branch CORRECT
The debug branch
A remote branch

Great work! It's common practice to keep the latest version in the master branch and the latest stable version in a separate branch.
4.
Question 4
Which of the following statements represent best practices for collaboration? (check all that apply)

When working on a big change, it makes sense to have a separate feature branch.
You should always rebase changes that have been pushed to remote repos.
Always synchronize your branches before starting any work on your own. CORRECT
Avoid having very large changes that modify a lot of different things. CORRECT

Awesome! That way, whenever you start changing code, you know that you're starting from the most recent version, and you minimize the chances of conflicts or the need for rebasing.
Woohoo! Instead, try to make changes as small as possible, as long as they’re self-contained.
5.
Question 5
What command would we use to change the base of the current branch?

git checkout <branchname>
git pull
git rebase <branchname> CORRECT
git fetch

Right on! You can also use git rebase <branchname> to change the base of the current branch to be <branchname>.
"""
