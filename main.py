#!/usr/bin/env python3

from word_counter import counter

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
# if __name__ == '__main__':

input_filename = "data/input/words.txt"
output_filename = "data/output/counts.txt"

counter.write_word_counts(input_filename, output_filename)
