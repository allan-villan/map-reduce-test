#!/usr/bin/env python

import sys

"""
    autoinc_mapper1.py is the mapper for autoinc_reducer1.py

    The key is the vin_number:
        - Each vehicle has a repeating vin_number for multiple entries.

    The values is a tuple of:
        - the incident type
        - make of car
        - year of car
"""
for line in sys.stdin:
    line = line.split(",") # delimited by commas

    type = line[1]
    vin_num = line[2]
    make = line[3]
    year = line[5]

    key = vin_num
    value = (type, make, year)

    print '%s\t%s' % (key, value)