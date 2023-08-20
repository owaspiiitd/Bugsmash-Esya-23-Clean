# Bugsmash Challenge - GitPython and Directory Creation Bug

## Description of App

1. Users will be allowed to clone a repository from a remote source
1. They can decide where they want to clone the repository to
1. The program will give them a statistic regarding the statistics of the repository (number of commits, number of branches, loc of each language, etc.)
1. List cloned repositories and allow to be deleted

## Exploits
* GitPython's Repo.clone_from() function allows for RCE (Remote Code Execution) if the user is able to control the URL of the repository (Point 1)