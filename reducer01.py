#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

# Reducer: Sum counts for each word
for line in sys.stdin:
    line = line.strip()                        # Remove whitespace
    word, count = line.split('\t', 1)          # Split word and count
    count = int(count)                         # Convert count to integer

    if current_word == word:
        current_count += count                 # If same word, add count
    else:
        if current_word:                       # If word changed, print result
            print(f"{current_word}\t{current_count}")
        current_word = word                    # Update to new word
        current_count = count                  # Reset count

# Output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")
