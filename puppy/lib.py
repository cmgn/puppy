#!/usr/bin/env python3

import math
from functools import reduce
from types import FunctionType
from puppy import environment
from puppy import ast
from puppy import semantics


@semantics.typechecked([int, float], "+")
def addition(x):
    @semantics.typechecked([int, float], "+")
    def _addition(y):
        return x + y
    return _addition


@semantics.typechecked([int, float], "-")
def subtraction(x):
    @semantics.typechecked([int, float], "-")
    def _subtraction(y):
        return x - y
    return _subtraction


@semantics.typechecked([int, float], "*")
def multiplication(x):
    @semantics.typechecked([int, float], "*")
    def _multiplication(y):
        return x * y
    return _multiplication


@semantics.typechecked([int, float], "/")
def division(x):
    @semantics.typechecked([int, float], "/")
    def _division(y):
        try:
            return x / y
        except ZeroDivisionError:
            raise ValueError("cannot divide by 0")
    return _division


@semantics.typechecked([int, float], "sqrt")
def sqrt(x):
    return math.sqrt(x)


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


@semantics.typechecked([list], "concat")
def concat(x):
    """Concatenate two lists"""
    return lambda y: x + y


@semantics.typechecked([FunctionType], "map")
def _map(f):
    """Map the function f over each element of the list x"""
    @semantics.typechecked([list], "map")
    def __map(x):
        return list(map(f, x))
    return __map


@semantics.typechecked([int, float], "range")
def _range(a):
    """Create a list of numbers in the interval [a, b)"""
    @semantics.typechecked([int, float], "range")
    def __range(b):
        return list(range(int(a), int(b)))
    return __range


@semantics.typechecked([int, float], "to")
def to(a):
    """Create a list of the numbers in the interval [0, a)"""
    return _range(0)(a)


@semantics.typechecked([FunctionType], "fold")
def fold(f):
    """Transform a list into a single value using the function f"""
    @semantics.typechecked([list], "fold")
    def _fold(x):
        return reduce(lambda a, b: f(a)(b), x)
    return _fold


@semantics.typechecked([FunctionType], "compose")
def compose(f):
    """Compose a function f and a function g"""
    @semantics.typechecked([FunctionType], "compose")
    def _compose(g):
        return lambda *x: f(g(*x))
    return _compose


# TODO: find a better way of dealing with situations like this,
# where the function depends on the items within the list being of
# a certain type
@semantics.typechecked([list], "compose")
def compose_list(fs):
    return reduce(lambda f, g: lambda *a: f(g(*a)), fs)


@semantics.typechecked([FunctionType], "flip")
def flip(f):
    """Flip the arguments a function f takes"""
    def _flip(x):
        return lambda y: f(y)(x)
    return _flip


@semantics.typechecked([float, int], "negate")
def negate(x):
    return -x


@semantics.typechecked([float, int], "odd?")
def odd(x):
    return int(x) & 1


@semantics.typechecked([float, int], "even?")
def even(x):
    return int(not x & 1)


@semantics.typechecked([float, int, list], "eq?")
def eq(x):
    @semantics.typechecked([type(x)], f"eq? ({type(x).__name__})")
    def _eq(y):
        return int(x == y)
    return _eq


@semantics.typechecked([float, int], ">")
def gt(x):
    @semantics.typechecked([float, int], ">")
    def _gt(y):
        return int(x > y)
    return _gt


@semantics.typechecked([float, int], "<")
def lt(x):
    @semantics.typechecked([float, int], "<")
    def _lt(y):
        return int(x < y)
    return _lt


@semantics.typechecked([float, int], "or")
def _or(x):
    @semantics.typechecked([float, int], "or")
    def __or(y):
        return int(x or y)
    return __or


@semantics.typechecked([float, int], "and")
def _and(x):
    @semantics.typechecked([float, int], "and")
    def __and(y):
        return int(x and y)
    return __and


@semantics.typechecked([int, float], "not")
def _not(x):
    return int(not x)


@semantics.typechecked([FunctionType], "filter")
def _filter(f):
    """Remove the numbers not satisfying the predicate function f from the list""" 
    @semantics.typechecked([list], "filter")
    def __filter(xs):
        return [x for x in xs if f(x)]
    return _filter


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
            nonlocal env
            if not env.parent:
                env = environment.Environment(parent=env)
            env[x.value] = y
            return body.evaluate(env)
        return apply
    return lambda_body


@semantics.typechecked([list], "head")
def head(x):
    try:
        return x[0]
    except IndexError:
        raise ValueError("Can not perform 'head' function on an empty list.")


@semantics.typechecked([list], "tail")
def tail(x):
    return x[1:]


@semantics.typechecked([list], "init")
def init(x):
    return x[:-1]


@semantics.typechecked([list], "last")
def last(x):
    return x[-1]


@semantics.typechecked([list], "length")
def length(x):
    return len(x)


@semantics.typechecked([list, int, float], "null?")
def null(x):
    return int(not bool(x))


@semantics.typechecked([FunctionType], "uncurry")
def uncurry(f):
    return lambda x: f(x[0])(x[1])


@semantics.typechecked([int], "repeat")
def repeat_n(n):
    return lambda x: [x] * n


@semantics.typechecked([int, list, float], "assert")
def _assert(x):
    assert x
    return 1


def exports():
    return {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division,
        "sqrt": sqrt,
        "list": _list,
        "range": _range,
        "map": _map,
        "fst": fst,
        "snd": snd,
        "fold": fold,
        "compose": compose,
        "compose-list": compose_list,
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
        "head": head,
        "tail": tail,
        "last": last,
        "init": init,
        "length": length,
        "null?": null,
        "assert": _assert,
        "uncurry": uncurry,
        "repeat": repeat_n,
    }
