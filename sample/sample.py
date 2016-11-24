#!/usr/bin/env python3

################################################################################
# Simple script to sample a number of lines from a file
# Author: Piet De Vaere --- piet@devae.re
################################################################################

import sys
import random

USAGE_STRING = "Usage: ./sample.py SAMPLE_SIZE < input_data > sample\n"

if len(sys.argv) != 2:
    sys.stderr.write(USAGE_STRING)
    sys.exit(1)

try:
    sample_size = int(sys.argv[1])
except ValueError:
    sys.stdout.write(USAGE_STRING)
    sys.exit(1)

# Get the lines of the file
lines = []
for line in sys.stdin:
    lines.append(line)

# Shuffle them
if sample_size > len(lines):
    sys.stderr.write("ERROR: sample size larger than input size\n")
    sys.exit(1)

sample = random.sample(lines, sample_size)

# Write them out
for line in sample:
    sys.stdout.write(line)
