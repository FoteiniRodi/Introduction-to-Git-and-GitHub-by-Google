#%%
"""
Introduction to Git and GitHub, by Google

WEEK 2 – Using Git Locally

2.1 Advanced Git interaction
2.1.1	Intro to Module 2: Using Git Locally
2.1.2	Skipping the Staging Area
2.1.3	Getting More Information About Our Changes
2.1.4	Deleting and Renaming Files
2.1.5	Advanced Git Cheat Sheet
2.1.6	Practice Quiz

MY SYNOPSIS

we have 2 ways to commit a change:
1 - do the change in the file, 
    use "git add" to stage the file, 
    then use "git commit" to commit the file to the VCS
2 - do the change in the file, 
    then use "git commit -a" to stage and commit the file at the same time 

COMMAND "commit -a":        stage and commit in 1 step
COMMAND "commit -m -a":     stage and commit in 1 step. Also add the commit message on the command line

(ofcourse with -m flag, we write the commit message on the command line 
without opening the file on a text editor to write the commit message there)

HEAD indicator is like a bookmark that we can use to keep track of where we are.
HEAD indicator accompanies the latest commit
in general HEAD indicator tells us where we are+++
HEAD is used to indicate what the currently checked-out snapshot is.

COMMAND "git show <commit ID>": we choose to see a specific commit

COMMAND "git log":  shows list of commits. AFTER GIT LOG type q TO EXIT

COMMAND "git log -p": shows associated patches, text is longer

COMMAND "git show <commit ID>": shows a specific commit

COMMAND "git log --stat": shows some stats about the changes in the commit

COMMAND "git diff": for modified but unstaged files
So,     "git diff" is used for Modified files that have not benn staged yet and not commited yet
        "git diff" is used for Modified files to display changes before and after 
        similar to the Linux `diff` command, and can show the differences in various commits
displays the differences between old and new file (after a change we made to the file)
by default,it shows only UNSTAGED changes (so I have not used git add yet to place the file in the staging area)
In other words, git diff works on un-staged files, otherwise its output is nothing

COMMAND "git diff -- staged":   for modified and staged files
                                shows changes that are staged but not commited
                                With this command, we can see the actual stage changes before 
                                we call git commit.
                                An alias to --cached, this will show all staged files compared to the named commit

remember: the sequence is, Modify, Stage, Commit

COMMAND "git add": This command adds changes from the working tree to the staging area i.e., 
                    it gathers and prepares files for Git before committing them. 

COMMAND "git add -p": git will show us the change being added and ASKS US if we want to stage it or not.
                      This way we can detect if there's any changes that we don't want to commit. 
                      Allows a user to interactively review patches to add to the current commit
                      
Attention: "git add * ": stages ALL changes we made while on the working tree

COMMAND "git rm <filename>": deletes a file from the Repository
                             Similar to the Linux `rm` command, this deletes, or removes a file

COMMAND "git mv old-name new-name": to rename files in the Repository
                                    we can also use the mv command to move files between directories
                                    Similar to the Linux `mv` command, this moves a file

COMMAND "git status":   view the status of the working tree
                        shows   tracked files
                                untracked files
                                added files
                                modified files
                                deleted files
                                renamed files
                        git status tells us everyhting about our files
            
.gitignore <file>
we place in that file, everything we want our Repository to ignore
ofcourse we stage it and commit the .gitignore <file>, as with all changes
git add .gitignore then git commit -m 'I added a gitignore file'
The gitignore file is a text file that tells Git which files or folders to ignore in a project

"""
#%%
"""
2.1.1	Intro to Module 2: Using Git Locally
 
Over the course of the next videos, we'll go into much more detail about what we can do with Git. 
  
We'll start by learning some handy shortcuts and how we can get more info out of our version control system. 

Then we'll experience the true power of Git by seeing how we can undo some of our changes. 
The ability to revert previous changes is one of the most useful aspects of version control systems. 
Depending on what needs to be undone, there's a bunch of different techniques that we can use in Git. 
We can discard the changes made to a file, fix a commit that was incorrect and even roll back our project 
to an older snapshot. 

Finally, we'll check out yet another important concept, Branches. 
We can use branches to work on an experimental feature without affecting the main code of our project. 
Support separate versions of a program that can't be merged together and much more.
We'll dive into what branches are, when and how to use them and how to deal with merge conflicts. 
"""
#%%
"""
2.1.2	Skipping the Staging Area

According to the Git workflow, we modify the file, stage it and then commit it.
Here we will see how to stage and commit not in 2 steps but in 1 step

Below we see how to stage and commit in one step
WHEN to do stage and commit in one step, 
    -when we already know that the current changes are the ones that we want to commit
    -when making small changes that we know we'll want to commit directly 
    without keeping them in the staging area and having to write long and complex descriptions. 

We can do stage and commit in one step with "git commit -a"
The flag "-a" automatically stages every file that's tracked and modified before doing the commit
"git commit -a" doesn't work on new files because those are untracked.
Instead, git commit -a, is a shortcut to stage any changes to tracked files and commit them in one step.
If the modified file has never been committed to the repo, we'll still need to use git add to track it first
In the below example, we have the file "all_checks.py" in the Repository "scripts"
We will modify it and then stage and commit it in one step.


COMMAND "git commit -a":
This is a shortcut that,
-stages a tracked, modified file     (places it in the staging area)
AND
-commits the file                    (places it in the Repository)
IN ONE STEP

So, we have 2 ways to commit a change
1 - do the change in the file, use git add to stage the file, then use git commit to commit the file to the VCS
2 - do the change in the file, then use git commit -a to stage and commit the file at the same time 


COMMAND "git commit -a -m"
-a indicates we will do stage and commit for the file in one step
    with -a we skip the staging area. 
    that means we can't add any other changes before creating the commit. 
    So we need to be sure that we have already included everything we want to include in that commit.
-m indicates we will add the commit message directly (without opening text editor)
    the -m flag is used for very short commit messages 

HEAD
HEAD indicator accompanies the latest commit (see example)
Git uses the head alias to represent the currently checked out snapshot of your project.
In this case, the current snapshot is the latest commit in the project.
Also, HEAD indicator can accompany a commit in a different branch of the projec
it's generally easy to think of head as a pointer to the current branch

So, HEAD is used to indicate what the currently checked out snapshot is. 
This is how git marks your place in the project. 
HEAD indicator is like a bookmark that we can use to keep track of where we are.

When you run git commands like diff, branch, or status, 
git will use the head bookmark as a basis for whatever operation it's performing. 
We'll see Head used when we learn how to undo things and perform rollbacks.

In_Video question
If we're making a small change and want to skip the staging step, 
which two flags do we need to add to the git commit command? 
Answer: -m and -a
The -m flag allows us to directly add the commit message to the command.
EXAMPLE
cd scripts
nano all_checks.py              # see previous py file in Week_1_4
                                # I change the file all_checks.py, it needs to be staged and commited
                                # I will use the new command git commit -a, to stage and commit in one step
                                # below I added content after def main, and imported sys module
                                #!/usr/bin/env python3
                                import os
                                import sys
                                def check_reboot():
                                    "Returns True if the computer has a pending reboot "
                                    return os.path.exist("/run/reboot-required")
                                def main():
                                    if check_reboot():
                                        print('Pending Reboot.')
                                        sys.exit(1)
                                
                                main()

git commit -a -m "Call check_reboot from main, exit with 1 on error"
                                # Output is:
                                # [master ef21e4e] Call check_reboot from main, exit with 1 on error
                                # 1 file changed, 4 insertions(+), 1 deletion(-)

git log                         # this displays all commit messages 
                                # latest commit appears on the top
                                commit ef21e4efdae10d9c36a7d306432ce5d505fdb25a (HEAD -> master)
                                Author: FoteiniRodi <foteinirodis@gmail.com>
                                Date:   Tue Nov 17 07:50:38 2020 +0200
                                
                                    Call check_reboot from main, exit with 1 on error
                                
                                commit 2fa1b5a6fa88e40da6297dc62cab0dfe5b0f9f9e
                                Author: FoteiniRodi <foteinirodis@gmail.com>
                                Date:   Mon Nov 16 10:54:57 2020 +0200
                                
                                    Add a check_reboot function
                                
                                commit 7ad8fb48b2e0b775ecc0b90684c45328682bfec8
                                Author: FoteiniRodi <foteinirodis@gmail.com>
                                Date:   Mon Nov 16 10:36:15 2020 +0200
                                
                                    Create an empty all_checks.py


ls -l .git/                     # displays contents of the Repository?
                                total 13
                                -rw-r--r-- 1 jimko 197609  50 Nov 17 07:50 COMMIT_EDITMSG
                                -rw-r--r-- 1 jimko 197609  23 Nov 16 10:24 HEAD
                                -rw-r--r-- 1 jimko 197609 130 Nov 16 10:24 config
                                -rw-r--r-- 1 jimko 197609  73 Nov 16 10:24 description
                                drwxr-xr-x 1 jimko 197609   0 Nov 16 10:24 hooks/
                                -rw-r--r-- 1 jimko 197609 145 Nov 17 07:50 index
                                drwxr-xr-x 1 jimko 197609   0 Nov 16 10:24 info/
                                drwxr-xr-x 1 jimko 197609   0 Nov 16 10:38 logs/
                                drwxr-xr-x 1 jimko 197609   0 Nov 17 07:50 objects/
                                drwxr-xr-x 1 jimko 197609   0 Nov 16 10:24 refs/

"""
#%%
"""
2.1.3	Getting More Information About Our Changes

COMMAND "git log"
shows s list of commits
shows a list of commits in the current Git repository
By default it displays: commit message, author, date of the change

COMMAND "git log -p"
shows associated patches, text is longer
we use the -p flag. 
The p comes from patch, because using this flag gives us the patch that was created.
The format is equivalent to the diff-u output that we saw on an earlier video.
It shows added lines with plus sign + and remove lines with minus sign -. 
Because the amount of text is now longer than what fits on your screen, 
    Git automatically uses a paging tool that allows us to scroll using page up, page down, and the arrow keys.
We still have one commit below the other, but now each commit takes up a different amount of space, 
    depending on how many lines were added or removed in that commit.
Using this option, we can quickly see what changes were made to the files in our repository. 
This can be especially useful if we're trying to track down a change that recently broke our tools.

COMMAND "git show <commit ID>"
we choose to see a specific commit

COMMAND "git log --stat"
This will cause git log to show some stats about the changes in the commit, 
like which files were changed and how many lines were added or removed.

In-Video question
If we want to see a specific commit, which command would we use along with the commit ID?
Answer: git show

CHANGES THAT HAVE NOT BEEN COMMITED YET - COMMAND "git diff"
git diff displays the differencies between old and new file (after a change we made to the file)
git diff by default, shows only UNSTAGED changes.
In other words, git diff works on un-staged files, otherwise its output is nothing

Until now, whenever we've made changes to our files, 
we've either added them to the staging area with git add and committed them with git commit, 
or 
committed them directly using git commit -a. 

This works fine, but it means we have to know exactly which changes we've made. 
Sometimes it can take a while until we're ready to commit.  
But imagine you've been working on adding a new complex feature to a script and it requires thorough testing.
Before committing it, you need to make sure that it works correctly.
So while doing this you find bugs in your code that you need to fix. 
It's only natural that by the time you get to the commit step you don't really remember everything you changed. 

To help us keep track, git gives us the git diff command.
(so with git diff I can see what changes I did to my file before even having my file staged)
git diff shows differences of an un-staged file before and after a change.

lets make a change to the script all_checks.py and then try the command "git diff"
We see that the only change is the extra lines that we've added. 
If our change was bigger and included several files, we could pass a file by parameter 
    to see the differences relevant to that specific file instead of all the files at the same time. 

COMMAND "git add -p"
To review changes before adding them, use the -p flag with the git add command.
When we use this flag, git will show us the change being added and ask us if we want to stage it or not.
This way we can detect if there's any changes that we don't want to commit. 

COMMAND "git diff -- staged"
shows changes that are staged but not commited
With this command, we can see the actual stage changes before we call git commit.


EXAMPLE
git log
                    commit ef21e4efdae10d9c36a7d306432ce5d505fdb25a (HEAD -> master)
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Tue Nov 17 07:50:38 2020 +0200
                    
                        Call check_reboot from main, exit with 1 on error
                    
                    commit 2fa1b5a6fa88e40da6297dc62cab0dfe5b0f9f9e
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Mon Nov 16 10:54:57 2020 +0200
                    
                        Add a check_reboot function
                    
                    commit 7ad8fb48b2e0b775ecc0b90684c45328682bfec8
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Mon Nov 16 10:36:15 2020 +0200
                    
                        Create an empty all_checks.py

git log -p          # amount of text is now longer than what fits on your screen, use page up/page down
                    # exit by pressing :q
                    commit ef21e4efdae10d9c36a7d306432ce5d505fdb25a (HEAD -> master)
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Tue Nov 17 07:50:38 2020 +0200
                    
                        Call check_reboot from main, exit with 1 on error
                    
                    diff --git a/all_checks.py b/all_checks.py
                    index 9424b71..0dcda8d 100644
                    --- a/all_checks.py
                    +++ b/all_checks.py
                    @@ -1,9 +1,12 @@
                     #!/usr/bin/env python3
                     import os
                    +import sys
                     def check_reboot():
                         "Returns True if the computer has a pending reboot"
                         return os.path.exist("/run/reboot-required")
                     def main():
                    -    pass
                    +    if check_reboot():
                    +        print('Pending Reboot.')
                    +        sys.exit(1)
                    
                     main()
                    
                    commit 2fa1b5a6fa88e40da6297dc62cab0dfe5b0f9f9e
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Mon Nov 16 10:54:57 2020 +0200
                    
                        Add a check_reboot function
                    
                    diff --git a/all_checks.py b/all_checks.py
                    index c0d03b3..9424b71 100644
                    --- a/all_checks.py
                    +++ b/all_checks.py
                    @@ -1,5 +1,8 @@
                     #!/usr/bin/env python3
                    -
                    +import os
                    +def check_reboot():
                    +    "Returns True if the computer has a pending reboot"
                    +    return os.path.exist("/run/reboot-required")
                     def main():
                         pass
                    
                    
                    commit 7ad8fb48b2e0b775ecc0b90684c45328682bfec8
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Mon Nov 16 10:36:15 2020 +0200
                    
                        Create an empty all_checks.py
                    
                    diff --git a/all_checks.py b/all_checks.py
                    new file mode 100644
                    index 0000000..c0d03b3
                    --- /dev/null
                    +++ b/all_checks.py
                    @@ -0,0 +1,6 @@
                    +#!/usr/bin/env python3
                    +
                    +def main():
                    +    pass
                    +
                    +main()
                    (END)

git show 2fa1b5a6fa88e40da6297dc62cab0dfe5b0f9f9e 
                    # I have chosen to see a specific commit
                    commit 2fa1b5a6fa88e40da6297dc62cab0dfe5b0f9f9e
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Mon Nov 16 10:54:57 2020 +0200
                    
                        Add a check_reboot function
                    
                    diff --git a/all_checks.py b/all_checks.py
                    index c0d03b3..9424b71 100644
                    --- a/all_checks.py
                    +++ b/all_checks.py
                    @@ -1,5 +1,8 @@
                     #!/usr/bin/env python3
                    -
                    +import os
                    +def check_reboot():
                    +    "Returns True if the computer has a pending reboot "
                    +    return os.path.exist("/run/reboot-required")
                     def main():
                         pass

git log --stat
                    commit ef21e4efdae10d9c36a7d306432ce5d505fdb25a (HEAD -> master)
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Tue Nov 17 07:50:38 2020 +0200
                    
                        Call check_reboot from main, exit with 1 on error
                    
                     all_checks.py | 5 ++++-
                     1 file changed, 4 insertions(+), 1 deletion(-)
                    
                    commit 2fa1b5a6fa88e40da6297dc62cab0dfe5b0f9f9e
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Mon Nov 16 10:54:57 2020 +0200
                    
                        Add a check_reboot function
                    
                     all_checks.py | 5 ++++-
                     1 file changed, 4 insertions(+), 1 deletion(-)
                    
                    commit 7ad8fb48b2e0b775ecc0b90684c45328682bfec8
                    Author: FoteiniRodi <foteinirodis@gmail.com>
                    Date:   Mon Nov 16 10:36:15 2020 +0200
                    
                        Create an empty all_checks.py
                    
                     all_checks.py | 6 ++++++
                     1 file changed, 6 insertions(+)

nano all_scripts.py # I changed it by adding print("Everything ok."), sys.exit(0)
                    #!/usr/bin/env python3
                    import os
                    import sys
                    def check_reboot():
                        "Returns True if the computer has a pending reboot"
                        return os.path.exist("/run/reboot-required")
                    def main():
                        if check_reboot():
                            print('Pending Reboot.')
                            sys.exit(1)
                        print("Everything ok.")
                        sys.exit(0)
                    main()

CTRL-O, ENTER, CTRL-X

git diff            # check out what git diff shows us. This works on modified BUT UNSTAGED FILES
                    # this format is equivalent to the diff -u output that we saw in an earlier video
                    # we see the added lines with a + in front of them
                    diff --git a/all_checks.py b/all_checks.py
                    index 0dcda8d..661bbce 100644
                    --- a/all_checks.py
                    +++ b/all_checks.py
                    @@ -8,5 +8,6 @@ def main():
                         if check_reboot():
                             print('Pending Reboot.')
                             sys.exit(1)
                    -
                    +    print("Everything ok.")
                    +    sys.exit(0)
                     main()

git add -p          # gitshows us the change being added and ASKS us if we want to stage it or not
                    # I answered y yes
                    diff --git a/all_checks.py b/all_checks.py
                    index 0dcda8d..661bbce 100644
                    --- a/all_checks.py
                    +++ b/all_checks.py
                    @@ -8,5 +8,6 @@ def main():
                         if check_reboot():
                             print('Pending Reboot.')
                             sys.exit(1)
                    -
                    +    print("Everything ok.")
                    +    sys.exit(0)
                     main()
                    (1/1) Stage this hunk [y,n,q,a,d,e,?]? y

git diff          # now it does not show any differences, because I staged the modified file with git add above
                  # no output shown
                  
git commit -m 'Added a message when everything is ok'
                  # I modified the file, i used git add to stage it and now I finally commit it  
                 [master 8f10e32] Added a message when everything is ok
                 1 file changed, 2 insertions(+), 1 deletion(-)

"""
#%%
"""
2.1.4	Deleting and Renaming Files

COMMAND "git rm <filename>"
deletes a file from the Repository

COMMAND "git mv old-name new-name"
to rename files in the Repository
the mv command exists in Linux, it can be used for renaming and for moving a file
we can use the mv command to move files between directories

COMMAND git status
the output of git status is a super useful tool to help us know what's up with our files. 
It shows us which files have tracked or untracked changes, and 
which files were added, modified, deleted or renamed.
It's important that the output of these commands stays relevant to what we're doing. 
If we have a long list of untracked files, we might lose an important change in the noise.

.gitignore <file>
If there are files that get automatically generated by our scripts, 
or our operating system generates artifacts that we don't want in our repo, 
we'll want to ignore them so that they don't add noise to the output of git status.
To do this, we can use the gitignore file.


EXAMPLE
cd checks
ls -l
        total 9
        -rw-r--r-- 1 jimko 197609 4428 Nov 17 16:59 find-error.py
        -rw-r--r-- 1 jimko 197609   31 Nov 15 18:16 program.py
git rm program.py
        rm 'program.py'
ls -l
        total 8
        -rw-r--r-- 1 jimko 197609 4428 Nov 17 16:59 find-error.py
git status
        On branch master
        Changes to be committed:
          (use "git restore --staged <file>..." to unstage)
                deleted:    program.py
git commit -m 'Deleted un-needed file'
        # the below output states name of deleted file
        # 1 deletion means there was 1 line in the file
        # and aslo we see the commit message we wrote
        [master 1de27b4] Deleted un-needed file
         1 file changed, 1 deletion(-)
         delete mode 100644 program.py

git mv find-error.py find_allerrors.py
        I changed the name of "find-error.py" to "find_allerrors.py"

git status
        On branch master
        Changes to be committed:
          (use "git restore --staged <file>..." to unstage)
                new file:   find_allerrors.py

git commit -m'New name for find-error.py'
        [master 3e6535b] New name for find-error.py
         1 file changed, 118 insertions(+)
         create mode 100644 find_allerrors.py

.gitignore <file>
Inside this file, we'll specify rules to tell git which files to skip for the current repo.
So, here we specify rules that tell Git to IGNORE certain files

For example, if we're working on an OSX computer, we'll probably want to ignore the dot DS store file, 
which is automatically generated by the operating system. 
To do this, we'll create a .gitignore file containing the name of this file.
Remember that the dot prefix in a Unix-like file system indicates that the file or directory 
is hidden and won't show up when you do the normal directory listing. 
That's why we have to use ls-la to see all files.

cd checks
ls -la
            total 56
            drwxr-xr-x 1 jimko 197609    0 Nov 17 17:13 ./
            drwxr-xr-x 1 jimko 197609    0 Nov 16 10:23 ../
            drwxr-xr-x 1 jimko 197609    0 Nov 17 17:15 .git/
            -rw-r--r-- 1 jimko 197609 4428 Nov 17 16:59 find_allerrors.py

echo .DS_STORE > .gitignore
            the file .gitignore takes its input from +++
ls -la
            total 57
            drwxr-xr-x 1 jimko 197609    0 Nov 17 17:25 ./
            drwxr-xr-x 1 jimko 197609    0 Nov 16 10:23 ../
            drwxr-xr-x 1 jimko 197609    0 Nov 17 17:15 .git/
            -rw-r--r-- 1 jimko 197609   10 Nov 17 17:25 .gitignore
            -rw-r--r-- 1 jimko 197609 4428 Nov 17 16:59 find_allerrors.py

git add .gitignore
            # I added the file to the staging area

git commit -m 'I added a .gitignore file, to ignore .DS_STORE files '
            [master a6a26a4] I added a .gitignore file, to ignore .DS_STORE files
             1 file changed, 1 insertion(+)
             create mode 100644 .gitignore
"""
#%%
"""
2.1.5	Advanced Git Cheat Sheet

Command	Explanation & Link
git commit -a	 Stages files automatically
git log -p	     Produces patch text
git show	Shows various objects
git diff	Is similar to the Linux `diff` command, and can show the differences in various commits
git diff --staged	An alias to --cached, this will show all staged files compared to the named commit
git add -p	Allows a user to interactively review patches to add to the current commit
git mv	Similar to the Linux `mv` command, this moves a file
git rm	Similar to the Linux `rm` command, this deletes, or removes a file
There are many useful git cheatsheets online as well. Please take some time to research and study a few, such as this one.

.gitignore files
.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. 
For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. 
Check out more at: https://git-scm.com/docs/gitignore.

A few common examples of file patterns to exclude can be found here.
"""

#%%
"""
2.1.6	Practice Quiz

1.
Question 1
Which of the following commands is NOT an example of a method for comparing or reviewing the changes 
made to a file?

git log -p

git diff --staged

git add -p

git mv
correct. git mv won't give you any information on changes. 
Instead, it is used to move or rename a file or directory in Git.

2.
Question 2
What is the gitignore file?

A file containing a list of commands that Git will ignore.

A file the user is intended to ignore.

A file listing uncommitted changes.

A file containing a list of files or filename patterns for Git to skip for the current repo.
correct.The gitignore file is a text file that tells Git which files or folders to ignore in a project.

3.
Question 3
What kind of file will the command git commit -a not commit?

Tracked files
New files 
correct.  Files that are new and untracked will not be committed before being added.
Old files
Staged files (The git commit -a command will commit all staged files.)

4.
Question 4
What does HEAD represent in Git?

The subject line of a commit message

The top portion of a commit

The currently checked-out snapshot of your project
correct.In all cases, HEAD is used to indicate what the currently checked-out snapshot is.

The first commit of your project

5.
Question 5
If we want to show some stats about the changes in a commit, like which files were changed and how many lines were added or removed, what flag should we add to git log?

--stat
correct. This will cause git log to show some stats about the changes in the commit, like which files were changed and how many lines were added or removed.
--patch

-2

--pretty

"""
