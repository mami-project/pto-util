#!/usr/bin/env python3

################################################################################
# Simple script to shuffle the lines in a file.
# Reads line from stdin shuffles them, and then writes them to stdout
# Author: Piet De Vaere --- piet@devae.re
################################################################################

import sys
import random

# Get the lines of the file
lines = []
for line in sys.stdin:
    lines.append(line)

# Shuffle them
random.shuffle(lines)

# Write them out
for line in lines:
    sys.stdout.write(line)
