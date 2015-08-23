# github-reflog

Git's reflog is a wonderful tool for viewing the base transactions in a
git repository. But, when a project is hosted on Github, how does one see
Github's reflog?

Well, you can't. However, using `git-github-reflog` you can get the next
best thing.

This tool will read Github's event log for a given project and display
it in a human readable form.

Want to track down who deleted or created a branch? This tool can do that.

Want to see who is forking or following a repo? This tool can do that.

Want to follow commit status changes, see who did them and why? This tool can
do that.

## Install

Set up Python requirements (can be done in a virtualenv):

```
pip install -r requirements.txt
```

Then run the `git-github-reflog` command:

```
usage: git-github-reflog [-h] [--naughty]

optional arguments:
  -h, --help  show this help message and exit
  --naughty   Ignore Github's requested poll-interval (naughty naughty)
  --events    List supported events
```

Normally `git-github-reflog` will pause between requests for the amount of time
Github requests (usually 60 seconds). If you want to be naughty and ignore
that, then use the `--naughty` option. But don't do that, that'd be
dickish.

## Setting up your git repo

Inside your git repo, you will need to set a few things up in order for
`git-github-reflog` to work. `git-github-reflog` will need to know the
repo owner, the repo name, and your personal authentication information.

### Setting up the repo metadata

Change into your locally cloned repo directory, and add the repo owner
and repo name. The repo owner is the user or organization under which
the repo is published on at Github. The repo name is the name of the
repository on Github.

So, for example, in the following Github project URL:

```
https://github.com/twbs/bootstrap
```

The repo owner is `twbs` and the repo name is `bootstrap`. If I had a local
clone of this repo, I would set it up for `git-github-reflog` thusly:

```
$ cd bootstrap
$ git config github.repouser twbs
$ git config github.reponame bootstrap
```

### Setting up your authentication metadata

There are two ways which `git-github-reflog` can authenticate with Github:
With an authentication token or with a username and password.

#### Using authentication tokens

Go to your [personal access token page](https://github.com/settings/tokens)
and generate a personal access token which `git-github-reflog` can use.

Then, set your access token thusly:

```
$ git config github.token <access token>
```

#### Using username and password

Set your username with:

```
$ git config github.username <my username>
```

When you run `git-github-reflog`, it will ask for your password. You
can also set your password (so you don't need to enter it again) with:

```
$ git config github.password <my password>
```

However, this is not recommended as it will store your password as plain-text
in your `.git/config` file.

## Making pagination work

If you're on a Mac OS X, or Linux box, be sure to export your `$LINES`
environmental variable

```
export LINES
```

## Use as a git extension

If this file is in your PATH, then it will work as a git
extension

```
git github-reflog
```

## Supported platforms

It should work on Linux, Mac OS X, and other Unixes.

It may work on Windows.

