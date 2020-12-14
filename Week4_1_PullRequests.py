#%%
"""
Introduction to Git and GitHub, by Google

WEEK 4 - Collaboration

4.1 Pull Requests
    4.1.1 Intro to Module 4: Collaboration
    4.1.2 A Simple Pull Request on GitHub
    4.1.3 The Typical Pull Request Workflow on GitHub
    4.1.4 Updating an Existing Pull Request
    4.1.5 Squashing Changes
    4.1.6 Git Fork and Pull Request Cheat Sheet
    4.1.7 Practice Quiz

MY SYNOPSIS
Pull request: ask the owner of a repository to add our changes to the working tree of the repository

Pull request using only  GitHub
create a pull request directly on github to ask the owner for very small changes
this creates a forked repository which sits on our account
Once you have forked a repo, you own your forked copy. 
This means that you can edit the contents of your forked repository without impacting the parent repo

Fork a repository: copy a repository on github to work on it

Pull request using local and forked
large requests
fork someone else's repository (same repository but it sits on my account on GitHub) 
now I have the forked directory on my GitHub account
clone the forked directory
now I have a local repository on my machine.
Eventually, I will work with my local repository and the forked repository as the remote.
I do changes on the local, push them to my forked 
Then I will do a Pull Request on the original repository on github

git checkout -b add-readme   # to create the file first we create the branch
                             switched to a new branch called "add-readme"
git push -u origin add-readme # push the change to the remote indicated by 'origin' for the first time
                                and write name of file too
                                git push -u origin <filename>
                                we push this my github account, to the forked repository!

Update a Pull request
do a change on our local
push it to our forked on github
then update our pull request to the original

git push                 # push this change to the remote
                         notice it is the second time we do a push
                         so I do not need to use additional info for the git push command

Squash 2 commits in 1, to do a Pull request
git rebase -i main  # squash 2 changes in one commit
pick keyword in editor, pick takes the commits, and rebases them against the branch we selected
we have two options for combining commits
1 squash
2 fix up
Squash combines the commit messages into one. Fixup discards the new commit message

replace pick keyword with squash keyword to squash/incorporate/merge the commit to the previous one

git log --graph --oneline --all --4
           # see last 4 commits

git push -f # force the push even when Git detects conflict, even resulting in permanent data loss.not recommended 

"""
#%%
"""
4.1.1 Intro to Module 4: Collaboration

 In this module, we'll keep exploring the collaboration tools available in Git.
 We'll learn about tools that allow us to send changes to projects that we aren't a member of, 
 help us improve the quality of our code, and let us track our work better. 
 Some of these tools will be specific to GitHub, but most of the Git repository hosting services have similar tools. 
 So the concepts will still apply if you decide to use a different platform. 
 In recent years, GitHub has become a super popular platform for collaboration across many projects. 
 It's used heavily for open-source projects.
 These are projects that allow anyone to use, copy, and modify their code. 
 Having the code published online means that anybody in the world can learn from what the project is doing, 
 and even collaborate on fixes and extra features. 
 It also helps us learn from each other, because we can look at how others have solved the problem that 
 we're tackling. 
"""
#%%
"""
 4.1.2 A Simple Pull Request on GitHub
 
Here we will learn how to:
create a pull request directly on GitHub by using the web interface to edit files.
 
 
go to github and create a remote repository called validations belonging to blue-kale
create the py file validations
#!/usr/bin/env python 3
def validate_user(username, minlen):
    """Checks if the recieved username matches the required conditions"""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise valueError("minlen must be at least 1")
        
    if len(username) < minlen:
        return false
    if not username.isalnum():
        return False
    # usernames cannot begin with a number
    if username[0].isnumeric():
        return False
    return True

Another person, user RF (me) locates an error
I locate a typing error
I click EDIT
Git tells me we i am trying to edit a file, that I do not have access to
Git tells me it created a fork of this project for me, in which I can commit my changes to
if I submit changes to this file, it will create a new branch so that I can send a pull request

FORK/ FORKING
Creates a copy of the remote repository of blue-kale so that it belongs to user RF
User RF can push changes to the forked copy, even when she cannot push changes to the remote repository

A GitHub fork is a copy of a repository (repo) that sits in your account 
rather than the account from which you forked the data from. 
Once you have forked a repo, you own your forked copy. 
This means that you can edit the contents of your forked repository without impacting the parent repo

forking is different than cloning a remote repository++

Typical workflow
create a fork of the repository
then work on that local fork

a forked repository is just like a normal repository, except Github knows which repo it forked from

eventually we can merge our changes back to the remote repo by creating a pull request

PULL REQUEST
A pull request is a commit or series of commits that you send to the owner of the repository so that
 they incorporate it into their tree. 
This is common because only a few people have commit rights to a repository and at the same time,
anybody can suggest, patches, bug fixes or even new features
So with pull requests, unauthorized users can suggest changes and then 
the owners of the repository can evaluate then and then apply them

SO:
correct the typing mistake
propose change/create commit on the forked repository
git created a branch <Name-patch-1> for us
Git tells us that merge can be done, no conflict
allow change from mainteners. Tick this! This way the maintaner can do the change without asking us
submit pull request

on the remote repository, the owner blu-kale can see "Pull requests 1"
"""
#%%
"""
 4.1.3 The Typical Pull Request Workflow on GitHub
  
when we propose a small change for someone else's repository
then editing and creating a pull request on GitHub is OK

BUT
if we want to propose a larger change we will 
fork someone else's repository (same repository but it sits on my account on GitHub) 
now I have the forked directory on my GitHub account
clone the forked directory
now I have a local repository on my machine.
Eventually, I will work with my local repository and the forked repository as the remote.

remote repository: is the forked repository that sits on my account on GitHub
local repository: is the copied forked repository, on my machine


fork a repository: copy it, acquire copy on my github account
clone a repository: copy it, acquire copy on my machine 

EXAMPLE
blue-kale's repository on github: original repository 'rearrange'
fork this to my account: forked repository rearrange or remote repository rearrange
clone this to my machine: local repository rearrange

On my machine:

cd rearrange     # navigate 
ls -l            # display contents
git log          # display commit history

now we can make any changes we like (to the local repository ofcourse)
blue-kale's repository does not have a readme file
we will add it

git checkout -b add-readme   # to create the file first we create the branch
                             switched to a new branch called "add-readme"
nano readme.md              # opens editor
                            we write
                            rearrange
                            =========
                            
                            This module is used for rearranging names
CTRL O, ENTER, CTRL X
git add README.md
git commit -m 'Added a simple README.md file'

Now, to push this change from my local to the forked repository (the remote),
I have to create a corresponding branch

git push -u origin add-readme # push the change to the remote indicated by 'origin' for the first time
                                and write name of file too
                                git push -u origin <filename>
                                we push this my github account, to the forked repository!
then on github                               
we will do a "Pull request" on the original repository 
On the original repository we see that: 
our branch is ahead of the original repositories master branch by one commit, which is the commit we just made. We can start our pull requests by clicking on the Pull Request link.

select "open a pull request"
see if the merge will be successful
Git tells us : able to merge
If this wasn't the case, we'd need to rebase our change against the current branch of the original repo so that it could be merged.
In the text window of the Pull Request write the reason we are proposing a change to the owner of the original repository
In the text window I can explain my change
for the example I write:
"Adding a README file that was missing from the project

also before submitting see the diff at the bottom!                 

each Pull request has an identifier, so if the owner of the original repository asks us to improve our Pull request we can find it easily
"""
#%%
"""
4.1.4 Updating an Existing Pull Request

here, we will update our Pull Request by
doing a change on our local
push it to our forked on github
then update our pull request to the original

When we send a pull request, it's pretty common to receive some comments from the project maintainers asking for some improvements. 

maintaner writes us a comment for our above Pull Request
"This README is tto short. it would be nice to see an example"

so
nano readme.md            # we write
                            rearrange
                            =========
                            
                            This module is used for rearranging names
                            Turns "Lastname, Firstname" into "Firstname Lastname"
                            # Example
                            Calling 'rearrange_name("Turing, Alan")' will return '"Alan Turing"'
CTRL O, ENTER, CTRL X

git commit -a -m 'Added more info to the README'
                         # this stages and commits in one step

git push                 # push this change to the remote
                         notice it is the second time we do a push
                         so I do not need to use additional info for the git push command
                         now the change is on my forked repository on github

Then on github update the previous Pull Request   
I can see this commit under the same Pull Request                     
We just pushed our commit to the same branch as before and GitHub automatically added it to the pull request.
 If we wanted to create a separate pull request, we would need to create a new branch instead. 
+++
"""
#%%
"""
4.1.5 Squashing Changes

Here, we will squash our changes into a SINGLE COMMIT

above I made 1 change, did a commit, created a pull request
then I made another change, did another commit and updated the first pull request
now, the maintaner of the original repository asks us to create a single commit that includes both changes
we will use git rebase -i main to do that

git rebase -i main  # squash 2 changes in one commit
                     rebase commit history of my 2 commits with the base of the main branch (of the original repository)
                     text editor opens with a list of all selected commits
                     pick 736d754 Added a simple README.md file
                     pick 01231b0 Added more info to the README
                     pick takes the commits, and rebases them against the branch we selected
we have two options for combining commits
1 squash
2 fix up

In both cases, the contents of the selected commit are merged into the previous commit in the list.                     
The difference is what happens with the commit messages. 
When we choose squash, 
the commit messages are added together and an editor opens up to let us make any necessary changes. 
When we choose fix up, the commit message for that commit is discarded. 

here, we will use squash to combine the commits in one and also modify the commit description
So let's change the pick command in the second line to squash it into the first one, then we'll save and exit the editor as usual.
                     pick 736d754 Added a simple README.md file
                     squash 01231b0 Added more info to the README
new text appears on editor, I can improve it
CTRL O, ENTER, CTRL X   

I see the message:
Successfully rebased and updated refs/heads/add-readme                

git show  # I see only one commit

git status # git tells us that our local has 1 commit, which is the rebase we just did
            On branch add-readme
            Your branch and 'origin/add-readme' have diverged
            and have 1 and 2 different commits each, respectively
            (use git pull to merge the remote branch into yours)
            nothing to commit, working tree clean

git log --graph --oneline --all --4
           # see last 4 commits
           We can see that the two commits pushed to the origin/add-readme branch 
           show up in a different path than the commit that's currently in our local add-readme branch. 
           This is expected whenever we do a rebase because the old commits are in the remote repo 
           and we have a different commit in our local repo.
git push # push changes from my local to my forked on github
         # fails
         in this case we do not want to do a merge
         we want to replace 1 old commits with 1 new one
         to do this we will use git push -f to force the push as it is!!!

git push -f # force the push
            # succeeds
            
git log --graph --oneline --all --4
            # we see 1 commit on top of main
            previous divergence is gone
            
go to github and see contents of the Pull Request on the original repository


          
"""
#%%
"""
4.1.6 Git Fork and Pull Request Cheat Sheet

Check out the following link for more information:

https://help.github.com/en/articles/about-pull-request-merges
"""
#%%
"""
4.1.7 Practice Quiz

1.
Question 1
What is the difference between using squash and fixup when rebasing?

Squash deletes previous commits.
Squash combines the commit messages into one. Fixup discards the new commit message.CORRECT
Awesome! The fixup operation will keep the original message and discard the message from the fixup commit, 
while squash combines them.
Squash only works on Apple operating systems.
Fixup combines the commit messages into one. Squash discards the commit message.

2.
Question 2
What is a pull request?

The owner of the target repository requesting you to add your changes.
A request sent to the owner and collaborators of the target repository to pull your recent changes.CORRECT
Right on! You send a pull request to the owner of the repository 
in order for them to incorporate it into their tree.
A request to delete previous changes.
A request for a specific feature in the next version.

3.
Question 3
Under what circumstances is a new fork created?

When you want to experiment with changes without affecting the main repository.CORRECT
Nice work! For instance, when you want to propose changes to someone else's project, 
or base your own project off of theirs.
When you clone a remote repository to your local machine.
During a merge conflict.
When there are too many branches.

4.
Question 4
What combination of command and flags will force Git to push the current snapshot to the repo as it is,
possibly resulting in permanent data loss?

git push -f CORRECT
Awesome! git push with the -f flag forcibly 
replaces the old commits with the new one and forces Git to push the current snapshot to the repo as it is. 
This can be dangerous as it can lead to remote changes being permanently lost and is not recommended 
unless you're pushing fixes to your own fork (nobody else is using it) such as in the case 
after doing interactive rebasing to squash multiple commits into one as demonstrated.
git log --graph --oneline --all
git status
git rebase -i

5.
Question 5
When using interactive rebase, 
which option is the default, and takes the commits and rebases them against the branch we selected?

squash
edit
reword
pick CORRECT
Great job! The pick keyword takes the commits and rebases them against the branch we have chosen.
"""
