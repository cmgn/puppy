#!/usr/bin/env python3


from puppy import ast

UNCURRIED_FUNCTIONS = (
    "if", "define"
)


def auto_curry(tokens):
    """
    Automatically transform a function application into curried
    function application.

    e.g.
    (+ 1 2) -> ((+ 1) 2)
    (map (+ 1) [1 2 3]) -> ((map (+ 1)) [1 2 3])
    """
    if tokens[0] in UNCURRIED_FUNCTIONS:
        return tokens
    prev = tokens[:2]
    tokens = tokens[2:]
    while tokens:
        prev = [prev, tokens[0]]
        tokens = tokens[1:]
    return prev


def parse(tokens, i=0, closing=")"):
    """
    Convert a list of tokens into list of lists to be interpreted
    by the convert_to_tree function
    """
    parsed = []
    while i < len(tokens) and tokens[i] != closing:
        token = tokens[i]
        if token == "(":
            sub_expression, i = parse(tokens, i + 1)
            parsed.append(sub_expression)
        elif token == "[":
            sub_expression, i = parse(tokens, i + 1, closing="]")
            parsed.append(["__list", sub_expression])
        else:
            parsed.append(token)
        i += 1
    if len(parsed) > 2 and closing != "]":
        parsed = auto_curry(parsed)
    return parsed, i


def convert_to_tree(expression):
    """
    Convert a list of tokens into a tree structure, utilising the parse
    function for formatting.
    """
    def _treeify(expression):
        if type(expression) == str:
            return ast.Symbol(expression)
        elif type(expression) in (float, int):
            return ast.Number(expression)
        elif type(expression) == list and expression and expression[0] == "if":
            try:
                return ast.IfStatement(*[_treeify(expr) for expr in expression[1:]])
            except TypeError:
                raise ValueError("Invalid arguments given to an if statement.")
        elif type(expression) == list and expression and expression[0] == "define":
            return ast.DefineStatement(expression[1], _treeify(expression[-1]))
        elif type(expression) == list:
            return ast.Pair([_treeify(sub_expr) for sub_expr in expression])
        else:
            raise ValueError(f"Parser got bad value {str(expression)}")
    expression_list = parse(expression)[0]  # throw away index returned
    return _treeify(expression_list)
