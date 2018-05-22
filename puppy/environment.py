#!/usr/bin/env python3


from puppy import lib


class Environment(dict):
    def __init__(self, lookup=None, parent=None):
        self.update((lookup or {}).items())
        self.parent = parent
    
    def recursive_lookup(self, value):
        if value in self:
            return self[value]
        elif self.parent:
            return self.parent.recursive_lookup(value)
        raise ValueError(f"Could not find symbol {value}")
