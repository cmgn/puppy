#!/usr/bin/env python3


def typechecked(valid_types, display_name):
    def typechecked_internal(func):
        def wrapper(arg):
            if type(arg) in valid_types:
                return func(arg)
            raise ValueError(
                "Function '{}' expected the type of the argument given to be "
                "one of {}, but got an argument of type '{}'.".format(
                    display_name,
                    [_type.__name__ for _type in valid_types],
                    type(arg).__name__
                )
            )
        return wrapper
    return typechecked_internal
