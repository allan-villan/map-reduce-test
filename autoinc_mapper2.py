#!/usr/bin/env python

import sys

"""
    autoinc_mapper2.py is a mapper for autoinc_reducer2.py

    The key is the make and year of an incident type A (Accident) concatenated
    The value is the count 1 (For each make and year combination)
"""
for line in sys.stdin:
    line = line.split('\t')

    values = eval(line[1]) # reads in the tuple provided

    make = values[1]
    year = values[2]

    mapper2_key = '%s %s' % (make, year)
    
    print '%s\t1' % (mapper2_key)
