#!/usr/bin/env python

import sys

"""
    autoinc_reducer2.py is a reducer for the mapped values from autoinc_mapper2.py

    methods:
        - reset()
            Resets variables to scan next row
        - flush()
            If the incident type is A (Accident), print out:
                1) the combination of make and year
                2) the count of that combination of make and year
"""

current_key = None
current_value = []

def reset():
    global current_key
    global current_value

    current_key = None
    current_values = []

def flush():
    global current_key
    global current_value

    total = 0

    for value in current_value:
        count = value
        total += count

    print '%s\t%s' % (current_key, total)

for line in sys.stdin:
    line = line.split('\t')
    
    key = line[0] # make and year
    value = int(line[1]) # count per combo of make and year

    if current_key != key: # catches key changes
        if current_key != None:
            flush()
        reset()

    current_key = key
    current_value.append(value)

flush() # flush last group if needed