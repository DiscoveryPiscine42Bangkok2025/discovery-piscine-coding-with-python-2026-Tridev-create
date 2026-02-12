#!/usr/bin/env python3
import sys
count = len(sys.argv)

if count != 2:
    print('none')
else:
    inputs = input('What was the parameter? ')
    if inputs.count(sys.argv[1]) > 0:
        print('Good job!')
    else:
        print('Nope, sorry...')


