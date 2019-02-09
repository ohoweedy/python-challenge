import os
import csv
import re

pypara = os.path.join('PyParagraph.txt')

# with open(pypara, newline='') as textfile:

# Read in local rtf file
# txt = open('PyParagraph.txt').read()

# print(txt)
num_words = 0

with open(pypara, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

with open(pypara, 'r') as f:
    for line in f:
        sentences = line.split()
        num_words += len(words)


print(f"Number of words: {num_words}")
