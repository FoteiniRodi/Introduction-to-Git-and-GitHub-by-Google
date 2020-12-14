#%%
"""
Introduction to Git and GitHub, by Google
WEEK 4 - Collaboration

4.3 Managing Projects
    4.3.1 Managing Collaboration
    4.3.2 Tracking Issues
    4.3.3 Continuous Integration
    4.3.4 Additional Tools
    4.3.5 Practice Quiz
    
    
"""
#%%
"""
4.3.1 Managing Collaboration

refactor a part of code that others are not currently working on to avoid conflicts
document well your code, write informative comments

If you're a project maintainer, it's important that you are reply promptly to pull requests and don't let them stagnate
big response time = higher probbability for additional commits
understand completely any changes you accept

ISSUE TRACKER
When it comes to coordinating who does what and when, a common strategy for active software projects is to use an issue tracker.

communication between collaborators
mailing list
IRC channels
now
slack channels
telegram groups
"""
#%%
"""
4.3.2 Tracking Issues

we'll talk about two important tools that can help us collaborate better,
 tracking issues and continuous integration.

issue tracker, bug tracker
helps us coordinate work

An issue tracker tells us the tasks that need to be done, the state they're in and who's working on them
The system also let's us add comments to the issue, these comments can be super helpful. They can give us more details about the problem, explain a way to solve it, or detail how to test if it's been solved. Issue trackers aren't just useful for people actively working on projects. 
They also let users report bugs when they come across them, even if they don't know how to solve the problem. 

bug tracker e.g. Bugzilla for open source projects

GitHub has an issue tracker of its own
see Issues at the page of a repository
When writing in issues description, it's a good idea to include all the information that we have about the problem or missing feature and any ideas on how to solve it.
issues have identification numbers (like pull requests)
if we have a pull request ID=5, there will not be an issue with id = 5!

resolving a pull request can close an issue automatically,
just add e.g. Closes: #4 #4 will be automatically detected by Git
    
  when solving an issue, have it assigned to you  
Assigning issues to collaborators helps us track who is working on what. By assigning the bug to yourself, you can let others know that you're working on it, so they don't need to.     
"""
#%%
"""
4.3.3 Continuous Integration

Continuous Integration (CI) system,
will build and test our code every time there is a change!
This means that it will run whenever there's a new commit in the main branch of our code.
It will also run for any changes that come in through pull requests
In other words, if we have continuous integration configured for our project, we can automatically run our tests using the code in a pull request. This way, we can verify that the test will pass after the new changes get merged back into the tree and that means instead of hoping our collaborators will remember to properly test their code, we can rely on our automated testing system to do it for us. 
Once we have our code automatically built and tested, the next automation step is continuous deployment

Continuous Deployment (or Continuous Delivery), CD
Continuous deployment means the new code is deployed often. The goal is to avoid roll outs with a lot of changes between two versions of a project and instead do incremental updates with only a few changes at a time. This allows errors to be caught and fixed early. Typical configurations include deploying a new version whenever a commit is merged into the main tree or whenever a branch is tagged for release.

whole system is called CI/CD
e.g. Jenkings

GitHub does not offer such a system
Some repository hosting services like GitLab provide their own infrastructure for doing continuous integration. GitHub doesn't offer an integrated solution. Instead, the popular alternative is to use Travis which communicates with GitHub and can access the information from GitHub projects to know which integrations to run. 

When creating a CI/CD
Pipelines
Pipelines specify the steps that need to run to get the result you want.
Artifacts
files that are generated as part of the pipeline

attention
1 make sure the authorized entities for the test servers are not the same entities authorized to deploy on the production servers.
2 always have a plan to recover your access in case your pipeline gets compromised

"""
#%%
"""
4.3.4 Additional Tools
Additional Tools
Check out the following links for more information:

https://arp242.net/diy.html 
https://help.github.com/en/articles/closing-issues-using-keywords
https://help.github.com/en/articles/setting-guidelines-for-repository-contributors 
https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html
https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/
https://docs.travis-ci.com/user/tutorial/
https://docs.travis-ci.com/user/build-stages/
"""
#%%
"""
4.3.5 Practice Quiz

1.
Question 1
How do we reference issues in our commits with automatic links?

By using one of the keywords followed by a hashtag and the issue number. CORRECT
ight on! Keywords such as closes or resolves followed by a hashtag and the issue number will tell Git to autolink to the issue with the provided ID number.
By using an asterisk (*) after the issue number.
By typing the issue number inside braces ({}).
By using a special keyword.

2.
Question 2
What is an artifact in terms of continuous integration/continuous delivery (CI/CD) pipelines?

An old and obsolete piece of code or library.
Any file generated as part of the CI/CD pipeline. CORRECT
Awesome! Artifacts can include compiled code, test results, logs, or any type of file generated as part of the pipeline.
An unintended minor glitch in a computer program
An automated series of tests that run each time there is a new commit or pull request.

3.
Question 3
Which of the following statements are good advice for project maintainers? (Check all that apply)

Coordinate solely via email
Reply promptly to pull-requests CORRECT
Woohoo!  The more time that passes until a pull-request gets reviewed, the more likely it is that there's a new commit that causes a conflict when you try to merge in the change.
Understand any changes you accept CORRECT
Nice job! Not only do we not know whether the original coder is going to be around to maintain those functions, we also want to avoid feature creep and unmanageable code
Use an issue tracker CORRECT

4.
Question 4
Which statement best represents what a Continuous Integration system will do?

Run tests automatically CORRECT
Nice job! A continuous integration system will build and test our code every time there's a change.
Update with incremental rollouts 
Assign issues and track who's doing what
Specify the steps that need to run to get the result you want

5.
Question 5
Which statement best represents what a Continuous Delivery (CD) system will do?

Run tests automatically
Update with incremental rollouts CORRECT
Right on! Continuous Delivery means new code is often deployed with the goal of avoiding rollouts with lots of changes between two versions.
Assign issues and track who's doing what
Specify the steps that need to run to get the result you want




"""
