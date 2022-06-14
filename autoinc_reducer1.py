#!/usr/bin/env python

import sys

"""
    autoinc_reducer1.py is piped to autoinc_mapper2.py

    methods:
        - reset()
            resets variables to scan next row
        - flush()
            prints output if the incident type was an Accident
"""
current_key = None
current_values = []
initial_sale_dict = {}

def reset():
    global current_key
    global current_values
    global initial_sale_dict

    current_key = None
    current_values = []
    initial_sale_dict = {}

def flush():
    global current_key
    global current_values
    global initial_sale_dict

    for value in current_values:
        type = value[0]
        if type == 'A':
            make = initial_sale_dict[current_key][1]
            year = initial_sale_dict[current_key][2]
            values = (type, make, year)

            print '%s\t%s' % (current_key,values)
        else:
            continue

for line in sys.stdin:
    line = line.split('\t')

    key = line[0]
    values = eval(line[1]) # reads in the tuple from stdin
    type = values[0]

    if type == 'I': # type I has all necessary information
        initial_sale_dict[key] = values

    if current_key != key: # detects key changes
        if current_key != None:
            flush()
        reset()

    current_key = key
    current_values.append(values)

flush()