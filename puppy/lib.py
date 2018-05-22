#!/usr/bin/env python3


from functools import reduce


def pairs_to_list(p):
    if type(p) == tuple:
        return [p[0]] + pairs_to_list(p[1])
    else:
        return [p]


def list_to_pairs(l):
    result = reduce(lambda x, y: (y, x), reversed(l))
    return result


def addition(x):
    return lambda y: x + y


def subtraction(x):
    return lambda y: x - y


def multiplication(x):
    return lambda y: x * y


def _list(x):
    return lambda y: (x, y)


def concat(x):
    return lambda y: list_to_pairs(pairs_to_list(x) + pairs_to_list(y))


def _map(f):
    def __map(x):
        if type(x) == tuple:
            return f(x[0]), __map(x[1])
        else:
            return f(x)
    return __map


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
    }
