#%%
"""
Introduction to Git and GitHub, by Google

WEEK 3 - Working with Remotes

3.1 Introduction to GitHub
    3.1.1 Intro to Module 3: Working with Remotes
    3.1.2 What is GitHub?
    3.1.3 Basic Interaction with GitHub
    3.1.4 Basic Interaction with GitHub Cheat-Sheet
    3.1.5 Practice Quiz

MY SYNOPSIS
Git is a distributed version control system. 
Distributed means that: each developer has a copy of the whole repository on their local machine.

GitHub is an online service
GitHub hosts Git repositories

create a remote repository on GitHub (name it, provide description of use, initialize with a readme)
copy the URL of the remote repository
on my machine, on the Linux command line write

git clone URL  # clones/copies the remote repository to my machine
               # a directory with same name is created on my machine
               # the directory contains the working tree of the remote repository
cd  health-checks
               # navigate to the created directory
ls -l          # display contents (only a readme file)
nano README.md # add a line here
CTRL-O, ENTER, CTRL-X
git commit -a -m 'I Added a line in the README.md'
               # I did git add, git commit for the local repository
               # I updated my local repository woth the change
git push       # I updated my remote repository too

git pull       # when a change is commited to the remote repository
               I pull it to the local repository to update it

COMMAND "git clone URL": copy a remote repository to my machine (create a local repository)
                         clone a remote repository into a local workspace
COMMAND "git push":      update remote repository for changes made to the local repository
                         push commits from your local repo to a remote repo 
COMMAND "git pull":      update local repsitory for changes made to the remote repository
                         fetch the newest updates from a remote repository 
"""
#%%
"""
3.1.1 Intro to Module 3: Working with Remotes

Until we have used Git LOCALLY
Now, we will learn about GitHub and remote repositories
Being able to use remote repositories allows us to effectively collaborate with others.
Using a version control system like Git 
lets us incorporate the work of different people no matter where they are or when they're working.
"""
#%%
"""
3.1.2 What is GitHub?

Git is a distributed version control system. 
Distributed means that: each developer has a copy of the whole repository on their local machine.

Each copy is a peer of the others. 
But we can host one of these copies on a Git server 
and then use it as a remote repository for the other copies. 
This lets us synchronize work between copies through this server.

If we do not want to to set up a Git server yourself and host your repositories, 
you can use an online service like GitHub.

GitHub is an online service
GitHub is a web-based, Git repository hosting service. 
GitHub hosts Git repositories
In addition to what Git offers, GitHub extra features like 
    bug tracking, 
    wikis, and 
    task management
    
GitHub lets us share and access repositories on the web 
and copy or clone them to our local computer, so we can work on them.    

Other options except GitHub are BitBucket, and GitLab.

On GitHub we can have either a private or a public Repository

Attention: to avoid hackers,  use a secure and private Git server, and limit the people authorized to work on it.

In_video question
Which BEST describes GitHub?
It is a remote repository hosting service for Git
"""
#%%
"""
3.1.3 Basic Interaction with GitHub

Go to https://github.com and create an account

Create a Remote Repository on GitHub
provide a name for the Repository
provide a description of what the Repository will be used for
select Public or Private Repository
Initialize the Repository with a readme file, a gitignore file, a license file

    health checks
    Scripts that check the health of our computers
    private Repository
    initialize with a readme file

Create a local copy of the Repository
Go to Code, then copy the URL
Command "git clone" followed by the URL of the repo.
GitHub conveniently lets us copy the URL from our repo from the interface so that we don't have to type it.
We are now ready to clone this Repository from GitHub to our computer

In_Video question
After making changes to our local repository, how do we update the remote repository to reflect our changes?
Use the git push command to send snapshots to the remote repository

EXAMPLE
create remote repository
clone it to our machine, then on the linux command line

git clone URL        # copy the remote repository in my machine
                     # GitHub will ask for our username and password
                     # HERE the credentials manager opened
                     
Since the repository is called health checks, 
a directory with that name was automatically created for us 
and now has the working tree of the Repository in it.

cd health-checks/   # navigate to this directory
ls -l               # display contents of directory
                    # the Repository contains only the readme file that GitHub created for us
                    # README.md this file is in a special format called "markdown"
                    total 1
                    -rw-r--r-- 1 jimko 197609 65 Nov 22 12:52 README.md

nano README.md      # open the readme and add content
                    This repository will be populated with lots of fancy checks
CTRL-O, ENTER, CTRL-X
now we have to do git add and git commit

git commit -a -m 'I Added a line in the README.md'
                    # this command adds and commits in 1 step
                    [main 1506ac7] I Added a line in the README.md
                    1 file changed, 1 insertion(+)
                    
So, I have updated my local repository
I have to update the remote repository too
I will do that with git push

git push            # updates remote repository
                    # GitHub will ask for our username and password
                    # if we check our repository on GitHub, we should see the updated message.
                    Enumerating objects: 5, done.
                    Counting objects: 100% (5/5), done.
                    Delta compression using up to 4 threads
                    Compressing objects: 100% (2/2), done.
                    Writing objects: 100% (3/3), 355 bytes | 177.00 KiB/s, done.
                    Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
                    To https://github.com/FoteiniRodi/health-checks.git
                       5fb21ea..1506ac7  main -> main

success, I pushed the change on my local repository TO the remote repository on GitHub

How to avoid GitHub asking for our username and password
1 One way is to create an SSH key pair and store the public key in our profile,
 so that GitHub recognizes our computer. 
2 Another option is to use a credential helper which caches our credentials for a time window 
so that we don't need to enter our password with every interaction. 
Git already comes with a credential helper baked in. 
We just need to enable it. 
We do that by calling git config - - global credential.helper cache.

git config - - global credential.helper cache
                     # enable the credential helper
                     # enter our credentials once more
                     after that they will be cached for 15 minutes
                     
git pull             # to retrieve new changes from the repository
                     # we will try this to see if credential helper works
                     # enter our credentials once more
                     after that they will be cached and we will not enter them again                  
"""
#%%
"""
3.1.4 Basic Interaction with GitHub Cheat-Sheet

Basic Interaction with GitHub Cheat-Sheet
There are various remote repository hosting sites:

GitHub
BitBucket
Gitlab.
Follow the workflow at https://github.com/join to set up a free account, username, and password. After that, these steps will help you create a brand new repository on GitHub.

Some useful commands for getting started:

Command	Explanation & Link
git clone URL	Git clone is used to clone a remote repository into a local workspace
git push	Git push is used to push commits from your local repo to a remote repo
git pull	Git pull is used to fetch the newest updates from a remote repository
This can be useful for keeping your local workspace up to date.

https://help.github.com/en/articles/caching-your-github-password-in-git
https://help.github.com/en/articles/generating-an-ssh-key  
"""
#%%
"""
3.1.5 Practice Quiz

Question 1
When we want to update our local repository to reflect changes made in the remote repository, 
which command would we use?

git clone <URL>
git push
git pull CORRECT
git commit -a -m

Question 2
git config --global credential.helper cache 
allows us to configure the credential helper, which is used for ...what?

Troubleshooting the login process
Dynamically suggesting commit messages
Allowing configuration of automatic repository pulling
Allowing automated login to GitHub CORRECT

Question 3
Name two ways to avoid having to enter our password 
when retrieving and when pushing changes to the repo. (Check all that apply)

Implement a post-receive hook
Use a credential helper CORRECT
Create an SSH key-pair CORRECT
Use the git commit -a -m command.

Question 4
Before we have a local copy of a commit, we should download one using which command?

git commit -a -m
git push
git pull
git clone <URL> CORRECT

"""
