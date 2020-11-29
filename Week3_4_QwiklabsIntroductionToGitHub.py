#%%
"""
Introduction to Git and GitHub, by Google

WEEK 3 - Working with Remotes

3.4 Qwiklabs Assessment: Introduction to Github

Contents
1   CREATE A REMOTE REPOSITORY ON GIT HUB
2   CLONE THE REMOTE REPOSITORY ON MY MACHINE
3   CONFIGURE THE REPOSITORY add username and user email
4   EDIT THE README FILE ON MY LOCAL REPOSITORY AND PUSH IT TO THE REMOTE
5   CREATE A NEW FILE ON MY LOCAL REPOSITORY
6   ON GITHUB, ON THE REMOTE REPOSITORY CREATE AN EMPTY FILE
7   PUSH FILE OF STEP 5, FROM LOCAL TO REMOTE

#%%
1   CREATE A REMOTE REPOSITORY ON GIT HUB
name = directory1
description = qwiklabs week 3
private
initialize the repository with a readme

#%%
2   CLONE THE REMOTE REPOSITORY ON MY MACHINE
copy url of remote on github
go to linux command line (remote machine of the exercise)

git clone URL # copy remote repository, create the local

cd directory1 # navigate to the newly created local repository
ls            # display contents of local
README.md

 
3   CONFIGURE THE REPOSITORY add username and user email

git config --global user.name "Name"
git config --global user.email "user@example.com"

#%%
4   EDIT THE README FILE ON MY LOCAL REPOSITORY AND PUSH IT TO THE REMOTE

nano README.md # open file and add the text
    I am editing the README file. Adding some more details about the project description.
Ctrl-o, Enter key, and Ctrl-x # save file
git status
    The git status command shows the different states of files in your working directory and staging area, 
    like files that are modified but unstaged and files that are staged but not yet committed.
    You can now see that the README.md file shows that it's been modified.
On branch main
Your branch is up-to-date with 'origin/main'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md RED!

no changes added to commit (use "git add" and/or "git commit -a")



git add README.md # add the file to the staging area
    Use the git add command to add content from the working directory into the staging area for the next commit. 
    When the git commit command is run, it looks at this staging area. 
    So you can use git add to craft what you'd like your next commit snapshot to look like. 
    To check the files in staging area use git status.
git status
On branch main
Your branch is up-to-date with 'origin/main'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md RED

no changes added to commit (use "git add" and/or "git commit -a")
student-04-283ce6f0edc7@linux-instance:~/directory1$ ^C
student-04-283ce6f0edc7@linux-instance:~/directory1$ git add README.md
student-04-283ce6f0edc7@linux-instance:~/directory1$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.md GREEN




git commit # A Git commit is like "saving" your work.
    This now opens an editor that asks you to type a commit message. 
    Every commit has an associated commit message. 
    A commit message is a log message from the user describing the changes.
    Enter the commit message of your choice or you can use the following text:
        I am editing the README file.

I am editing the README file.
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch main
# Your branch is up-to-date with 'origin/main'.
#
# Changes to be committed:
#       modified:   README.md
#



Ctrl-o, Enter key, and Ctrl-x # save file with the commit message

git push origin main
    Now, push the committed changes from your local repository to a remote repository on the main branch by using:
Username for 'https://github.com': FoteiniRodi
Password for 'https://FoteiniRodi@github.com':
Counting objects: 3, done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 363 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/FoteiniRodi/directory1.git
   4b04a35..4a906d3  main -> main

        
        
You can check the changes made to the local README.md file on the remote repository on Github. 
You can see the last time when the README.md file was added/updated.
You can also see the commit ID just above the list of files in the repository.
 Click on the Commit ID to get more details related to the commit.

#%%
5   CREATE A NEW FILE ON MY LOCAL REPOSITORY

nano example.py

#!/usr/bin/env python 3
def git_operation():
 print("I am adding example.py file to the remote repository.")
git_opeation()

Ctrl-o, Enter key, and Ctrl-x
git add example.py
git commit # Enter a commit message
Ctrl-o, Enter key, and Ctrl-x

We will push these changes later in the lab.

#%%
6   ON GITHUB, ON THE REMOTE REPOSITORY CREATE AN EMPTY FILE

add file
create new file
name = empty_file
commit new file

#%%
7   PUSH FILE OF STEP 5, FROM LOCAL TO REMOTE

git push origin main # it fails

To https://github.com/FoteiniRodi/directory1.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/FoteiniRodi/directory1.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.


git pull origin main
    This opens an editor that asks you to enter a commit message for the merge operation 
    (remote repository to local repository).
    You can simply accept the default message or type your own message.
Ctrl-o, Enter key, and Ctrl-x

git push origin main # it succeeds

Counting objects: 5, done.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 773 bytes | 0 bytes/s, done.
Total 5 (delta 0), reused 0 (delta 0)
To https://github.com/FoteiniRodi/directory1.git
   c561a02..5e1b273  main -> main

git log

commit 5e1b273ade946d31cbac268f310c65067c3150d1
Merge: d815596 c561a02
Author: foteinirodis@gmail.com <FoteiniRodi>
Date:   Sun Nov 29 07:27:56 2020 +0000

    Merge branch 'main' of https://github.com/FoteiniRodi/directory1 into main
    I pulled updates from remote to my local

commit c561a02d9bb9ff74c8f28a09002876b0fb152b49
Author: FoteiniRodi <60667452+FoteiniRodi@users.noreply.github.com>
Date:   Sun Nov 29 09:26:46 2020 +0200

    Create empty_file

commit d8155964776a9a27a4b9dde3e095507f1e975901
Author: foteinirodis@gmail.com <FoteiniRodi>
Date:   Sun Nov 29 07:25:22 2020 +0000

    created the file add example.py on my local

commit 4a906d39f112e6aebddbf061bff7883eb1c4771d
Author: foteinirodis@gmail.com <FoteiniRodi>
Date:   Sun Nov 29 07:19:37 2020 +0000

    I am editing the README file.

commit 4b04a3536474ae1f810b062785d5a4be2633af6b
Author: FoteiniRodi <60667452+FoteiniRodi@users.noreply.github.com>
Date:   Sun Nov 29 09:11:46 2020 +0200
