#%%
"""
Introduction to Git and GitHub, by Google

WEEK 4 - Collaboration

4.2 Code Reviews
    4.2.1 What are code reviews?
    4.2.2 The Code Review Workflow
    4.2.3 How to Use Code Reviews in GitHub
    4.2.4 More Information on Code Reviews
    4.2.5 Practice Quiz
    
MY SYNOPSIS

"""
#%%
"""
4.2.1 What are code reviews?


Doing a code review means going through someone else's code, 
documentation or configuration and checking that it all makes sense and follows the expected patterns. 

high quality code
catch mistakes of others
learn from others
collaborate remotely
"""
#%%
"""
4.2.2 The Code Review Workflow

Now, we'll check out a typical code review using a reviewing tool

finish our work
send it to the reviewer
reviewer sends us back comments with what must be fixed
we correct our mistakes on the code and on our reply to the reviewer
mark the comments from the reviewer as resolved
we can ask the reviewer for more information on how to fix mistakes
once all comments from the reviewer are resolved, our changes are approved and we can merge them

Types of comments from reviewer
typing mistakes
major problems with our code
style of the code (see style guide for coding, eg PEP8 for Python)
always ask for a style guide for your code

Code Reviewing systems
e.g. a maintaner must approve your code before you submit it
e.g. if other contributors vote favorably with +1's, you can submit it without asking the maintainner
"""
#%%
"""
4.2.3 How to Use Code Reviews in GitHu

how does the code reviewing process work specifically on GitHub?

You might remember that git commit dash dash amend modifies commits. 
So it's not safe to do with commits that have been pushed to the repo. 
Using amend is pretty much the same as creating a new commit, and then using an interactive rebase to fix up a change

git commit --amend is equivalent to git rebase -i (interactive rebase)

+++
"""
#%%
"""
4.2.4 More Information on Code Reviews
Check out the following links for more information:

http://google.github.io/styleguide/
https://help.github.com/en/articles/about-pull-request-reviews
https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31
https://smartbear.com/learn/code-review/what-is-code-review/
"""
#%%
"""
4.2.5 Practice Quiz

1.
Question 1
When should we respond to comments from collaborators and reviewers?

When their comments address software-breaking bugs
No need, just resolve the concerns and be done with it
Always CORRECT
Excellent! It is good manners and proper conduct to respond, even when it's simply an acknowledgement.
Only when a code correction is necessary

2.
Question 2
What is a nit?

A trivial comment or suggestion CORRECT
Good work! In git jargon (and elsewhere in the tech world), a nit is a minor “nitpick” about a piece of code.
A couple lines of code
A repository that is no longer maintained
An orphaned branch

3.
Question 3
Select common code issues that might be addressed in a code review. (Check all that apply)

Using unclear namesCORRECT
Following PEP8 guidelines
Forgetting to handle a specific conditionCORRECT
Forgetting to add testsCORRECT

4.
Question 4
If we've pushed a new version since we've made a recent change, what might our comment be flagged as?

Accepted
Resolved
Outdated correct
Nice job! If we push a new version after making a change, old comments are marked with the "Outdated" flag.
Merged not CORRECT
Not quite. You can comment on a merged commit, but you can't flag comments as merged.
5.
Question 5
What are the goals of code review? (Check all that apply)

Make sure that the contents are easy to understand
Ensure consistent style
Build perfect code
Ensure we don't forget any important cases

"""
