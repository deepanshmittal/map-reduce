#!/usr/bin/env python3
import sys

# Mapper: Read each line, split it into words, and emit each word with a count of 1
for line in sys.stdin:
    line = line.strip()            # Remove whitespace from the beginning and end
    words = line.split()            # Split line into words
    for word in words:
        print(f"{word}\t1")         # Emit word and count (1)
