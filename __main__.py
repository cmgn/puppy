#!/usr/bin/env python3


from puppy import lex
from puppy import parse
from puppy import environment
from puppy import lib


def main():
    root_env = environment.Environment(lib.exports())
    expression = input(">>> ")
    while expression != "quit":
        try:
            trees = parse.convert_to_tree(lex.to_tokens(expression))
            for tree in trees.values:
                print(tree.evaluate(root_env))
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(f"Malformed expression: {e}")
            print("This was probably caused by giving a function bad arguments.")
        expression = input(">>> ")


if __name__ == '__main__':
    main()
