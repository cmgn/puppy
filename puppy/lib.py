#!/usr/bin/env python3


from functools import reduce, cmp_to_key
from puppy import environment
from puppy import ast


def pairs_to_list(p):
    res = []
    while type(p) == tuple:
        res.append(p[0])
        p = p[1]
    res.append(p)
    return res


def list_to_pairs(l):
    return reduce(lambda x, y: (y, x), reversed(l))


def addition(x):
    return lambda y: x + y


def subtraction(x):
    return lambda y: x - y


def multiplication(x):
    return lambda y: x * y


def _list(x):
    return lambda y: (x, y)


def concat(x):
    def _concat(y):
        if type(x) == tuple and type(y) == tuple:
            return list_to_pairs(pairs_to_list(x) + pairs_to_list(y))
        elif type(x) == tuple:
            return (list_to_pairs(x), y)
        elif type(y) == tuple:
            return (x, list_to_pairs(y))
        else:
            return (x, y)
    return _concat


def _map(f):
    return lambda x: list_to_pairs([f(x_) for x_ in pairs_to_list(x)])


def _range(a):
    return lambda b: list_to_pairs(list(map(float, range(int(a), int(b)))))


def to(a):
    return _range(0)(a)


def fold(f):
    def _fold(x):
        if type(x) == tuple:
            return f(_fold(x[1]))(x[0])
        else:
            return x
    return _fold


def compose(f):
    def _compose(g):
        return lambda *x: f(g(*x))
    return _compose


def flip(f):
    def _flip(x):
        return lambda y: f(y)(x)
    return _flip


def negate(x):
    return -x


def odd(x):
    return x & 1


def even(x):
    return not odd(x)


def eq(x):
    return lambda y: float(x == y)


def gt(x):
    return lambda y: float(x > y)


def lt(x):
    return lambda y: float(x < y)


def _or(x):
    return lambda y: x or y


def _and(x):
    return lambda y: x and y


def _not(x):
    return not x


def _filter(f):
        return lambda l: list_to_pairs([x for x in pairs_to_list(l) if f(x)])


def fst(x):
    return lambda _: x


def snd(_):
    return lambda y: y


def _lambda(x, env):
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
    return x[0]


def tail(x):
    return x[1]


def _if(cond):
    def __if(x):
        return lambda y: x if cond else y
    return __if


def define(x, env):
    def _define(y):
        env[x.value] = y
    return _define


def length(x):
    return float(len(pairs_to_list(x)))


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
        "odd": odd,
        "even": even,
        "to": to,
        "flip": flip,
        "concat": concat,
        "pi": 3.1415926535,
        "and": _and,
        "or": _or,
        "not": _not,
        "__list": list_to_pairs,
        "lambda": _lambda,
        "λ": _lambda,
        "if": _if,
        "head": head,
        "tail": tail,
        "length": length,
    }
