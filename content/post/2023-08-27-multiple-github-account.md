---
title: "💻 Managing multiple Github accounts on the same computer"
url: /2023/08/27/multiple-github-account.html
date: 2023-08-27
tags:
  - github
weight: -20230827
---

## Introduction

It is common that one would have multiple [Github](https://www.github.com) accounts, such as one for personal use and one for work. Managing Github repositories requires a developer to set up SSH keys on his/her computer. However, this becomes non-trivial when one has to work with multiple accounts representing different identities. This blog post describes how one can easily manage multiple Github repositories from different accounts on the same computer.

## Scenario

Let's assume that I have a two Github accounts, one is `albert-personal` and one is `albert-work`. I use the former to work on my personal projects, and use the latter when working on repositories from my work. Let's also assume that we have two repositories, one is `personal-project` and another is `work-project`, which are under the two accounts mentioned above respectively.

Also when accessing these two accounts, I need to use different SSH keys. Let's say I have the following keys in my `.ssh` folder:

```bash
albert-personal       # private key for personal account
albert-personal.pub   # public key for personal account
albert-work           # private key for work account
albert-work.pub       # private key for work account
```

Our goal is to set up the repositories to use the corresponding SSH key when pushing and pulling from Github.

## Solution

We want to set up the local repository to use a certain SSH key. To do so, we first create a new **config file** under the `.ssh` folder.

Firstly, we create a file `~/.ssh/config-personal` with the following content:

```bash
Host github.com
    HostName github.com
    Port 22
    User git
    IdentifyFile ~/.ssh/albert-personal
```

and also a file `~/.ssh/config-work` with the following content

```bash
Host github.com
    HostName github.com
    Port 22
    User git
    IdentifyFile ~/.ssh/albert-work
```

These configuration files basically tells the `ssh` program to use a certain SSH key when accessing a certain domain (github.com in this case).

Next we need to configure each local repository to use the corresponding SSH configuration file when pushing or pulling from Github. Every Git repository has a `.git` folder, in which there is a file named `config` that stores some configurations of the repository. It looks something like this:

```bash
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:username/repo-name.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

We can add a new line into this config file to ask git to use a certain SSH configuration file. This is done by adding the following line under the `[core]` section in `personal-project/.git/config`:

```bash
sshCommand = ssh -F ~/.ssh/config-personal
```

and in `work-project/.git/config`:

```bash
sshCommand = ssh -F ~/.ssh/config-work
```

Finally, make sure that you have added the SSH public keys to the corresponding Github account.
