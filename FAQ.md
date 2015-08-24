# FAQ

## How do I install it?

Simply put `git-github-reflog` somewhere in your `$PATH`. I'd recommend
`$HOME/bin`, if you have it. See [here](http://askubuntu.com/a/9849).

## Why isn't the script simply called `github-reflog`?

I mainly wanted to use this script as a git extension. In order for that
to work, the script has to be named `git-github-reflog`.

## Why don't you support all Github events?

There are quite a few
[events](https://developer.github.com/v3/activity/events/types/) which
Github can generate. However, I've only implemented those events which I have
directly encountered. I'd like to eventually handle all the events, but we're
not there yet.

If you'd like to help,

* Submit an issue with a link to a repo which has the event in its log.
* Submit an issue with a copy of the JSON generated for the event.
* Fork the repo, add the handler yourself, and submit a PR.

## Why doesn't the output look more like git's reflog?

Github's events can be pretty complicated. I tried to make `github-reflog`
look more like git's `reflog` output, but it got too messy and hard to follow.

So I opted for something which looks more like git's `log` output.

## Why am I seeing "Unknown" in PushEvents?

This is a weird one. In the `PushEvent` handler, we cycle through the commits
in the `payload` looking for the `SHA` that matches the push's head. This
*should* be the push author. It *usually* works.

However, every once in a while the corresponding commit is not in the
`payload`. When this happens, you see something similar to the following in
your log:

```
3084953546 PushEvent
User:      criswell <https://api.github.com/users/criswell>
Date:      2014-08-24T17:28:14Z
SHA:       39864ac6eac5b78cb1b5917da964af25d7184d76
Author:    Unknown <Unknown>
Ref:       refs/heads/foo-bar

   Unknown
```

I'm not sure how best to handle this, as the commit is very clearly not in the
`payload`. If you have a good idea, why not fork the project and fix it! :-)

