#!/usr/bin/env python

import sys

def count_name(filename, protein_name):
    count = 0
    for line in filename:
        if line.rstrip() == protein_name:
            count += 1
    return count

if len(sys.argv) != 3:
    sys.exit("Usage: count_name.py <filename> <protein_name>")

filename = sys.argv[1]
protein_name = sys.argv[2]
try:
    input_file = open(filename)
except IOError as e:
    print >>sys.stderr, "Couldn't open {}: {}".format(filename, e.strerror)
    sys.exit(1)
else:
    name_count = count_name(input_file, protein_name)
    print protein_name, name_count
