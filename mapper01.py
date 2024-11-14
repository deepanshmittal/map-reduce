#!/usr/bin/env python3
"""mapper01.py"""

import sys

for line in sys.stdin:
	print(f"1 {line.strip().split()}")