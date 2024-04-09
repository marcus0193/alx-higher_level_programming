#!/usr/bin/python3
"""Defines a locked Class."""


class LockedClass:
    """
    Stops the users from instantiating a new Lockedclass attributes
    for anything except the 'first_name' attribute.
    """

    __slots__ = ["first_name"]
