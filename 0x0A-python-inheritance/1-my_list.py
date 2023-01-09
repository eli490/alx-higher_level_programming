#!/usr/bin/python3
"""Defines an inherited class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in class."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
