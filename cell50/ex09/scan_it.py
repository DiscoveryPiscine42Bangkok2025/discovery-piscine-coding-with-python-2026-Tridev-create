#!/usr/bin/env python3
import sys
count = len(sys.argv)

if count != 3:
    print('none')
else:
    if sys.argv[2].count(sys.argv[1]) > 0:
        print(sys.argv[2].count(sys.argv[1]))
    else:
        print('none')


