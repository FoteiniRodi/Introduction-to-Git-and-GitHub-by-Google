#%%
"""
Introduction to Git and GitHub, by Google

WEEK 1 – Introduction to Version Control

1.3 Version Control Systems
1.3.1	What is version control?
1.3.2	Version Control and Automation
1.3.3	What is Git?
1.3.4	Reading: More Information About Git
1.3.5	Installing Git
1.3.6	Installing Git on Windows (Optional)
1.3.7	Reading: Installing Git
1.3.8	Practice Quiz

MY SYNOPSIS
a VCS records the changes we make to our files
A VCS is essentialy a system that stores files, but unlike a server it stores all the different versions of a file that we create as we save the file
There are many VCS's (Subversion, Mercurial) but we will use Git

Commit: a collection of edits/changes which we treat a a single edit/change
Commit Message: why the commit was performed
Repository: stores the files for which changes are recorded/tracked
In any organization that produces software, a VCS is a key part of managing the code
a VCS is not only used for files that contain code, but for any file that we need to monitor (e.g. text files, cofiguration files, data files etc.)
a VCS is not a good option for files with images and videos 
a VCS is useful for:
    -recoding history of changes
    -reverting back to previous versions of files that work, when a problem occurs 
    -for saving time and for automation of tasks
    -collaboration between many people
    -tracking changes we have made, even if I am the only person using it (after weeks I do not remember all details afterall)
    - it is not a back up system, so back up your files somewhere else
The Git VCS:
    -free open source system available for installation on Unix based platforms, Windows and macOS
    -not centralized around a single server
    -every person contributing to a repository has full copy of the repository on their own development machines
How to install Git
    - first check if it is already on our machine with git --version
    - for Windows OS, download Git from gitforwindows.org. PLEASE CHOOSE ATOM AS THE EDITOR
    - I did the download, now I am using Git Bash application (MINGW64) which allows me to practice Linux command on my Windows OS machine :)
"""
#%%
"""
1.3.1	What is version control?

Version Control System (VCS)
a VCS records the changes we make to our files

A VCS:
records -the type of changes we make to our files
         -when the changes were made
         -who made the changes
allows us to revert/undo a change 
facilitates collaboration by allowing to merge changes from lots of different sources

A VCS is essentialy a system that stores files
The difference with a file server (which saves the latest version of a file),
is that the VCS stores all the different versions of a file that we create as we save the file.

There are many VCS's, which work in a similar way, they store all versions of a file, they store type of change, when it was made and by who.

COMMIT 
we make edits to multiple files
then we treat the collection of edits as a SINGLE change, this is commit

A commit must always be accompanied by an explanation! COMMIT MESSAGE
(explanation= why the commit/single change was applied
what was fixed by this change. This helps us understand the history)

In any organization that produces software, a VCS is a key part of managing the code.

REPOSITORY
files are usually organized in Repositories.
A repository can be used by one or more people.

A VCS can be used also for files that do not contain only code, files that need to be monitored for changes.
e.g. a VCS can be used to store configuration files, documentation, data files, text files, or any other content that we may need to track/monitor for changes
VCS is not very useful for images or videos

So by using a VCS and diff command and patch command, we can find differences then make corrections etc.
"""
#%%
"""
1.3.2	Version Control and Automation


can a VCS help, even if you don't need to share your scripts or collaborate on them with others?
yes

example 1
a DNS zone file is a configuration file that specifies the mappings between IP addresses and host names in your network
when we update a DNS zone file we must use good explanatory commit messages
when a problem happens we can "roll back" to the previous version of a file which worked correctly and gain valuable time to fix the problematic files

example 2
DHCP daemon
DHCP:  Dynamic Host Configuration Protocol
daemon: a daemon is a computer program that runs as a background process, rather than being under the direct control of an interactive user.

Dynamic Host Configuration Protocol (DHCP) is a network management protocol 
used to automate the process of configuring devices on IP networks, 
thus allowing them to use network services such as DNS, NTP, and any communication protocol based on UDP or TCP.     

The configuration for a DHCP daemon can be replicated in two or more machines, 
where one acts as a primary server and the other one acts as standby machine.
The standby machines won't do much while the primary is up. 
BUT if the primary goes down for any reason, a standby machine can become primary and start responding to DHCP queries. 
For this to work, the configuration files on all machines need to be identical. 
This is because the DHCP protocol doesn't provide a way for standby machines to get an up-to-date version of the configuration files in the way DNS does. 
To deal with this, we can keep the up-to-date version of the DHCP configuration in a version control system 
and have the machines download the configuration from the VCS. 
This means all the machines will have the exact same files.

example 3
Say you get an urgent alert over the weekend, telling you that your DHCP server isn't responding to any queries. 
You look at the history of the changes and you find that one of the changes added on Friday evening, 
 included a duplicated entry causing the server to misbehave. 
By using a VCS, you can easily roll back the change and have the servers back to health in no time. 

You might come across a second unexpected benefit, when it's time to replace the server with a new one.
By having all the server configuration and a version control system, 
it's much easier to automate the task of deploying a new server.


In_Video question
Why is a version control system useful, even if it's used only by a single person? Check all that apply.

1 Seeing the history of the changes helps us understand what changed and why. CORRECT
One of the main benefits of a VCS is that you can see the history of how files changed and understand what changed at each step and what motivated the change.

2 Tracking code in a VCS ensures that it's bug free. not correct
a version control system doesn't ensure the quality of our code.

3 Tracking changes allows for easy rollbacks when a problem is detected. CORRECT
By having each change tracked in the VCS, it's very easy to go back to previous versions when an issue with a change is discovered.

4 Storing files in a VCS avoids the need for any kind of backups. not correct
While you can rely on the version control to keep track of your changes, you still need to ensure that you have proper backups of the data stored in the VCS itself.

In this course we will use Git,
which is one of the most popular version control systems in use today 
"""
#%%
"""
1.3.3	What is Git?

Git:
    free open source system available for installation on Unix based platforms, Windows and macOS
    it is not centralized around a single server
    it has a de-centralized architecture (This means that every person contributing to a repository has full copy of the repository on their own development machines.)
    Collaborators can "share" and "pull" in changes that others have made
    the repositories are all local to the computer being used to create the files, most operations can be done really fast
    Git can work as a standalone program as a server and as a client
    I can use Git on a single machine without a nrtwork connection
    I can use Git as a server on a machine where I want to host my repository
    I can use Git as a client TO access the repository from another machine
    You can use it for small projects with like one developer or huge projects with thousands of contributors. 
    You can use it to track private work that you can keep to yourself 
    You can use it to share your work with others by hosting a code on public servers like Github, Gitlab or others

In-Video question
What characteristics make Git particularly powerful? Check all that apply.

-It is a distributed VCS which means that each developer has a full cope of the repository. CORRECT
Because each contributor to a Git repo has a full copy of the repository, they can interact with the tracked files without needing a coordinating server. 
In turn, this improves collaboration.

- Repositories can be used by as many developers is needed
Because of the way Git was designed, repositories can be useful for any number of developers, from one to thousands.

the official Git website is called git-scm.com
scm= source control management
we prefer the term VCS version control system, because this includes files that contain e.g. text and not only code


Other VCS programs = Subversion, Mercurial
"""
#%%
"""
1.3.4	Reading: More Information About Git

Check out the following links for more information:

https://git-scm.com/doc
https://www.mercurial-scm.org/
https://subversion.apache.org/
https://en.wikipedia.org/wiki/Version_control
"""
#%%
"""
1.3.5	Installing Git

Check whether we have git already installed:
git --version


On Windows, after downloading and executing the installer,Pay attention to the editor question though. 
You'll probably want to change the editor to one that you feel comfortable with, like Notepad++ or Atom.

ATTENTION
One interesting thing about the Windows installation is that it comes preloaded with an environment called MinGW64. 
This environment lets us operate on Windows with the same commands and tools available on Linux.
So you can practice some Linux command line tools on your Windows machine. 
"""
#%%
"""
1.3.6	Installing Git on Windows (Optional)

visit gitforwindows.org
choose Atom as the editor
"""
#%%
"""
1.3.7	Reading: Installing Git

The first step on the way to using Git is to install it! The directions found in the Git documentation below are pretty thorough and helpful, check them out for the best method of getting Git onto your platform of choice.

Git download page
Git installation instructions for each platform
"""
#%%
"""
1.3.8	Practice Quiz

Question 1
How can a VCS (Version Control System) come in handy when updating your software, even if you’re a solo programmer? Check all that apply.

-Git retains local copies of repositories, resulting in fast operations.
CORRECT.  Git's distributed architecture means each person contributing to a repository retains a full copy of the repository locally.

-If something breaks due to a change, you can fix the problem by reverting to a working version before the change.
CORRECT. With version control, if something goes wrong, we can fix it immediately and figure out what happened later.
Git relies on a centralized server.

Git allows you to review the history of your project.


Question 2
Who is the original creator and main developer of the VCS (Version Control System) tool Git?

Bill Gates
Guido van Rossum
Linus Torvalds
CORRECT. Linus Torvalds developed Git in 2005 to better facilitate the process of developing the Linux kernel with developers across the globe.
James Gosling

Question 3
_____ is a feature of a software management system that records changes to a file or set of files over time so that you can recall specific versions later.

A repository

sys.exit()

Version control
CORRECT. A version control system keeps track of the changes that we make to our files.
IDE

Question 4
A _____ is a collection of edits which has been submitted to the version control system for safe keeping.

IDE

version control system

commit
CORRECT. We call the collection of edits we are making at one time a commit.
repository


Question 5
Within a VCS, project files are organized in centralized locations called _____ where they can be called upon later.

commits

repositories
CORRECT. A repository is a central location in which data is stored and managed.
IDE

yum


"""

