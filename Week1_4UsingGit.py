#%%
"""
Introduction to Git and GitHub, by Google

WEEK 1 – Introduction to Version Control

1.4 Using Git
1.4.1	First Steps with Git
1.4.2   Tracking Files
1.4.3   The Basic Git Workflow
1.4.4   Anatomy of a Commit Message
1.4.5   Reading: Initial Git Cheat Sheet
1.4.6   Practice Quiz

MY SYNOPSIS

contents:
    TELL GIT WHO YOU ARE
    CREATE/CLONE A REPOSITORY
    WORKING TREE/ STAGING AREA/ REPOSITORY
    2 WAYS TO PERFORM A "git commit"
    TRACKED AND UN-TRACKED FILES by Git
    THE COMMAND "git init"
    THE COMMAND "git status"
    THE COMMAND "git add <filename>"
    THE COMMAND "git commit"
    THE COMMAND "git diff filename"
    THE COMMAND "git log"
    THE COMMANDS ls, ls -l, ls -la, ls -l .git/
    EXAMPLE 1
        create directory, create Repository, commit 1 existing file to the Repository
    EXAMPLE 2
        Modify a file already in a Repository, stage it and commit it
TELL GIT WHO YOU ARE
git config --global user.email "me@example.com" # write my email
git config --global user.name "My name"         # write my username

git config --list                               # if I forget I can find the above with this command

CREATE/CLONE A REPOSITORY
Create or Clone a Repository:
git init                                        # create a repository from scratch
git clone                                       # make a clone of a repository (copy a repository) that already exists somewhere else

cd ..                                           # return to parent directory (for my machine it is /c/Users/jimko, I can see it with the pwd command)

WORKING TREE/ STAGING AREA/ REPOSITORY:
Note: a file is first tracked by Git, with the git add command, and then it can be modified/staged/commited
      the "git add" command helps Git to track a file and then stage it
modified    file is in the working tree     (work bench) we work on modified file in our working tree
staged      file is in the staging area     (wheel cart) the changes to the file are ready to be committed / we add files to the staging area
commited    file is in the repository       (storage) store those changes in the VCS

2 WAYS TO PERFORM A "git commit":
git commit                          # with "git commit" we tell Git to save our changes
                                    # this opens the text editor, then we write the commit message
git commit -m 'commit message'      # git commit -m 'Commit Message', does not open the file.
                                    # it allows us to write the commit message on the command line
Attention: Without a Commit Message the commit will be aborted!!                                  
                                    
every time we commit changes, we take another snapshot, which is annotated with a commit message that we can review later.
If multiple -m flags are given to the command, it concatenates the values as separate paragraphs.
 
TRACKED AND UN-TRACKED FILES by Git
when we create a file or store it in a directory, it starts off as untracked.
we will make it tracked with the "git add <filename>" command

 "git add <filename>":
this command changes a file from untracked to tracked by Git
this command changes a file from modified state to staged state
Git will only commit the changes that have been added to the staging area, 
untracked files or modified files that weren't staged will be ignored.

THE COMMAND "git init":
The command can initialize a new, empty repository
The command can convert an existing, unversioned project to a Git repository
(if we just create a directory and navigate to it, with git init we transform the directory into a Repository)

Executing "git init", creates a .git subdirectory in the current working directory, 
which contains all of the necessary Git metadata for the new repository. 
This metadata includes subdirectories for objects, refs, and template files. 
A HEAD file is also created which points to the currently checked out commit.

If you've already run "git init" on a project directory containing a .git subdirectory, 
you can safely run "git init" again on the same project directory. 
The operation is what we call idempotent; running it again doesn't override an existing .git configuration.

THE COMMAND "git status":
This command displays the status of the working tree. 
It also shows   changes that have been staged, 
                changes that haven't been staged, 
                and files that aren't tracked by Git.

THE COMMAND "git add":
This command adds changes from the working tree to the staging area i.e., 
it gathers and prepares files for Git before committing them. 
In other words, it updates the index with the current content found in the working tree 
to prepare the content that's staged for the next commit.

THE COMMAND "git commit"
A Git commit is equivalent to the term "Save"
A commit message is a log message from the user describing the changes

THE COMMAND "git diff filename"
You can see the differences between the older file and the new file. 
New additions are denoted by green-colored text and a + sign at the start of the line. 
Any replacements/removal are denoted by text in red-colored text and a - sign at the start of the line.

THE COMMAND "git log":
Git log command shows the commit history of the repository. 
It shows all the commits on the repository represented by a unique commit ID at the top of each commit. 
It also shows the author, date, and time and the commit message associated with the commits
You also have various options to limit the output of this command. 
The output can be filtered based on the last number of commits, author, commit message, etc. 

THE COMMANDS ls, ls -l, ls -la, ls -l .git/
ls:             display files of the directory
ls -l:          display files of the directory with more details
ls -la:         display files in the directory that start with a dot
ls -l .git/:    display contents of the Repository after it was initialized



EXAMPLE 1 - create directory, create Repository, commit 1 existing file, areas.py in the Repository

mkdir directory2            # create a directory

cd directory2               # navigate to the directory

ls                          # display files of the directory
                            #  no files!

git init                    # create a Repository inside this directory
                            # (Initialized empty Git repository in C:/Users/jimko/directory2/.git/)
                            
ls                          # display files of the directory
                            #  no files!
                            
ls -la                      # display files in the directory that start with a dot
                            # confirm the Repository was created in the directory (it is the .git/) 
                            # total 44
                            # drwxr-xr-x 1 jimko 197609 0 Nov 16 09:57 ./
                            # drwxr-xr-x 1 jimko 197609 0 Nov 16 09:56 ../
                            # drwxr-xr-x 1 jimko 197609 0 Nov 16 09:57 .git/
                          
ls -l .git/                 # display contents of the Repository before adding the areas.py
                            # total 7
                            # -rw-r--r-- 1 jimko 197609  23 Nov 16 09:57 HEAD
                            # -rw-r--r-- 1 jimko 197609 130 Nov 16 09:57 config
                            # -rw-r--r-- 1 jimko 197609  73 Nov 16 09:57 description
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:57 hooks/
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:57 info/
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:57 objects/
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:57 refs/
                            
git status                  # displays status of the Repository
                            # On branch master
                            # No commits yet
                            # nothing to commit (create/copy files and use "git add" to track)
                            # So, we have an empty Repository, no files in there
                            
cp ../areas.py ./areas.py   # copy a file from parent directory to current directory
                            # this file is in the directory but not on the Repository, it is not tracked yet by Git
ls                          # display files of the directory
                            # areas.py
ls -l .git/                 # display contents of the Repository  
                            # exactly same files as above, nothing was added
                            
git status                  # displays status of the Repository
                            # On branch master
                            # No commits yet
                            # Untracked files: (use "git add <file>..." to include in what will be committed)    areas.py
                            # nothing added to commit but untracked files present (use "git add" to track)
                            # So, git understands there is a file in the directory but it is not "tracked" yet!
                               
git add areas.py            # I tell Git to track this file 
                            # I add this file to the staging area 

git status                  # displays status of the Repository
                            # On branch master
                            # No commits yet
                            # Changes to be commited:
                            # (use "git rm --cached <file>..." to unstage)
                            # new file:   areas.py
                            # now the file is inside the Repository but in the staging area so I have to commit it 
                            
git commit                  # opens the nano editor so we can add the Commit Message to our file
                            # [master (root-commit) ed92e57] I am adding areas.py to the Repository of directory2
                            # 1 file changed, 41 insertions(+)
                            # create mode 100644 emails.py
                            # I finally added this file to the Repository
OR git commit -m 'I am adding areas.py to the Repository of directory2'
                            # I do the commit on the command line without an editor

                         
git status                  # displays status of the Repository
                            # On branch master
                            # nothing to commit, working tree clean
                            # the file is in stored in the VCS, no files on working area, no files in staging area
                            


ls                          # I see the contents of the directory, areas.py
ls -l                       # I see the contents of the directory,-rw-r--r-- 1 jimko 197609 270 Nov 16 09:29 areas.py
ls -la                      # I see contents of the directory that start with a dot
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:29 ./
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:24 ../
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:37 .git/
                            # -rw-r--r-- 1 jimko 197609 270 Nov 16 09:29 areas.py

ls -l .git/                 # display contents of the Repository after adding the areas.py
                            # -rw-r--r-- 1 jimko 197609 282 Nov 16 09:34 COMMIT_EDITMSG. THIS IS NEW! is it the areas.py?
                            # -rw-r--r-- 1 jimko 197609  23 Nov 16 09:25 HEAD
                            # -rw-r--r-- 1 jimko 197609 130 Nov 16 09:25 config
                            # -rw-r--r-- 1 jimko 197609  73 Nov 16 09:25 description
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:25 hooks/
                            # -rw-r--r-- 1 jimko 197609 137 Nov 16 09:34 index
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:25 info/
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:34 logs/
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:34 objects/
                            # drwxr-xr-x 1 jimko 197609   0 Nov 16 09:25 refs/

EXAMPLE 2 - Modify a file already in a Repository, stage it and commit it


cd directory2               # navigate to directory
ls -l                       # I see the contents of the directory,-rw-r--r-- 1 jimko 197609 270 Nov 16 09:29 areas.py

git status                  # displays status of the Repository
                            # On branch master
                            # nothing to commit, working tree clean
                            # we will modify the areas.py so this status will change

nano areas.py               # open the areas.py in the nano editor  
                            # modify the areas.py
                            
git status                  # On branch master
                            # Changes not staged for commit:
                            # (use "git add <file>..." to update what will be committed)
                            # (use "git restore <file>..." to discard changes in working directory)
                            # modified:   areas.py
                            # no changes added to commit (use "git add" and/or "git commit -a")
                            # SO: git understands that changes were made to the file and that they are not staged!

git add areas.py            # place the modified file in the staging area

git status                  On branch master
                            Changes to be committed:
                            (use "git restore --staged <file>..." to unstage)
                            modified:   areas.py

git commit -m 'I added a comment'  # commit the staged file to the Repository
                                    # [master 220379b] I added a comment
                                  # 1 file changed, 1 insertion(+)

git status                  On branch master
                            nothing to commit, working tree clean


"""
#%%
"""
1.4.1	First Steps with Git

Let's start by setting some basic configuration. 
A VCS tracks who made which changes, so for this to work, we need to tell Git who we are. 
We can do this by using the Git config command and then setting the values of user.email and user.name to our email 
and our name like this.

We use the dash dash global flag to state that
 we want to set this value for all git repositories that we'd use. 
We could also set different values for different repositories.

GIT BASH APPLICATION:
git config --global user.email "me@example.com"
git config --global user.name "My name"

git init        # create a repository from scratch
git clone       # make a clone of a repository (copy a repository) that already exists somewhere else
                # we will talk about remote repositories later


mkdir checks    # create the directory "checks"
cd checks       # navigate to the directory "checks"
 ~/checks git init        # create a new Repository inside the directory "checks"
Output is:
    Initialized empty Git repository in /home/user/checks/.git/ 
                # we see the directory .git (I see a file folder named "checks", and also a .gitconfig file)
ls -la          # check if the directory .git exists. The ls -la command lists files that start with a dot
Output in video is:
    total 12
    drwxr-xr-x 3 user user 4096 Jan 5 14:18 .
    drwxr-xr-x 29 user user 4096 Jan 5 14:18 ..
    drwxr-xr-x 7 user user 4096 Jan 5 14:18 .git
Output in my machine is:  
total 44
drwxr-xr-x 1 jimko 197609 0 Nov 15 17:45 ./
drwxr-xr-x 1 jimko 197609 0 Nov 15 17:45 ../
drwxr-xr-x 1 jimko 197609 0 Nov 15 17:45 .git/


ls -l .git/     # display contents of the directory ".git"
Output in video is:
    total 32
    drwxr-xr-x 2 user user 4096 Jan 5 14:18 branches
    -rw-r--r-- 1 user user 92 Jan 5 14:18 config
    -rw-r--r-- 1 user user 73 Jan 5 14:18 description
    -rw-r--r-- 1 user user 23 Jan 5 14:18 HEAD
    drwxr-xr-x 2 user user 4096 Jan 5 14:18 books
    drwxr-xr-x 2 user user 4096 Jan 5 14:18 info
    drwxr-xr-x 4 user user 4096 Jan 5 14:18 objects
    drwxr-xr-x 4 user user 4096 Jan 5 14:18 refs

Output in my machine is: 
total 7
-rw-r--r-- 1 jimko 197609  23 Nov 15 17:45 HEAD
-rw-r--r-- 1 jimko 197609 130 Nov 15 17:45 config
-rw-r--r-- 1 jimko 197609  73 Nov 15 17:45 description
drwxr-xr-x 1 jimko 197609   0 Nov 15 17:45 hooks/
drwxr-xr-x 1 jimko 197609   0 Nov 15 17:45 info/
drwxr-xr-x 1 jimko 197609   0 Nov 15 17:45 objects/
drwxr-xr-x 1 jimko 197609   0 Nov 15 17:45 refs/


                # the ".git" directory is a Git directory
                # You can think of it as a database for your Git project that stores the changes and the change history. 
                # it contains files and directories
                # we will not interact with them directly, but through Git commands
                
                # whenever we clone a repository, this Git directory is copied into your computer
                # whenever we create a Repository with git init, a new Git directory is initialized
                # the area outside the Git directory is the working tree
                # the working tree is the current version of your project
                # the working tree is like a workbench where you perform all the modification you want to your file.
                #  This working tree will contain all the files that are currently tracked by Git and any new files that we haven't yet added to the list of track files. 
                # 
                
                
Git directory(.git) and working tree
    The Git directory contains files and directories with which we interact ONLY through git commands
    The git-directory is where the repository resides
    
    Working tree: The work-tree has our source code which we want to be managed by git    

Git directory: contains all the changes and their history
Working tree: contains the current versions of the files

Git makes the distinction between three distinct areas/concepts:
The repository itself, which is stored within the .git directory, as discussed in the previous section
The working tree, which corresponds to the current state of files on your filesystem
The staging area (also called the index), which is the area that you can use to prepare commits / temporarily save your work      

Right now our working tree is empty. 
Let's change that by copying the disk usage, that py file that we saw in an earlier video into our current directory. 

cp ../disk_usage.py   # copy the file "disk_usage.py" into our current directory. 
                      # on my machine:cp ../areas.py ./areas1.py i copied areas.py from previous directory into current directory and gave it a new name too 
                      #(i got an error message with this command cp: missing destination file operand after '../areas.py'

ls -l                 # display contents of the directory
Output in video  is:
    total 4
    -rw-xr-x 1 user user 656 jan 5 14:25 disk_usage.py
Output in my machine is:
    total 1
-rw-r--r-- 1 jimko 197609 270 Nov 15 18:00 areas1.py


                      # We now have file and a working tree but it's currently untracked by Git. 
git add disk_usage.py # To make Git track our file, we'll add it to the project using the git add command
                      # we have added our file to the Staging Area
                      # on my machine git add areas1.py

Staging Area (index)
A file mainted by Git, that contains all of the information
about what files and changes are going to go into your next commit


git status           # use the git status command to get some information about the current working tree and pending changes
Output is:
    On branch master
    No commits yet
    Changes to be commited
    (use "git rm --cached <file>" to unstage)
    new file: disk_usage.py , on my machine it is areas1.py

                    # our change is currently in the staging area

git commit          # when we run this command we tell Git we want to save our changes
                    # this command opens a text editor where we can enter a commit message
                    # nano editor opens
                    # The text that we get tells us that we need to write a commit message and that the change to be committed is the new file that we've added. 
                    # type: Add new disk_usage check save and exit
                    # On Windows, if you use Git Bash the default editor will be Vim. Vim is another text editor, like nano or notepad.

Vim
On Windows, if you use Git Bash the default editor will be Vim. 
Vim is another text editor, like nano or notepad. 
In order to get started Vim there are only a few commands you must remember.
Before making your first commit, try running:
vim
in the terminal.

You start in a mode called “normal mode”. 
You can’t immediately type anything.

In order to get typing press i (stands for insert). This will bring you to “insert mode”, so named because in this mode you can actually type.

When you are done typing press esc. 
This will bring you back to “normal mode”.

In order to save your work you want to type :w 
and press return. 
And in order to exit vim you want to type :q 
and press return. 
Because saving and quitting is a very common action,
there is actually a shortcut :x, which stands for :wq (which just combines :w and :q).

CHANGE FROM VIM TO NANO
git config --global core.editor "nano"
"""

#%%
"""
1.4.2   Tracking Files

any Git project consists of 3 sections
1 git directory contains the history of all files and changes
2 working tree contains the current state of the project, including any changes that we have made
3 staging area contains the changes that have marked to be included in the next commit

 Each time you make a commit, Git records a new snapshot of the state of your project at that moment.
 It's a picture of exactly how all these files looked at a certain moment in time.
 Combined, these snapshots make up the history of your project, and it's information that gets stored in the Git directory. 

When we operate with Git, our files can be either tracked or untracked.
Tracked files are part of the snapshots, while untracked files aren't a part of snapshots yet. 
This is the usual case for new files

Each tracked file can be in one of three main states, 
MODIFIED   
If a file is in the modified state, it means that we've made changes to it that we haven't committed yet. 
STAGED
So, the next step is to stage those changes. 
When we do this, our modified files become stage files. 
In other words, the changes to those files are ready to be committed to the project. 
All files that are staged will be part of the next snapshot we take.
COMMITED
and finally, when a file gets committed, 
the changes made to it are safely stored in a snapshot in the Git directory. 

In other words,
a file tracked by Git, 
will first be modified when we change it in any way. 
Then it becomes staged when we mark those changes for tracking. 
And finally it will get committed when we store those changes in the VCS.

In_Video question:
What do we need to do after modyfying a file tracked by Git?
Answer: we need to stage the file, so that the changes will be included in the next commit

1 cd checks                     # navigate to this directory
2 ~/checks1 (master) ls -l      # display contents of the working tree
Output on my machine:
    total 8
-rw-r--r-- 1 jimko 197609 4428 Nov 15 18:33 find_error.py
3 ~/checks1 (master) git status # display current status of our files
Output on my machine:
    $ git status
    On branch master   # we are on the master branch
    nothing to commit, working tree clean # we will modify our file to change this!
4 ~/checks1 (master) atom find_error.py # open the file and modify it. I added another question mark
5 ~/checks1 (master) git status # 
Output on my machine:
    $ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   find_error.py

no changes added to commit (use "git add" and/or "git commit -a")
6 ~/checks1 (master) git add find_error.py # we will STAGE this change for commit with git add command
7 ~/checks1 (master) git status 
Output on my machine:
    $ git status
    On branch master
    Changes to be committed:
        (use "git restore --staged <file>..." to unstage)
        modified:   find_error.py

When we call git add, 
we're telling Git that we want to add the current changes in that file to the list of changes to be committed. 
This means that our file is currently part of the staging area, and it will be committed once we run 
the next Git command,git commit. 

8 ~/checks1 (master) git commit -m 'I added another question mark'
Output on my machine is:
    [master b43ff7d] I added another question mark
    1 file changed, 1 insertion(+), 1 deletion(-)

So, we've now committed our stage changes. 
This creates a new snapshot in the Git directory. 
The command shows us some stats for the change made.

9 ~/checks1 (master) git status #
Output on my machine is:
    On branch master
    nothing to commit, working tree clean

we have no changes to commit. 
Because the change we made has gone through the full cycle of modified, staged and committed. 

Summary:
So to sum up, we work on modified files in our working tree. 
When they're ready, we staged these files by adding them to the staging area. 
Finally, we commit the changes sitting in our staging area, which takes a snapshot of those files and stores them in the database that lives in the Git directory.
"""
#%%
"""
1.4.3   The Basic Git Workflow

In-Video question
When committing new files or changes with git commit, the user is asked to provide a commit message. 
What will happen if an empty commit message is entered?
Answer: The commit will be aborted

EXAMPLE - create a Repository and add to it the new file "all_checks.py" we just created on the nano editor
mkdir scripts
cd scripts
git init
git config -l
                diff.astextplain.textconv=astextplain
                filter.lfs.clean=git-lfs clean -- %f
                filter.lfs.smudge=git-lfs smudge -- %f
                filter.lfs.process=git-lfs filter-process
                filter.lfs.required=true
                http.sslbackend=openssl
                http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
                core.autocrlf=true
                core.fscache=true
                core.symlinks=false
                pull.rebase=false
                credential.helper=manager-core
                credential.https://dev.azure.com.usehttppath=true
                user.email=foteinirodis@gmail.com
                user.name=FoteiniRodi
                core.editor=nano
                core.repositoryformatversion=0
                core.filemode=false
                core.bare=false
                core.logallrefupdates=true
                core.symlinks=false
                core.ignorecase=true

nano all_checks.py
                #!/usr/bin/env python3
                def main():
                    pass
                main()
chmod +x all_checks.py
git status
                On branch master
                No commits yet
                Untracked files:(use "git add <file>..." to include in what will be committed)
                all_checks.py
                nothing added to commit but untracked files present (use "git add" to track)
git add all_checks.py
                This command will immediately move a new file from untracked to stage status
                And as we'll see later, it will also change a file in the modified state to staged state.
                Git will only commit the changes that have been added to the staging area, untracked files or modified files that weren't staged will be ignored.
                warning: LF will be replaced by CRLF in all_checks.py.
                The file will have its original line endings in your working directory
git status
                On branch master
                No commits yet
                Changes to be committed:
                (use "git rm --cached <file>..." to unstage)
                new file:   all_checks.py

git commit      
                nano editor opens
                I write: Create an empty all_checks.py
                Please enter the commit message for your changes. Lines starting with '#' will be ignored, and an empty message aborts the commit.                
                On branch master
                Initial commit
                Changes to be committed:
                new file:   all_checks.py
CTRL-, ENTER, CTRL-X
                [master (root-commit) 7ad8fb4] Create an empty all_checks.py
                1 file changed, 6 insertions(+)
                create mode 100644 all_checks.py

every time we commit changes, we take another snapshot, which is annotated with a commit message that we can review later.


EXAMPLE - Modify the file "all_checks.py", stage it and commit it to the Repository

nano all_checks.py
                modify this file
                #!/usr/bin/env python3
                import os
                def check_reboot():
                    "Returns True if the computer has a pending reboot "
                    return os.path.exist("/run/reboot-required")
                def main():
                    pass
                main()
CTRL-, ENTER, CTRL-X
git status
                git understands there as a change
                On branch master
                Changes not staged for commit:
                  (use "git add <file>..." to update what will be committed)
                  (use "git restore <file>..." to discard changes in working directory)
                        modified:   all_checks.py                
                no changes added to commit (use "git add" and/or "git commit -a")
git add all_checks.py
                we placed the modified file in the staging area
                
git status
                On branch master
                Changes to be committed:
                  (use "git restore --staged <file>..." to unstage)
                        modified:   all_checks.py
git commit -m 'Add a check_reboot function'
                [master 2fa1b5a] Add a check_reboot function
                1 file changed, 4 insertions(+), 1 deletion(-)

"""
#%%
"""
1.4.4   Anatomy of a Commit Message

git log
the command git log displays commit messages
we can check the history of the commits of our project using the git log command.
example
commit 2fa1b5a6fa88e40da6297dc62cab0dfe5b0f9f9e (HEAD -> master)
Author: FoteiniRodi <foteinirodis@gmail.com>
Date:   Mon Nov 16 10:54:57 2020 +0200

    Add a check_reboot function


what makes a good commit message:
Writing a clear informative commit message is important when you use a VCS, for the future you or other developers
 or IT specialists who might read the commit message later on.
They will really appreciate the contextual information as they try and figure out some of the parts of the code or
 configuration.

Sections of a commit message
1st section:
Short description of what the commit changes are about.
Must be Fifty characters or less

2nd section:
Empty line

3rd section:
This text is intended to provide a detailed explanation of what's going on with the change. 
It can reference bugs or issues that will be fixed with the change. 
It can also include links to more information when relevant. 
The line limits can be annoying but they help in making the commit message be more digestible for the reader.
each line under 72 characters

4th section:
all lines start with the # symbol
Just like in Python, this symbol indicates that these lines are comments and
 won't get included in the commit message. 
Git shows them to us whenever we're writing a commit message as a reminder of what files we are about to commit.


In -Video question
What should your commit message look like?
Answer: a short description of the change(up to 50 chars),
followed by one or more paragraphs that give more details of the change (if needed)
"""
#%%
"""
1.4.5   Reading: Initial Git Cheat Sheet

Check out the following links for more information:

The Linux kernel documentation itself, as well as impassioned opinions from other developers. 

You can check out "Setting your email in Git" and "Keeping your email address private" on the GitHub help site for how to do this.
"""

#%%
"""
1.4.6   Practice Quiz

1.
Question 1
Before changes in new files can be added to the Git directory, what command will tell Git to track our file in the list of changes to be committed?
git add
git add will add a file to the staging area and mark it for tracking.
2.
Question 2
Which command would we use to review the commit history for our project?
git log
git log will give us information about the author of each commit, its timestamp, and each commit message.




"""
