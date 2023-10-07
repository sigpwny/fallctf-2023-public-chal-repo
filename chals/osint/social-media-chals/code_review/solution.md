# Code Review Solution

In this challenge, we're tasked with finding Pinto Bean's GitHub account, and from there, decoding a hidden flag.

Pinto Bean's GitHub is linked from his LinkedIn About section. Once you find his account, it has just one repository, which is a "dotfile repo" -- a type of repository where Linux and Mac users share their configuration files, aka dotfiles, that make their desktop environments/code editors/etc look pretty and function well. 

Looking at the Git commit history, we can see that the last commit deleted some files. But those files can still be viewed on GitHub! (Keeping deleted files around is a feature, not a bug, since it lets you easily revert deletions that broke something when you're writing code.) We can view the contents of those files, which are named as an SSH private and public key-pair. If someone actually uploaded their SSH private key to GitHub, it would be a security nightmare, since it would let people impersonate them when logging into SSH servers.

Fortunately, these files aren't anyone's actual SSH keys. The public key has a note pointing readers towards the private key, and the private key is a base-64 encoded string. It can be decoded with CyberChef or other software, giving you the flag!

In real life, it's very rare for people to accidentally upload SSH private keys -- I think GitHub has a check that warns you if you upload a file with that format. But other secrets, like API keys and passwords, make their way into code repositories all the time. Hence the flag's warning to keep your secrets off GitHub.
