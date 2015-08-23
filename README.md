# github-reflog

Git's reflog is a wonderful tool for viewing the base transactions in a
git repository. But, when a project is hosted on Github, how does one see
Github's reflog?

Well, you can't. However, using this tool you can get the next best thing.

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

Then run the `github-reflog` command:

```
usage: github-reflog [-h] [--naughty]

optional arguments:
  -h, --help  show this help message and exit
  --naughty   Ignore Github's requested poll-interval (naughty naughty)
```

Normally `github-reflog` will pause between requests for the amount of time
Github requests (usually 60 seconds). If you want to be naughty and ignore
that, then use the `--naughty` option. But don't do that, that'd be
dickish.

## Making pagination work

If you're on a Mac OS X, or Linux box, be sure to export your `$LINES`
environmental variable

```
export LINES
```

## Use as a git extension

If this file is in your PATH, then it probably will work as a git
extension

```
git github-reflog
```

## Supported platforms

It should work on Linux, Mac OS X, and other Unixes.

It may work on Windows.

