#!/usr/bin/env python3
import sys
def downcase_it(strs):
    result = []
    for i in range(1, len(sys.argv)):
        txt = f'{sys.argv[i]}'
        result.append(txt.lower())

    return result

r = downcase_it(sys.argv)
for i in r:
    print(i)