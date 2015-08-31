# github-reflog

Git's reflog is a wonderful tool for viewing the base transactions in a
git repository. But, when a project is hosted on Github, how does one see
Github's reflog?

Well, you can't. However, using `git-github-reflog` you can get the next
best thing.

This tool will read Github's event log for a given project and display
it in a human readable form.

* Want to track down who deleted or created a branch? This tool can do that.
* Want to see who is forking or following a repo? This tool can do that.
* Want to see when code was commented on and by who? This tool can do that.
* Have someone `--force` pushing and overwriting history? Catch them with this
tool.

You can see a screencast of `git-github-reflog` in action
[here](https://asciinema.org/a/25457).

## Install

`git-github-reflog` requires Python (>=2.7) and
[pip](https://pypi.python.org/pypi/pip), it can be installed with:

```
pip install git-github-reflog

       # -or- for an individual user

pip install --user git-github-reflog
```

Then run the `git-github-reflog` command:

```
usage: git-github-reflog [-h] [--naughty] [--events] [--desc]

optional arguments:
  -h, --help  show this help message and exit
  --naughty   Ignore Github's requested poll-interval (naughty naughty)
  --events    List supported events
  --desc      Display helpful descriptions in the event log
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

Then, set your access token globally like this:

```
$ git config --global github.token <access token>
```

#### Using username and password

Set your username with:

```
$ git config --global github.username <my username>
```

When you run `git-github-reflog`, it will ask for your password. You
can also set your password (so you don't need to enter it again) with:

```
$ git config github.password <my password>
```

However, this is not recommended as it will store your password as plain-text
in your `.git/config` file (or `~/.gitconfig` if set globally).

## Use as a git extension

If `git-github-reflog` is placed in your `$PATH`, then it will work as a git
extension

```
git github-reflog
```

## Caveats

* Github's event log only goes back 90 days, and you are only allowed to
view a total of 300 past events.
* `git-github-reflog` does not support all of the [event
types](https://developer.github.com/v3/activity/events/types/) which Github
uses. If you'd like to help add support for a given type, fork me and write a
handler!
* Github has [rate limits](https://developer.github.com/v3/#rate-limiting) for
their API. You can very easily hit those limits using `git-github-reflog`.
* `git-github-reflog` currently has built in pagination and does not support piping
to external pagers or files. The reason for this is because we want to limit the Github
API calls as much as possible.
* Error handling is currently flaky at best, or nonexistent at worst. If
you'd like to help, fork it and improve it!

## Contributing and FAQ

* [Contributing](CONTRIBUTING.md)
* [FAQ](FAQ.md)

## Supported platforms

It should work on Linux, Mac OS X, and other Unixes.

It may work on Windows.

