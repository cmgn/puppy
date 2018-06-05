#!/usr/bin/env python


from puppy import lib


class Environment(dict):
    """
    Environment is the class used to hold the current map
    of symbols to values.
    """
    def __init__(self, lookup=None, parent=None):
        self.update((lookup or {}).items())
        self.parent = parent

    def recursive_lookup(self, value):
        """Recursively traverse through environments looking for a symbol"""
        if value in self:
            return self[value]
        elif self.parent:
            return self.parent.recursive_lookup(value)
        raise ValueError(f"Could not find symbol {value}")
