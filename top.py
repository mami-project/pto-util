#!/usr/bin/env python3

################################################################################
# Simple script to print the first N lines from a file
# Author: Piet De Vaere --- piet@devae.re
################################################################################

import sys
import random

USAGE_STRING = "Usage: ./top.py NUMBER_OF_LINES < input_data > topfile\n"

if len(sys.argv) != 2:
    sys.stderr.write(USAGE_STRING)
    sys.exit(1)

try:
    num_of_lines = int(sys.argv[1])
except ValueError:
    sys.stdout.write(USAGE_STRING)
    sys.exit(1)

lines = []
line_counter = 0
for line in sys.stdin:
    if line_counter >= num_of_lines:
        break
    sys.stdout.write(line)
    line_counter = line_counter + 1

if line_counter < num_of_lines:
    sys.stderr.write("WARNING: file shorter than requested number of lines\n")
