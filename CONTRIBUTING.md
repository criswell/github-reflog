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

