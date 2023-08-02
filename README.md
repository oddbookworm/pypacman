# pypacman
A python package manager

The `test.pacman` is intended to show the basic functionality of the library.
It'll install `black` (and it's dependents) and `pygame-gui` (and it's dependents).
Then it'll uninstall the `pygame-ce` library because it is overridden and install
`pygame` which overrides `pygame-ce`.