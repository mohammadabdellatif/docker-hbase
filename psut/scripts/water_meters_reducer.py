#!/usr/bin/python

import sys

k_min = 10000
k_max = 110000
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    fields = line.split(",")
    max_readings = int(fields[4])  # max reading
    norm = (max_readings - k_min) / (k_max - k_min)
    if 0 <= norm <= 1:
        print(line)
