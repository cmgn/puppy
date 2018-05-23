#!/usr/bin/env python3


# most of this is boilerplate at the moment, however I
# plan on using it a lot more later on.


import abc
from puppy import lib


class Value(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def evaluate(self, env):
        raise NotImplementedError()


class Number(Value):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self, env):
        return self.value


class Symbol(Value):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self, env):
        return env.recursive_lookup(self.value)


class Pair(Value):
    def __init__(self, values):
        self.values = values
    
    def evaluate(self, env):
        # if it is callable then it must be a partially
        # applied function
        if callable(self.values[0]):
            return self.values[0](self.values[1].evaluate(env))
        
        value = self.values[0].evaluate(env)
        # special case for syntactic sugar.
        if value is lib.list_to_pairs:
            return value([v.evaluate(env) for v in self.values[1].values])
        elif value is lib._lambda:
            return value(self.values[1], env)
        # hacky, this is the second stage stage of the lambda function and
        # the argument (function body at this point) should not be evaluated 
        # as it will (probably) contain references to the argument name provided 
        # to the lambda, which will not be defined yet
        elif value.__name__ is "lambda_body":
            return value(self.values[1]) 
        else:
            return value(self.values[1].evaluate(env))
