#!/usr/bin/env python3
import sys
count = len(sys.argv)

if count <= 1:
    print('none')
else:
    # inputs = input('What was the parameter? ')
    print('parameter:', count - 1)
    for i in range(1, len(sys.argv)):
        print(sys.argv[i], ':', len(sys.argv[i]))


