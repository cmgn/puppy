#!/usr/bin/env python3


from functools import reduce, cmp_to_key
from puppy import environment
from puppy import ast


def addition(x):
    return lambda y: x + y


def subtraction(x):
    return lambda y: x - y


def multiplication(x):
    return lambda y: x * y


def _list(x):
    def __list(y):
        return [x, y]
    return __list


def list_literal(x):
    """
    Create a new list from an existing list: for now this is just
    the identity function.
    """
    return x


def concat(x):
    """Concatenate two lists"""
    return lambda y: x + y


def _map(f):
    """Map the function f over each element of the list x"""
    return lambda x: list(map(f, x))


def _range(a):
    """Create a list of numbers in the interval [a, b)"""
    return lambda b: list(map(float, range(int(a), int(b))))


def to(a):
    """Create a list of the numbers in the interval [0, a)"""
    return _range(0)(a)


def fold(f):
    """Transform a list into a single value using the function f"""
    def _fold(x):
        if len(x) > 1:
            return f(_fold(x[1:]))(x[0])
        elif len(x) == 1:
            return x[0  ]
        else:
            raise ValueError("Cannot fold empty list")
    return _fold


def compose(f):
    """Compose a function f and a function g"""
    def _compose(g):
        return lambda *x: f(g(*x))
    return _compose


def flip(f):
    """Flip the arguments a function f takes"""
    def _flip(x):
        return lambda y: f(y)(x)
    return _flip


def negate(x):
    return -x


def odd(x):
    return float(int(x) & 1)


def even(x):
    return float(not odd(x))


def eq(x):
    return lambda y: float(x == y)


def gt(x):
    return lambda y: float(x > y)


def lt(x):
    return lambda y: float(x < y)


def _or(x):
    return lambda y: float(x or y)


def _and(x):
    return lambda y: float(x and y)


def _not(x):
    return float(not x)


def _filter(f):
    """Remove the numbers not satisfying the predicate function f from the list""" 
    return lambda l: [x for x in l if f(x)]


def fst(x):
    return lambda _: x


def snd(_):
    return lambda y: y


def _lambda(x, env):
    """Create a lambda abstraction"""
    if type(x) != ast.Symbol:
        raise ValueError("Lambda requires a symbol as its first argument.")
    def lambda_body(body):
        def apply(y):
            sub_env = environment.Environment(parent=env)
            sub_env[x.value] = y
            return body.evaluate(sub_env)
        return apply
    return lambda_body


def head(x):
    try:
        return x[0]
    except IndexError:
        raise ValueError("Can not perform 'head' function on an empty list.")


def tail(x):
    return x[1:]


def _if(cond):
    def __if(x):
        return lambda y: x if cond else y
    return __if


def length(x):
    return float(len(x))


def null(x):
    return float(len(x) == 0)


def exports():
    return {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "list": _list,
        "range": _range,
        "map": _map,
        "fst": fst,
        "snd": snd,
        "fold": fold,
        "compose": compose,
        "filter": _filter,
        ">": gt,
        "=": eq,
        "<": lt,
        "neg": negate,
        "odd?": odd,
        "even?": even,
        "to": to,
        "flip": flip,
        "concat": concat,
        "pi": 3.1415926535,
        "and": _and,
        "or": _or,
        "not": _not,
        "__list": list_literal,
        "lambda": _lambda,
        "λ": _lambda,
        "if": _if,
        "head": head,
        "tail": tail,
        "length": length,
        "null?": null,
    }
