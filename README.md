# pypacman
A python package manager

The `test.pacman` is intended to show the basic functionality of the library.
It'll install `black` (and it's dependents) and `pygame-gui` (and it's dependents).
Then it'll uninstall the `pygame-ce` library because it is overridden and install
`pygame` which overrides `pygame-ce`.

The `version` argument is the library version. May be ignored depending on the `strict`
setting.

The `strict` argument is either `True` or `False` and will determine if that exact
version of the library is installed or if the latest version of the library is installed.

The `overrides` argument is a comma-separated list of libraries to uninstall before
installing the indicated library. No spaces.