#%%
"""
Introduction to Git and GitHub, by Google

WEEK 2 – Using Git Locally

2.2 Undoing things
    2.2.1 Undoing Changes Before Committing	
    2.2.2 Amending Commits
    2.2.3 Rollbacks
    2.2.4 Identifying a Commit
    2.2.5 Git Revert Cheat Sheet
    2.2.6 Practice Quiz

MY SYNOPSIS

revert=go back=restore to previous state

COMMAND "git checkout <file>:       reverts a modified but unstaged file
COMMAND "git checkout -p <file>:    reverts individual changes on the modified but unstaged file, 
                                    not all file but certain changes on it.
Attention: git checkout <file>, reverts a file
           git checkout <branch>, switches into this branch 
           
COMMAND "git reset <file>":         reverts a file that is modified and staged
                                    git reset is the OPPOSITE of git add
                                    git reset unstages, git add stages  
                                    "git resert" is useful when by mistake, 
                                    we stage changes that we do not want to commit eventually.
COMMAND "git reset -p <file>":      reverts individual changes
                                    use git reset dash p to get git to ask you which specific changes you want to reset

COMMAND "git add * ":              stages ALL changes we made while on the working tree

COMMAND "git commit --amend":       OVERWRITES THE PREVIOUS COMMIT
                                    for local commits not public commits
                                    AVOID AMENDING COMMITS THAT HAVE ALREADY BEEN MADE PUBLIC

COMMAND "git revert a6a26a480dca83a563bdbf895b9a86e99e4f9420"
                                    reverts a specific commit  
                                    git revert will create a new commit to reverse the previous one

COMMAND "git revert HEAD":          reverts latest commit?
                                    creates a new commit that is the inverse of the previous commit
                                    HEAD indicates we want to revert the latest commit
                                    creates a new commit that is the inverse of the previous commit
                                    Just like that, the bad commit is reverted and the error stopped.
                                    git revert will create a new commit, that is the opposite of everything in the given commit.                                   
COMMAND "git revert a6a26a480dca83a563bdbf895b9a86e99e4f9420" 
                                    reverts a commit that is not the most recent one
                                    
linux command touch <file>: creates a new file
e.g touch auto-update.py                
    touch gather-information.sh

COMMAND "git log -1": git log shows list of commits made
                        -1 shows the latest commit
COMMAND "git log -2": lets us see the 2 latest commits made

COMMAND "git show a6a26a480dca83a563bdbf895b9a86e99e4f9420"
            shows a specific commit
Attention command "git show" without a parameter, shows us information about the commit pointed to by the HEAD.
D.
"""
#%%
"""
2.2.1    Undoing Changes Before Committing

One of the most powerful features of a VCS is that it allows us to REVERT CHANGES
revert change, cancel a change, go back to the immediately precedent state
revert=go back=restore to previous state

1 REVERT UN-STAGED CHANGES, git checkout
revert a file that is modified but not staged


COMMAND "git checkout <file>":
changes a modified but unstaged file, back to its earlier committed state
(Note: my Git Bash names this command as "git restore <file>")


we can use "git checkout <file>" to revert changes to modified files before they get staged. 
This command will restore the file to the latest storage snapshot (which can be either committed or staged).
So if you've made additional changes to a file after you've staged it, 
you can restore the file to the earlier stage version.

COMMAND "git checkout -p <file>"
reverts not the whole Modified file, but individual changes on the file
This command also reverts changes not on the whole file, but treats changes individually
If you need to check out individual changes instead of the whole file, 
you can do that using the dash p flag. 
This will ask you change by change if you want to go back to the previous snapshot or not.


2 REVERT STAGED CHANGES, git reset
revert a file that is modified and staged.
If we realize we've added something to the staging area that we didn't actually want to commit, 
we can unstage our changes by using the git reset command.

COMMAND "git reset ":
    this command is the opposite of git add
    git add, adds changes to the staging area
    git reset, removes changes from the staging area
    
"git resert" is useful when by mistake, we stage changes that we do not want to commit eventually.

COMMAND "git reset -p "++


Staging changes that we don't actually intend to commit happens all the time.
Especially if we use a command like git add star, 
where the star is a file glob pattern used in Bash that expands to all files.
COMMAND " git add * "
This command will end up adding any change done in the working tree to the staging area. 
While sometimes that might be what we want, it can also lead to some surprises.


EXAMPLE for git checkout
cd scripts          # navigate to this directory (we have initialized the Repository earlier)    
nano all_checks.py  # remove the function "check_reboot"
                    def check_reboot():
                        "Returns True if the computer has a pending reboot "
                        return os.path.exist("/run/reboot-required")


./all_checks.py    # run the script
                   #  on my machine I see the message
                   bash: ./all_scripts.py: No such file or directory
                   # on the video:
                   NameError: name 'check_reboot()' is not defined
                   we broke the script with the above change
                   
git status         # git status tells us that our file is modified and the changes aren't staged yet.             
                   # also git status tells us
                   to use git add <file> to stage our changes
                   or to use "git restore <file> to discard our changes
                   
                    On branch master
                    Changes not staged for commit:
                      (use "git add <file>..." to update what will be committed)
                      (use "git restore <file>..." to discard changes in working directory)
                            modified:   all_checks.py
                    
                    no changes added to commit (use "git add" and/or "git commit -a")
                 
git checkout all_checks.py 
                    # We reverted the file to its previous state
                    Updated 1 path from the index

git status
                    # now git status tells us that there is nothing to commit
                    apparently, the previous state of the file was "commited"
                    On branch master
                    nothing to commit, working tree clean

./all_checks.py    # run the script
                   #  on my machine I see the message
                   bash: ./all_scripts.py: No such file or directory
                   # on the video:
                   AttributeError: module 'posixpath' has not attribute 'exist'
                   it is a typing error which we will correct

nano all_checks.py  # open the script and delete "exist" and write "exists"

./all_checks.py         # run the script
                       #  on my machine I see the message
                       bash: ./all_scripts.py: No such file or directory
                       # on the video:
                       Everything ok. (This is the output of the script when it works correctly)

git checkout -p all_checks.py
                    # this command reverts CERTAIN CHANGES
                    diff --git a/all_checks.py b/all_checks.py
                    index 661bbce..49f23aa 100644
                    --- a/all_checks.py
                    +++ b/all_checks.py
                    @@ -3,7 +3,7 @@ import os
                     import sys
                     def check_reboot():
                         "Returns True if the computer has a pending reboot "
                    -    return os.path.exist("/run/reboot-required")
                    +    return os.path.exists("/run/reboot-required")
                     def main():
                         if check_reboot():
                             print('Pending Reboot.')

EXAMPLE for git reset
First, we'll pretend we're trying to debug a problem in our script.
we create a temporary file where we save the output of our file
we do not want to stage this temporary file
by mistake, and by using git add *, we eventually stage this temporary file, how can we undo that?


./all_checks.py > output.txt
                                # run the file, re-direct its output to the txt file
git add *   
                                # add all unstaged changes of our working tree using git add star

git status
                                On branch master
                                Changes to be committed:
                                  (use "git restore --staged <file>..." to unstage)
                                        modified:   all_checks.py
                                        new file:   output.txt
git reset HEAD output.txt 
                                   # output.txt is the file we unstage with git reset
                                   # we are using the HEAD alias, because it indicates the current "snapshot"
                                   I see no output hereof this command

git status                      # I see here that the mistakenly staged output.txt is reverted
                                # It is back to its previous state (previous state=untracked file
                                # remember with git add we 1) track a file and 2) stage a file
                                # track a file = have the file monitored by Git for changes
                                On branch master
                                Changes to be committed:
                                  (use "git restore --staged <file>..." to unstage)
                                        modified:   all_checks.py
                                
                                Untracked files:
                                  (use "git add <file>..." to include in what will be committed)
                                        output.txt
"""
#%%
"""
2.2.2    Amending Commits

amend a commit (commit a file I forgot)
amend a commit message

COMMAND "git commit --amend": 
When we run git commit --amend, 
git will take whatever is currently in our staging area and 
run the git commit workflow to overwrite the previous commit.    
So, "git commit --amend" OVERWRITES THE PREVIOUS COMMIT
Attention: use "git commit --amend" for local commits not public commits ( those that have been pushed to a public or shared repository.)
This is because using --amend re-writes the git history removing the previous commit and replacing it with the amended one. 
This can lead to some confusing situations when working with other people and should definitely be avoided. 
AVOID AMENDING COMMITS THAT HAVE ALREADY BEEN MADE PUBLIC

EXAMPLE 

cd scripts
touch auto-update.py
touch gather-information.sh
ls -l
                            # list the files in the directory
                            # not all files are commited so I cannot say I added them to the Repository
                            total 1
                            -rwxr-xr-x 1 jimko 197609 327 Nov 18 11:47 all_checks.py*
                            -rw-r--r-- 1 jimko 197609   0 Nov 19 06:40 auto-update.py
                            -rw-r--r-- 1 jimko 197609   0 Nov 19 06:40 gather-information.sh
                            -rw-r--r-- 1 jimko 197609   0 Nov 19 06:17 output.txt
git add auto-update.py                         
git commit -m 'I am adding two new scripts'   
                            # I made a mistake on my commit message her
                            # I commited only auto-update.py so I did not add two new scripts,
                            my commit message is wrong
                            [master cdb95c0] I am adding two new scripts
                             1 file changed, 0 insertion(+), 0 deletion(-)
                             create mode 100644 auto-update.py
git add gather-information.sh  
                            # first amend the commit 
                            # commit the second file too
                            
git commit --amend 
                            # this open the text editor
                            # we see the commit message and the stats of the commit 
                            I will add a second line to the exisiting commit message:
                            I am adding two new scripts.
                            gather-information.sh will be used to collect information in case of errors
                            auto-update.py will be run daily to update computers automatically.
                            # Please enter the commit message for your changes. Lines starting
                            # with '#' will be ignored, and an empty message aborts the commit.
                            #
                            # Date:      Thu Nov 19 06:42:54 2020 +0200
                            #
                            # On branch master
                            # Changes to be committed:
                            #       new file:   auto-update.py
                            #       new file:   gather-information.sh
                            #
                            # Untracked files:
                              output.txt
CTRL-O, ENTER, CTRL-X
                            now I see
                            [master 755acd7] I am adding two new scripts. gather-information.sh will be used to collect in
                             Date: Thu Nov 19 06:42:54 2020 +0200
                             3 files changed, 1 insertion(+), 1 deletion(-)
                             create mode 100644 auto-update.py
                             create mode 100644 gather-information.sh

We've amended our previous commit to include both files and a better message                            
BUT we can use git commit --amend, to just update the commit message
                            
"""
#%%
"""
2.2.3    Rollbacks

It is good when we correct our work before doing a "commit".
But what happens if we commit changes and then we want to correct our work?

git revert, is one way to perform a ROLLBACK.
rollback: revert, go back, to code that is working correctly

COMMAND "git revert"
creates a new commit that is the inverse of the previous commit
Just like that, the bad commit is reverted and the error stopped.

Git revert doesn't just mean undo. 
Instead, it creates a commit that contains the inverse of all the changes made in the bad commit 
 in order to cancel them out.
 
e.g. if I added a line in a script on my last commit,
this line will be deleted when I use the command git revert

This way you get the effect of having undone the changes, 
but the history of the commits in the project remains consistent leaving a record of exactly what happened.

So git revert will create a new commit, that is the opposite of everything in the given commit. 
We can revert the latest commit by using the HEAD alias that we mentioned before.  
Since we can think of head as a pointer to the snapshot of your current commit, 
when we pass head to the revert command we tell Git to rewind that current commit

the output of git revert is similar to git commit!This is because the git revert creates a commit for us
                         
Since a revert is a normal commit, we can see both the commit and the reverted commit in the log.                         
                         
EXAMPLE

cd scripts
nano all_checks.py      I open the script and add
                        if disk_full():
                        print("Disk Full.")
                        sys.exit(1)
                       
                        #!/usr/bin/env python3
                        import os
                        import sys
                        def check_reboot():
                            """Returns True if the computer has a pending reboot """
                            return os.path.exists("/run/reboot-required")
                        def main():
                            if check_reboot():
                                print('Pending Reboot.')
                                sys.exit(1)
                            if disk_full():
                                print("Disk Full.")
                                sys.exit(1)
                            print("Everything ok.")
                            sys.exit(0)
                        main()

git commit -a -m 'I added call to a function disk_full'
                        # here I stage and commit my change
                        now the modified file is staged and commited,
                        it contains an error though, I did not test it before commiting it!
                        [master 7506bca] I added call to a function disk_full
                        1 file changed, 3 insertions(+)

./all_checks.py
                        I run the file
                        I get the output
                        NameError: disk_full is not defined
                        This script is not working so we will do a ROLLBACK
                         
git revert HEAD
                        with HEAD we indicate we want to revert our latest commit
                        text editor opens
                        we see the commit interface
                        first line: revert (then the commit message of our latest commit)
                        second line: Git has ADDED A LINE IN THE COMMIT MESSAGE!
                        It defines which commit it reverts, indicating it is a ROLLBACK
                        
                        
                        Revert "I added call to a function disk_full"
                        
                        This reverts commit 7506bca86d70aeffa88386b1c50a0beab668920d.
                        
                        # Please enter the commit message for your changes. Lines starting
                        # with '#' will be ignored, and an empty message aborts the commit.
                        #
                        # On branch master
                        # Changes to be committed:
                        #       modified:   all_checks.py
                        #
                        # Untracked files:
                        
                        It is good practice to add an explanation
                        for WHY we did the ROLLBACK
                        Reason for rollback: the disk_full function was not defined

CTRL-O, ENTER, CTRL-X

after all that, we get the output:
                        [master b32707a] Revert "I added call to a function disk_full"
                         1 file changed, 3 deletions(-)
                         # the output of git revert is similar to git commit!
                         This is because the git revert creates a commit for us
                         Since a revert is a normal commit, we can see both the commit and the reverted commit in the log.

git log -p -2
                        git log shows list of commits
                        latest is shown first
                        -p lets us see the patch created by the commit
                        -2 shows us only 2 latest commits

                        commit b32707a160b942c617ad687ac172b5dc6a0fb1d9 (HEAD -> master)
                        Author: FoteiniRodi <foteinirodis@gmail.com>
                        Date:   Thu Nov 19 07:48:30 2020 +0200
                        
                            Revert "I added call to a function disk_full"
                        
                            Reason for rollback: the disk_full function was not defined
                        
                            This reverts commit 7506bca86d70aeffa88386b1c50a0beab668920d.
                        
                        diff --git a/all_checks.py b/all_checks.py
                        index 140e3ef..49f23aa 100644
                        --- a/all_checks.py
                        +++ b/all_checks.py
                        @@ -8,9 +8,6 @@ def main():
                             if check_reboot():
                                 print('Pending Reboot.')
                                 sys.exit(1)
                        -    if disk_full():
                        -        print("Disk Full.")
                        -        sys.exit(1)
                             print("Everything ok.")
                             sys.exit(0)
                         main()
                        
                        commit 7506bca86d70aeffa88386b1c50a0beab668920d
                        Author: FoteiniRodi <foteinirodis@gmail.com>
                        Date:   Thu Nov 19 07:42:39 2020 +0200
                        
                            I added call to a function disk_full
                        
                        diff --git a/all_checks.py b/all_checks.py
                        index 49f23aa..140e3ef 100644
                        --- a/all_checks.py
                        +++ b/all_checks.py
                        @@ -8,6 +8,9 @@ def main():
                             if check_reboot():
                                 print('Pending Reboot.')
                                 sys.exit(1)
                        +    if disk_full():
                        +        print("Disk Full.")
                        +        sys.exit(1)
                             print("Everything ok.")
                             sys.exit(0)
                         main()

"""
#%%
"""
2.2.4    Identifying a Commit

before, we made a mistake in the latest commit
the latest commit is accompanies by the HEAD alias and we can find the commit by using the HEAD alias

but what can we do when the mistake is in a commit we did a long time ago?
we can find and then revert the faulty past commit by using its ID

a commit ID is a long string e.g.
commit 7506bca86d70aeffa88386b1c50a0beab668920d
the sequence after the name commit is called a HASH
HASH is produced by an algorithm
Why Git uses the HASH and not an arithmetic sequence?
HASH used to guarantee the consistency of our repository
Computing the hash keeps data consistent because it's calculated from all the information that makes up a commit.
The commit message, date, author, and the snapshot taken of the working tree. 
The chance of two different commits producing the same hash, commonly referred to as a collision, is extremely small. 
Remember our discussion about fixing commits with the dash dash amend command? 
Each time we amend a commit, the commit ID will change. 
This is why it's important not to use dash dash amend on commits that have been made public.

The data integrity offered by the commit ID means that 
if a bad disk or network link corrupt some data in your repository, or worse, 
if someone intentionally corrupt some data, Git can use the hash to spot that corruption.

How can you use commit IDs to specify a particular commit to work with, like during a rollback?
see example below at git log -2

EXAMPLE

cd checks
git log -1
            git log shows list of commits made
            -1 shows the latest commit
            commit a6a26a480dca83a563bdbf895b9a86e99e4f9420 (HEAD -> master)
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Tue Nov 17 17:28:24 2020 +0200
            
                I added a .gitignore file, to ignore .DS_STORE files
git log -2
            # lets see the 2 latest commits made
            commit a6a26a480dca83a563bdbf895b9a86e99e4f9420 (HEAD -> master)
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Tue Nov 17 17:28:24 2020 +0200
            
                I added a .gitignore file, to ignore .DS_STORE files
            
            commit 3e6535b49317794d84997309b05a8c0d54251e35
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Tue Nov 17 17:15:57 2020 +0200
            
                New name for find-error.py

git show a6a26a480dca83a563bdbf895b9a86e99e4f9420     
            # I choose to see the commit where I changed the name of the file
            commit a6a26a480dca83a563bdbf895b9a86e99e4f9420 (HEAD -> master)
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Tue Nov 17 17:28:24 2020 +0200
            
                I added a .gitignore file, to ignore .DS_STORE files
            
            diff --git a/.gitignore b/.gitignore
            new file mode 100644
            index 0000000..fd5106f
            --- /dev/null
            +++ b/.gitignore
            @@ -0,0 +1 @@
            +.DS_STORE

git revert a6a26a480dca83a563bdbf895b9a86e99e4f9420
            # now I am not using HEAD to revert the latest commit
            I am using the commit ID to revert a specific commit that is not the latest one
            text editor with the commit interface opens
            I will add a reason for the ROLLBACK
            Rollback reason: the previous name was actually better
            when we generate the rollback, Git automatically icludes
            the ID of the commit we are reverting
            commit b6182f460a56bc015d271ade1f84543442635edf (HEAD -> master)
            Author: FoteiniRodi <foteinirodis@gmail.com>
            Date:   Thu Nov 19 08:27:48 2020 +0200
            
                Revert "New name for find-error.py"
            
                Rollback reason: the previous name was actually better
            
                This reverts commit 3e6535b49317794d84997309b05a8c0d54251e35.
            
            diff --git a/find_allerrors.py b/find_allerrors.py
            deleted file mode 100644
            index 53234d9..0000000
            --- a/find_allerrors.py
            +++ /dev/null
            @@ -1,118 +0,0 @@

            
"""
#%%
"""
2.2.5    Git Revert Cheat Sheet

Git Revert Cheat Sheet
git checkout 
    is effectively used to switch branches.

git reset 
    basically resets the repo, throwing away some changes. 
    It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful.

There are some other useful articles online, which discuss more aggressive approaches to resetting the repo.

git commit --amend 
    is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.

git revert 
    makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.

There are a few ways you can rollback commits in Git.

There are some interesting considerations about how git object data is stored, such as the usage of sha-1.

Feel free to read more here:

https://en.wikipedia.org/wiki/SHA-1
https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/
"""
#%%
"""
2.2.6    Practice Quiz

1.
Question 1
Let's say we've made a mistake in our latest commit to a public branch. 
Which of the following commands is the best option for fixing our mistake?

git revert
git commit --amend
git reset
git checkout -- <file>

My Notes:
    the file is commited, so it is modified and staged and commited
    git checkout, reverts a modified but unstaged file which is not the case here
    public branch means we cannot use git commit --amend, this over-writes the previous commit and erases any history, we use this in a local repository
    git reset is used to unstage changes that we eventually do not want to commit
    I think git revert is correct, it will create a new commit it will inverse the mistake in our latest commit and we can see all information too
Answer: Correct
Nice job! git revert will create a new commit to reverse the previous one, and is the best option for undoing commits on public branches.
2.
Question 2
If we want to rollback a commit on a public branch that wasn't the most recent one using the revert command,
 what must we do?

Use the git reset HEAD~2 command instead of revert
Use the revert command repeatedly until we've reached the one we want
use the commit ID at the end of the git revert command CORRECT.
Use the git commit --amend command instead

Answer: Correct
Nice work! The commit ID is a 40-character hash that identifies each commit.
3.
Question 3
What does Git use cryptographic hash keys for?

To secure project backups
To guarantee the consistency of our repository CORRECT
To encrypt passwords
To identify commits

Answer: Correct
Woohoo! Git doesn't really use these hashes for security. Instead, they’re used to guarantee the consistency of our repository.
4.
Question 4
What does the command git commit --amend do?

Start a new branch
Create a copy of the previous commit
Delete the previous commit
Overwrite the previous commit CORRECT

Answer: Correct
Awesome! The command git commit --amend will overwrite the previous commit with what is already in the staging area.
5.
Question 5
How can we easily view the log message 
and diff output the last commit 
if we don't know the commit ID?

git show correct
git identify
git log
git revert

Answer: Correct
Right on! The git show command without an object parameter specified  will default to show us information about the commit pointed to by the HEAD.


"""

