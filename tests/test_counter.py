#!/usr/bin/env python3

import unittest
from word_counter import counter


class TestCounter(unittest.TestCase):

    def test_get_word_counts_empty(self):

        text = ""

        # call method under test
        actual = counter.get_word_counts(text)

        self.assertEqual(actual, [])

    def test_get_word_counts(self):

        text = "foo bar baz foo bar bar baz bar"

        # call method under test
        actual = counter.get_word_counts(text)

        self.assertEqual(actual, [('bar', 4), ('foo', 2), ('baz', 2)])

