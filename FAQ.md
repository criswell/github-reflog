# FAQ

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

