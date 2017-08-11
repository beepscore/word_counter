#!/usr/bin/env python3

import unittest
from word_counter import counter


class TestCounter(unittest.TestCase):

    def test_word_counts_empty(self):

        text = ""

        # call method under test
        actual = counter.word_counts(text)

        self.assertEqual(actual, [])

    def test_word_counts_one(self):

        text = "foo"

        # call method under test
        actual = counter.word_counts(text)

        self.assertEqual(actual, [('foo', 1)])

    def test_word_counts(self):

        text = "foo bar baz foo bar bar baz bar"

        # call method under test
        actual = counter.word_counts(text)

        self.assertEqual(actual, [('bar', 4), ('foo', 2), ('baz', 2)])

    def test_word_counts_from_file(self):

        filename = "data/input/words0_test.txt"

        # call method under test
        actual = counter.word_counts_from_file(filename)

        self.assertEqual(actual, [('bar', 4), ('foo', 2), ('baz', 2)])
