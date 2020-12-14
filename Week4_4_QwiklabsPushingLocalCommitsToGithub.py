#%%
"""
Introduction to Git and GitHub, by Google

WEEK 4 - Collaboration

4.4 Qwiklabs Assessment: Pushing Local Commits to Github

student-03-0d05814a1900@linux-instance:~$ git clone https://github.com/[git-username]/it-cert-automation-practice.git
Cloning into 'it-cert-automation-practice'...
fatal: unable to access 'https://github.com/[git-username]/it-cert-automation-practice.git/': The requested URL returned error: 400
student-03-0d05814a1900@linux-instance:~$ git clone https://github.com/FoteiniRodi/it-cert-automation-practice.git
Cloning into 'it-cert-automation-practice'...
remote: Enumerating objects: 25, done.
remote: Total 25 (delta 0), reused 0 (delta 0), pack-reused 25
Unpacking objects: 100% (25/25), done.
student-03-0d05814a1900@linux-instance:~$ cd ~/it-cert-automation-practice
student-03-0d05814a1900@linux-instance:~/it-cert-automation-practice$ git remote -v
origin  https://github.com/FoteiniRodi/it-cert-automation-practice.git (fetch)
origin  https://github.com/FoteiniRodi/it-cert-automation-practice.git (push)
student-03-0d05814a1900@linux-instance:~/it-cert-automation-practice$ git remote add upstream https://github.com/[git-username]/it-cert-automation-practice.git
student-03-0d05814a1900@linux-instance:~/it-cert-automation-practice$ git remote -v
origin  https://github.com/FoteiniRodi/it-cert-automation-practice.git (fetch)
origin  https://github.com/FoteiniRodi/it-cert-automation-practice.git (push)
upstream        https://github.com/[git-username]/it-cert-automation-practice.git (fetch)
upstream        https://github.com/[git-username]/it-cert-automation-practice.git (push)
student-03-0d05814a1900@linux-instance:~/it-cert-automation-practice$


cat validations.py
#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True


"""
