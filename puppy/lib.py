#!/usr/bin/env python3


from functools import reduce
from puppy import environment
from puppy import ast


def addition(x):
    return lambda y: x + y


def subtraction(x):
    return lambda y: x - y


def multiplication(x):
    return lambda y: x * y

def division(x):
    def _division(y):
        try:
            return x / y
        except ZeroDivisionError:
            raise ValueError("cannot divide by 0")
    return _division


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
    return lambda b: list(range(int(a), int(b)))


def to(a):
    """Create a list of the numbers in the interval [0, a)"""
    return _range(0)(a)


def fold(f):
    """Transform a list into a single value using the function f"""
    return lambda x: reduce(lambda a, b: f(a)(b), x)


def compose(f):
    """Compose a function f and a function g"""
    def _compose(g):
        return lambda *x: f(g(*x))
    return _compose


def compose_list(fs):
    return reduce(lambda f, g: lambda *a: f(g(*a)), fs)


def flip(f):
    """Flip the arguments a function f takes"""
    def _flip(x):
        return lambda y: f(y)(x)
    return _flip


def negate(x):
    return -x


def odd(x):
    return int(x) & 1


def even(x):
    return int(not x & 1)


def eq(x):
    return lambda y: int(x == y)


def gt(x):
    return lambda y: int(x > y)


def lt(x):
    return lambda y: int(x < y)


def _or(x):
    return lambda y: int(x or y)


def _and(x):
    return lambda y: int(x and y)


def _not(x):
    return int(not x)


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
            nonlocal env
            if not env.parent:
                env = environment.Environment(parent=env)
            env[x.value] = y
            return body.evaluate(env)
        return apply
    return lambda_body


def head(x):
    try:
        return x[0]
    except IndexError:
        raise ValueError("Can not perform 'head' function on an empty list.")


def tail(x):
    return x[1:]


def init(x):
    return x[:-1]


def last(x):
    return x[-1]


def _if(cond, env):
    def __if(x):
        return lambda y: x if cond else y
    return __if


def length(x):
    return len(x)


def null(x):
    return int(not bool(x))


def uncurry(f):
    return lambda x: f(x[0])(x[1])


def repeat_n(n):
    return lambda x: [x] * n


def _assert(x):
    assert x
    return 1


def exports():
    return {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division,
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
