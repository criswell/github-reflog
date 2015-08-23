# Monolithic versus modular

I'm well aware I can make this project using Python modules. I'm also
aware this would probably make working with it easier.

However, one of the current design goal is ease of installation. There is no
installation tool for `git-github-reflog`, and it should be easy to install
the tool by simply copying a single file into your `$PATH` somewhere. If
the project were modular, it would no longer be a trivial installation.

Additionally, there's a finite size this project will grow to. Once we support
all of the Github events, then there will be nothing else to add.

For these reasons, I've opted to have the project be monolithic, e.g., 
`git-github-reflog` will be a single, large script.

I do reserve the right to change this at any point, however :-)

# Consistency in log entries

If you want to add a new event handler, there is really only one, semi-hazy,
rule which you must follow: All log entries should be consistent in their
look and layout.

All entries should follow these basic things:

## All log entries should have a header, and a body where applicable

Log entries will have a header which contains metadata information such
as users involved, date stamps, SHAs for things like commits, references,
etc and so on.

Additionally, some log entries will have additional information which
should be displayed as bodies. These include things like messages,
comments, and titles.

Bodies should be indented using the `pager_message()` method.

## Headers should have some logical consistencies

Take a look at the other event handlers to see how similar events are
handled. Contributors should strive to keep things consistent across
event handlers.

By way of an example compare entries for `PullRequestEvent` and
`PullRequestReviewCommentEvent`:

```
3081385601 PullRequestEvent
User:    criswell <https://api.github.com/users/criswell>
Date:    2015-08-22T17:26:42Z
PR:      #5655 <https://github.com/foo/bar/pull/5655>
Created: 2015-08-22T17:26:42Z   Updated: 2015-08-22T17:26:42Z
SHA:     26b282c367a0867d12aa8927dfddaee7e837be81
Author:  criswell <https://github.com/criswell>
Ref:     issue_5631_fix-foos-that-bars
Action:  opened         State: open

 Issue #5631 - Fix foos that bars

   PR for Issue #5631, where we fix the foos that bar.
```

```
3079908537 PullRequestReviewCommentEvent
User:    criswell <https://api.github.com/users/criswell>
Date:    2015-08-21T18:55:47Z
PR:      #5651 <https://github.com/foo/bar/pull/5651>
Created: 2015-08-21T18:53:03Z   Updated: 2015-08-21T18:55:47Z
SHA:     23d4d6164f68c7025d9f7020754a55fb15aba66b
Author:  criswell <https://github.com/criswell>
Ref:     issue_991_Watch_snaz_frond
URL:     https://github.com/foo/bar/pull/5651#discussion_r37666338
Action:  created            State: open

   Please fix indentation here.
```

We can see that the following pattern in headers is observed:

```
PR:
Created:        Updated:
SHA:
Author:
Ref:
...
Action:         State:
```

To make it easier for humans to scan these log entries, similar patterns
should be followed. If the SHA is *always* in the same general location,
finding it is easier, for example.

