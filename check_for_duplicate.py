#!/usr/bin/env python3

################################################################################
# Simple script to check if there are duplicate lines in a file
# Reads input file from stdin
# Author: Piet De Vaere --- piet@devae.re
################################################################################

import sys
import random

lines = set()
counter = 0
for line in sys.stdin:
    if line in lines:
        counter = counter + 1
    lines.add(line)

if counter == 0:
    sys.stderr.write("Found no duplicate lines\n")
else:
    sys.stderr.write("Found {} duplicate lines\n".format(counter))
