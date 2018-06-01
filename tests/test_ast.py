#!/usr/bin/env python3


import unittest
from puppy import ast


class TestAbstractSyntaxTree(unittest.TestCase):
    def test_numeric_literal(self):
        self.assertEqual(ast.Number(3.0).evaluate(None), 3.0)
        self.assertEqual(ast.Number(5.5).evaluate(None), 5.5)
        self.assertEqual(ast.Number(0.0).evaluate(None), 0.0)
