#!/usr/bin/env python3


import unittest
from puppy import lex


class TestLexer(unittest.TestCase):
    def test_brackets(self):
        self.assertEqual(lex.to_tokens("(())"), ['(', '(', ')', ')'])
        self.assertEqual(lex.to_tokens("([()])"), ['(', '[', '(', ')', ']', ')'])
        self.assertEqual(lex.to_tokens("(([))"), ['(', '(', '[', ')', ')'])
    
    def test_symbols(self):
        self.assertEqual(lex.to_tokens("foo bar baz b@z f0£ m@p"),
                         ['foo', 'bar', 'baz', 'b@z', 'f0£', 'm@p'])
        self.assertEqual(lex.to_tokens("+ @ $ ! / -"),
                         ['+', '@', '$', '!', '/', '-'])
    
    def test_numbers(self):
        self.assertEqual(lex.to_tokens("1 23 456"), [1.0, 23.0, 456.0])
        self.assertEqual(lex.to_tokens("1 0.5 .3 2."), [1.0, 0.5, 0.3, 2.0])
    
    def test_expressions(self):
        self.assertEqual(lex.to_tokens("(+ 1 (* 2 3))"), 
                         ['(', '+', 1.0, '(', '*', 2.0, 3.0, ')', ')'])
        self.assertEqual(lex.to_tokens("(map (+ 1) [1 2 3 4 5])"), 
                         ['(', 'map', '(', '+', 1.0, ')', '[', 1.0, 2.0, 3.0, 4.0, 5.0, ']', ')'])
