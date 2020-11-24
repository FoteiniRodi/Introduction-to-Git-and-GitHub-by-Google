#%%
"""
Introduction to Git and GitHub, by Google

WEEK 2 – Using Git Locally

2.3 Branching and Merging
    2.3.1 What is a branch?
    2.3.2 Creating New Branches
    2.3.3 Working with Branches
    2.3.4 Merging
    2.3.5 Merge Conflicts
    2.3.6 Git Branches and Merging Cheat Sheet
    2.3.7 Practice Quiz

MY SYNOPSIS

MASTER BRANCH
default branch, Git creates it for us when a new Repository is initialized
represents the known good state of a project, the current working state

BRANCH
we create this branch
represents an independent line of development in a project
represents our efforts to improve the Master branch
if our efforts are successful then we merge them into the Master branch (incorporate the branch into the Master branch)

What is the purpose of organizing repositories into branches?
Answer: to enable changes to be worked on, without disrupting the most current working state

COMMAND "git branch":               it shows all branches in our Repository
COMMAND "git branch <branch>":      creates a new branch

COMMAND "git checkout <branch>":    switches to this branch
COMMAND "git checkout -b <branch>": creates a new branch and switches into it

Attention: git checkout <file>, reverts a file
           git checkout <branch>, switches into this branch 

Attention:
when we switch from one branch to another, 
we see working tree and commit history of the branch we selected

COMMAND "git branch -d <branch>": -deletes a branch
                                  -if there are changes to this branch, not MERGED to the Master branch,
                                      Git asks us what to do
                                  -if we are sure we want to delete it without merging it then,
                                      run 'git branch -D <branch>'.
COMMAND "git branch -D <branch>": Forcibly deletes the branch                               

COMMAND "git merge <branch>" : merges the branch to the Master branch (branch is incorporated to the Master branch)
                               combines branched data and history together 
                               (we merge a branch to the Master branch)
Attention
when I want to merge a branch into the Master branch,
first i have to switch to the Master branch and THEN do the merge

Attention:
What happens when we merge two branches?
Both branches are pointing to the same commit

Git uses two different algorithms to perform a merge:
    1 fast-forward
    2 three-way merge
My notes for MERGE
1) we have the Master branch
   we create a new branch
   IF we do not make a commit on the Master branch after we create the new branch, then 
   we merge with fast-forward
2) we have the Master branch
   we create a new branch
   IF we do make a commit on the Master branch after we create the new branch, then 
   we merge with three-way 
   2-1) IF the changes were made on different files or different part of the file, merge is successful
   2-2) IF  the changes were made on same file or same part of the file, Git does not know how to merge
        and will raise a MERGE CONFILCT

Merge Conflicts happen when we try to merge a branch into the Master branch,
but we have made a commit on the Master branch AFTER the new branch was created.(three-part merge)
Futhermore, 
the commits (on master branch and on new branch) are due to changes made on the SAME file (or same part of file),
so Git does not know how to do the merge and raises a MERGE CONFLICT
In other words,
both branches we're trying to merge have different edits to the same part of the same file

Attention
What's the advantage of Git throwing a merge conflict error in cases of overlap?
Answer: it prevents loss of work if two lines overlap


COMMAND "git merge --abort":  throw the merge away and start over
                              This will stop the merge and reset the files in your working tree 
                              back to the previous commit before the merge ever happened
                              If there are merge conflicts (meaning files are incompatible), 
                              --abort can be used to abort the merge action.

COMMAND "git log": -display a list of commits that were made
                    -most recent commit appears on top
COMMAND "git log --graph --oneline": displays all commits                    
                                    --graph for displaying commits as a graph
                                    --oneline for displaying one line per commit                    
                                    This format helps us better understand the history of our commits 
                                    and how merges have occurred.
                                    This shows a summarized view of the commit history for a repo.


"""
#%
"""
2.3.1   What is a branch?

BRANCH
it is a pointer to a particular commit
it represents an independent line of development in a project 
(Of which the commit it points to, is the latest link in a chain of developing history)

Branches make it really easy to experiment with new ideas or strategies and projects
When you want to add a feature or fix something, you can create a new branch and do your development there.
You can MERGE back into the master branch, 
    when you've got something you like, or 
    discard your changes without negative impact if they don't work out.
In Git, branches are used all the time, as a part of the normal development workflow.
After using a branch then we merge it to the master branch

MASTER BRANCH
Master branch = current working state
it is the default branch, that Git creates for us when a new Repository is initialized
The master branch is commonly used to represent the known good state of a project
When you want to develop a feature or try something new in your project, 
    you can create a separate branch to do your work without worrying about making mistakes on the MASTER branch

In-Video question
What is the purpose of organizing repositories into branches?
Answer: to enable changes to be worked on, without disrupting the most current working state
"""
#%%
"""
2.3.2   Creating New Branches

COMMAND "git branch"
to list, create, delete and manipulate branches

COMMAND "git branch":                   it shows all branches in our Repository
COMMAND "git branch <new branch>":      creates a new branch
COMMAND "git checkout <new branch>":    switches to the new branch
COMMAND "git checkout -b <new branch>": creates a new branch and switches into it

In-Video question
What does the git checkout -b new branch command do?
Answer: creates a new branch and switches to it

EXAMPLE
cd checks
            navigate to the Repository 

git branch
            list all branches in this Repository
            * master

git branch new-feature
            we are adding the branch "new-feature"
git branch
            list all branches in this Repository
            Our new branch was created based on the value of head
            we are still on the Master branch as indicated by the asterisk
            * master
            new-feature
            
git checkout new-feature
            now we are switching, from the Master branch into the branch "new-feature"
            Switched to branch 'new-feature'
            D       areas1.py
git branch
            list all branches in this Repository
            now we are working on the new branch
            the asterisk is now next to branch "new-feature"
              master
              * new-feature

creating a branch and switching to it immediately is a common task
that is why a command exists to create and switch in one step
git checkout -b <new branch>
      
git checkout -b even-better-feature
            this command helps us create a new branch AND 
            switch into it at the same time
            Switched to a new branch 'even-better-feature'

git branch   
            list all branches in this Repository
            now we are on the branch "even-better-feature"
            * even-better-feature
              master
              new-feature
nano free_memory.py
            open the nano editor, create a new py file


git add free_memory.py

git commit -m 'Add an empty free_memory.py'
            [even-better-feature e2d9221] Add an empty free_memory
             1 file changed, 6 insertions(+)
             create mode 100644 free_memory.py
git log -2
            we display the 2 latest commits
            in the most recent commit,
            we see the HEAD indicator that informs us about the branch
            The branch "even-better-feature" is ahead of the Master branch
            
            in the commit before the most recent,
            we see the other two branches: new-feature and Master
            commit e2d9221962c4e60e1ad7ad41a57ec39dcc180a85 (HEAD -> even-better-feature)
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Sat Nov 21 08:17:22 2020 +0200
            
                Add an empty free_memory
            
            commit b6182f460a56bc015d271ade1f84543442635edf (new-feature, master)
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Thu Nov 19 08:27:48 2020 +0200
            
                Revert "New name for find-error.py"
            
                Rollback reason: the previous name was actually better
            
                This reverts commit 3e6535b49317794d84997309b05a8c0d54251e35.

"""
#%%
"""
2.3.3   Working with Branches

previously, we created a branch ("even-better-feature"), different than the Master branch and 
added a commit to it ("free_memory.py")

when we switch from one branch to another, we see working tree and commit history of the branch we selected

COMMAND "git branch -d <branch>": -deletes a branch
                                  -if there are changes to this branch, not MERGED to the Master branch,
                                      Git asks us what to do
                                  -if we are sure we want to delete it without merging it then,
                                      run 'git branch -D <branch>'.


In-Video question
How does git checkout switch branches?
Answer:by updating the working tree to match the selected branch


EXAMPLE
cd checks
            navigate to the Repository
git status
            display the status of the Repository
            On branch even-better-feature
            nothing to commit, working tree clean
ls -l
            display current contents of our directory
            total 1
            -rwxr-xr-x 1 jimko 197609 53 Nov 21 08:15 free_memory.py*

So, we are in a clean working tree, in the branch "even-better-feature"
and we see the new file "free_memory.py"

git checkout master
            we switch to the Master branch
            Switched to branch 'master'
git log -2
            display latest 2 commits AT THE MASTER BRANCH!!
            commit b6182f460a56bc015d271ade1f84543442635edf (HEAD -> master, new-feature)
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Thu Nov 19 08:27:48 2020 +0200
            
                Revert "New name for find-error.py"
            
                Rollback reason: the previous name was actually better
            
                This reverts commit 3e6535b49317794d84997309b05a8c0d54251e35.
            
            commit fe7688b4007a0a2954b1632fbf0701c7c0b3fd10
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Thu Nov 19 08:23:56 2020 +0200
            
                Revert "I added a .gitignore file, to ignore .DS_STORE files"
            
                This reverts commit a6a26a480dca83a563bdbf895b9a86e99e4f9420.

When we switch to a different branch using git checkout, 
under the hood, git changes where head is pointing. 
Thanks to this checkout, head went from pointing to the latest commit in the even better feature branch to
 the most recent commit of the master branch.

ls -l
            display current contents of our directory
            total 0
            the "free_memory.py" is not here

This demonstrates that when we switch branches in git, the working directory or working tree and commit history will be changed to reflect the snapshot of our project in that branch.    
My notes: SO, the working directory and commit history are unique to each branch?
Since free memory py was committed on another branch, 
it doesn't show up in the history or working directory of the master branch.
each branch is just a pointer to a specific commit in a series of snapshots

git branch -d
            this deletes a branch

git branch
            list all braches in our Repository
              git branch -d 
            * master
              new-feature

git branch -d new-feature
            this deletes the branch "new-feature"
            Deleted branch new-feature (was b6182f4).

git branch
            list all braches in our Repository
             even-better-feature
            * master
If there are changes in the branch we want to delete that haven't been merged back into the master branch, git will let us know with an error.

git branch -d even-better-feature
              now we try to delete the branch "even-better-feature"
              BUT we get an error
              because there were changes in the branch NOT MERGED into the Master branch
              error: The branch 'even-better-feature' is not fully merged.
              If you are sure you want to delete it, run 'git branch -D even-better-feature'.

"""
#%%
"""
2.3.4   Merging

Merging
term that Git uses for combining branched data and history together
(we merge a branch to the Master branch)

COMMAND ""git merge <branch> : merges the branch to the Master branch
                               combines branched data and history together 
                               (we merge a branch to the Master branch)

In-Video question
What happens when we merge two branches?
Answer: both branches are pointing to the same commit

Git uses two different aldorithms to perform a merge:
    1 fast-forward
    2 three-way merge

FAST-FORWARD MERGE
when all the commits in the checked out branch are also in the branch that's being merged. 
If this is the case, we can say that the commit history of both branches doesn't diverge. 
In these cases, all Git has to do is update the pointers of the branches to the same commit, 
and no actual merging needs to take place.

THREE-WAY MERGE
when the history of the merging branches has diverged in some way, 
and there isn't a nice linear path to combine them via fast-forwarding. 
This happens when a commit is made on one branch AFTER the point when both branches split.
In our case, this could have happened if we made a commit on the master branch 
after creating the other branches.
When this occurs, Git will tie the branch histories together with a new commit. 
And merge the snapshots at the two branch tips with the most recent common ancestor, 
the commit before the divergence. 
To do this successfully, Git tries to figure out how to combine both snapshots. 
If the changes were made in different files, or in different parts of the same file, 
Git will take both changes and put them together in the result. 
If instead the changes are made on the same part of the same file, Git won't know how to merge those changes, 
and the attempt will result in a merge conflict. 

My notes for MERGE
1) we have the Master branch
   we create a new branch
   IF we do not make a commit on the Master branch after we create the new branch, then 
   we merge with fast-forward
2) we have the Master branch
   we create a new branch
   IF we do make a commit on the Master branch after we create the new branch, then 
   we merge with three-way 
   2-1) IF the changes were made on different files or different part of the file, merge is successful
   2-2) IF  the changes were made on same file or same part of the file, Git does not know how to merge
        and will raise a MERGE CONFILCT




EXAMPLE

git branch
                list all braches in our Repository
                OK, we are on the Master branch
                  even-better-feature
                * master
git merge even-better-feature
                we merge the branch "even-better-feature" into the Master branch
                 Updating b6182f4..e2d9221
                Fast-forward
                 free_memory.py | 6 ++++++
                 1 file changed, 6 insertions(+)
                 create mode 100644 free_memory.py
THIS IS A FAST-FORWARD MERGE!

git log
                -display a list of commits that were made
                -in the most recent commit which appears on top:
                the HEAD indicator pints at Master
                and we see that both Master branch and even-better-feature branch 
                are now both pointing to the same commit
                
                commit e2d9221962c4e60e1ad7ad41a57ec39dcc180a85 (HEAD -> master, even-better-feature)
                Author: FoteiniRodi <foteinirodis@gmail.com>
                Date:   Sat Nov 21 08:17:22 2020 +0200
                
                    Add an empty free_memory
                
                commit b6182f460a56bc015d271ade1f84543442635edf
                Author: FoteiniRodi <foteinirodis@gmail.com>
                Date:   Thu Nov 19 08:27:48 2020 +0200
                
                    Revert "New name for find-error.py"
                
                    Rollback reason: the previous name was actually better
                
                    This reverts commit 3e6535b49317794d84997309b05a8c0d54251e35.
                
                commit fe7688b4007a0a2954b1632fbf0701c7c0b3fd10
                Author: FoteiniRodi <foteinirodis@gmail.com>
                Date:   Thu Nov 19 08:23:56 2020 +0200
                
                    Revert "I added a .gitignore file, to ignore .DS_STORE files"
                
                    This reverts commit a6a26a480dca83a563bdbf895b9a86e99e4f9420.
                
                commit a6a26a480dca83a563bdbf895b9a86e99e4f9420
                Author: FoteiniRodi <foteinirodis@gmail.com>
                Date:   Tue Nov 17 17:28:24 2020 +0200
                
                    I added a .gitignore file, to ignore .DS_STORE files
                
                commit 3e6535b49317794d84997309b05a8c0d54251e35
                Author: FoteiniRodi <foteinirodis@gmail.com>
                Date:   Tue Nov 17 17:15:57 2020 +0200
                
                    New name for find-error.py
                
                commit 1de27b413ba68cff8e63c75ea690cfa584ad589a
                Author: FoteiniRodi <foteinirodis@gmail.com>
                Date:   Tue Nov 17 17:04:39 2020 +0200
                
                    Deleted un-needed file
                
                commit 5a8dc2aab9e45ebbd1f899fe95844aa21f6fa421
                Author: FoteiniRodi <foteinirodis@gmail.com>
                Date:   Sun Nov 15 18:17:38 2020 +0200
                
                    Add program.py to checks
                              

"""
#%%
"""
2.3.5   Merge Conflicts

Merge Conflicts happen when we try to merge a branch into the Master branch,
but we have made a commit on the Master branch AFTER the new branch was created.(three-part merge)
Futhermore, 
the commits (on master branch and on new branch) are due to changes made on the SAME file (or same part of file),
so Git does not know how to do the merge and raises a MERGE CONFLICT

In other words,
both the branches we're trying to merge have different edits to the same part of the same file

In-Video question
What's the advantage of Git throwing a merge conflict error in cases of overlap?
Answer: it prevents loss of work if two lines overlap


COMMAND "git merge --abort":  throw the merge away and start over
                              This will stop the merge and reset the files in your working tree 
                              back to the previous commit before the merge ever happened  

COMMAND "git log --graph --oneline": displays all commits                    
                                    --graph for displaying commits as a graph
                                    --oneline for displaying one line per commit                    
                                    This format helps us better understand the history of our commits 
                                    and how merges have occurred.

EXAMPLE- resolve a merge conflict that I created on purpose

cd checks
git branch
                    remember, I merged the branch even-better-feature into the Master branch 
                      even-better-feature
                    * master

nano free_memory.py
                    instead of pass write: Checks if there is enough memory in the computer
                    #!/usr/bin/env python3
                    def main():
                        pass
                    main()
                    #!/usr/bin/env python3
                    def main():
                        Checks if there is enough memory in the computer
                    main()

git commit -a -m 'I added a comment to function main()'
                    now I am adding to staging area
                    and
                    commiting the change IN ONE STEP
                    ALL THIS IN THE MASTER BRANCH

git checkout even-better-feature
                    switch from Master branch to this branch
                    Switched to branch 'even-better-feature'

                    remember "even-better-feature" originally contained the free_memory.py,
                    and we merged it to the Master branch

nano free_memory.py
                    we see the free_memory.py as it originally is
                    because the change we made above was on the Master branch
                    #!/usr/bin/env python3
                    def main():
                        pass
                    main()
                    NOW instead of pass write: print("Everything is OK.") 
                     #!/usr/bin/env python3
                    def main():
                        print("Everything is OK.")
                    main()
                                        
CTRL-O, ENTER, CTRL-X
                    
git commit -a -m 'I added print("Everything is OK.")'
                    now I am adding to staging area
                    and
                    commiting the change IN ONE STEP
                    ALL THIS IN THE "even-better-feature" BRANCH 

git checkout master
                    switch from "even-better-feature" into the Master branch

git merge even-better-feature
                    we try to merge the even-better-feature branch into the Master branch
                    we get the ERROR:
                        
                    Auto-merging free_memory.py
                    CONFLICT (content): Merge conflict in free_memory.py
                    Automatic merge failed; fix conflicts and then commit the result.
                    
                    So, Git cannot merge the branch into the Master branch
                    while on the Master branch, I made change 1 to the py file at the "pass" part
                    while on the even-better-feature branch, I made change 2 to the py file at the "pass" part
                    change 1 is different than change 2
                    therefore Git does not know which change to apply and cannot merge the branch into the Master branch

git status
                    On branch master
                    You have unmerged paths.
                      (fix conflicts and run "git commit")
                      (use "git merge --abort" to abort the merge)
                    
                    Unmerged paths:
                      (use "git add <file>..." to mark resolution)
                            both modified:   free_memory.py
git branch
                    displays all branches
                    we are on the Master branch
                      even-better-feature
                    * master

nano free_memory.py
                    we open the changed file
                    Git has added some information to our files 
                    to tell us which parts of the code are conflicting. 
                    we see HEAD and even-better-feature
                    
                    previously while on the Master branch, deleted pass and added:
                    Checks if there is enough memory in the computer  
                    
                    previously while on the even-better-feature branch,deleted pass and added:
                    print("Everything is OK.")
                    
                    So, Git tells us what we did and where 
                    
                    Finaly we decide to keep BOTH CHANGES
                    and delete the merger markers
                    
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
CTRL-O, ENTER, CTRL-X

git add free_memory.py
                    we add the changed file to the staging area

git status
                    On branch master
                    All conflicts fixed but you are still merging.
                      (use "git commit" to conclude merge)
                    
                    Changes to be committed:
                            modified:   free_memory.py

git commit
                    we add the file from the staging area to the Repository    
                    we have not added a Commit Message so the editor opens
                    
                    This looks different than other commits because it is a merge
                    
                    
                    
                    Merge branch 'even-better-feature'
                    
                    # Conflicts:
                    #       free_memory.py
                    #
                    # It looks like you may be committing a merge.
                    # If this is not correct, please run
                    #       git update-ref -d MERGE_HEAD
                    # and try again.
                    
                    
                    # Please enter the commit message for your changes. Lines starting
                    # with '#' will be ignored, and an empty message aborts the commit.
                    #
                    # On branch master
                    # All conflicts fixed but you are still merging.
                    #
                    # Changes to be committed:
                    #       modified:   free_memory.py

now the merge conflict has been resolved

git log --graph --oneline
                    displays all commits
                    --graph for displaying commits as a graph
                    --oneline for displaying one line per commit
                    
                    This format helps us better understand the history of our commits and how merges have occurred.
                    
                    *   48791ed (HEAD -> master) Merge branch 'even-better-feature'
                    |\
                    | * 5368a6f (even-better-feature) I added print("Everything is OK.")
                    * | 2b95dfc I added a comment to function main()
                    |/
                    * e2d9221 Add an empty free_memory
                    * b6182f4 Revert "New name for find-error.py"
                    * fe7688b Revert "I added a .gitignore file, to ignore .DS_STORE files"
                    * a6a26a4 I added a .gitignore file, to ignore .DS_STORE files
                    * 3e6535b New name for find-error.py
                    * 1de27b4 Deleted un-needed file
                    * 5a8dc2a Add program.py to checks
                    * e5b068d Add areas1.py

"""
#%%
"""
2.3.6   Git Branches and Merging Cheat Sheet

Command	Explanation & Link
git branch	             Used to manage branches
git branch <name> 	    Creates the branch
git branch -d <name>	Deletes the branch
git branch -D <name>	Forcibly deletes the branch

git checkout <branch> 	Switches to a branch.
git checkout -b <branch>	Creates a new branch and switches to it.

git merge <branch> 	Merge joins branches together. 
git merge --abort	If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.
git log --graph --oneline	This shows a summarized view of the commit history for a repo.

"""
#%%
"""
2.3.7   Practice Quiz


Question 1
When we merge two branches, one of two algorithms is used. 
If the branches have diverged, which algorithm is used?

three-way merge CORRECT
fast-forward merge
merge conflict
orphan-creating merge

2.
Question 2
The following code snippet represents the result of a merge conflict. Edit the code to fix the conflict and keep the version represented by the current branch.

<<<<<<<< HEAD
print("Keep me!")
========
print("No, keep me instead!")
>>>>>>> brancho-cucamonga

since we keep the change by the current branch indicated by HEAD,
we will keep "Keep me!" and delete the other
also I will delete the merger markers
so, print("Keep me!")


3.
Question 3
What command would we use to throw away a merge, and start over?

git checkout -b <branch>
git merge --abort CORRECT
git log --graph --oneline
git branch -D <name>

4.
Question 4
How do we display a summarized view of the commit history for a repo, showing one line per commit?

git log --format=short
git branch -D <name>
git log --graph --oneline CORRECT
git checkout -b <branch>

Question 5
The following script contains the result of a merge conflict. 
Edit the code to fix the conflict, so that both versions are included.

def main():
<<<<<<< HEAD
    print("Start of program>>>>>>>")
=======
    print("End of program!")
>>>>>>> improvement-to-the-code

main()

I will just delete the merge markers
def main():
    print("Start of program>>>>>>>")
    print("End of program!")

main()

"""
