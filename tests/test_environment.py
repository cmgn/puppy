#!/usr/bin/env python3


import unittest
from puppy import environment


class TestEnvironment(unittest.TestCase):
    def test_basic_lookup(self):
        env = environment.Environment(lookup={"a": 3})
        self.assertEquals(env.recursive_lookup("a"), 3)
        self.assertRaises(ValueError, env.recursive_lookup, "b")
    
    def test_recursive_lookup(self):
        env = environment.Environment(lookup={"a": 3})
        sub_env = environment.Environment(lookup={"b": 4}, parent=env)
        self.assertEqual(sub_env.recursive_lookup("b"), 4)
        self.assertEqual(sub_env.recursive_lookup("a"), 3)
        self.assertRaises(ValueError, sub_env.recursive_lookup, "c")

    def test_modifying_environment(self):
        env = environment.Environment(lookup={"a": 3})
        env["b"] = 4
        self.assertEqual(env.recursive_lookup("b"), 4)
        self.assertEqual(env.recursive_lookup("a"), 3)
        del env["b"]
        self.assertRaises(ValueError, env.recursive_lookup, "b")