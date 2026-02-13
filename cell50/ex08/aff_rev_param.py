#!/usr/bin/env python3
import sys
count = len(sys.argv)

if count <= 2:
    print('none')
else:
    print()
    for i in range(count-1, 0, -1):
        print(sys.argv[i])

