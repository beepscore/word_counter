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

    def test_write_word_counts(self):

        input_filename = "data/input/words1_test.txt"
        output_filename = "data/output/counts1.txt"

        # call method under test
        counter.write_word_counts(input_filename, output_filename)

        # read output_file in order to test it
        # throws UnicodeDecodeError: 'utf-8' codec can't decode byte
        outfile = open(output_filename, 'r', encoding='utf-8')
        # text is a string containing the entire text file
        actual = outfile.read()
        outfile.close()

        expected = """('bar', 4)
('mary', 3)
('foo', 2)
('baz', 2)
('why', 2)
('words0', 1)
('txt', 1)
('blah', 1)
('yay', 1)
('had', 1)
('little', 1)
('lamb', 1)
('oh', 1)
('nonsense', 1)
('follows', 1)
('fog', 1)
('bottom', 1)
"""

        self.assertEqual(actual, expected)
