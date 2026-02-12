#!/usr/bin/env python3
import sys
count = len(sys.argv)

if count <= 2:
    print('none')
else:
    for i in range(1, count):
        print(sys.argv[i])

