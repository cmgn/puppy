#!/usr/bin/env python3


from puppy import lex
from puppy import parse
from puppy import environment
from puppy import lib
from sys import setrecursionlimit, argv


def split_tokens(token_list):
    split_expressions = []
    current_expression = []
    height = 0
    for k, v in enumerate(token_list):
        if v == ")":
            height -= 1
        elif v == "(":
            height += 1
        current_expression.append(v)
        if not height:
            split_expressions.append(current_expression)
            current_expression = []
    return split_expressions


def evaluate(expression, env):
    trees = parse.convert_to_tree(expression)
    for tree in trees.values:
        evaluated = tree.evaluate(env)
        if evaluated:
            print(evaluated)


def repl(env):
    expression = input(">>> ")
    while expression != "quit":
        try:
            expressions = split_tokens(lex.to_tokens(expression))
            for expression in expressions:
                evaluate(expression, env)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        expression = input(">>> ")


def eval_file(filename, env):
    with open(filename, "r") as f:
        content = f.read()
    expressions = split_tokens(lex.to_tokens(content))
    for expression in expressions:
        evaluate(expression, env)


def main():
    setrecursionlimit(5000)
    root_env = environment.Environment(lib.exports())
    if len(argv) == 1:
        repl(root_env)
    else:
        for filename in argv[1:]:
          eval_file(filename, root_env)


if __name__ == '__main__':
    main()
