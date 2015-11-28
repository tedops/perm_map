########
perm_map
########

Purpose
=======

Years ago, I had an experience with JGit where it didn't correctly preserve the committed permissions of a cloned repository.

Having had to use JGit again, I wanted to test that a JGit-cloned repository had the same permissions as its Git-cloned version.

Thanks to this script, I was able to verify that the repo perms matched for both JGit and Git.

Usage
=====

::

    $ python3 [jgit-dir] [git-dir]

Assumes that the two cloned directories exist - one with JGit, the other with Git.

Also assumes Python 3.
