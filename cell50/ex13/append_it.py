#!/usr/bin/env python3
import sys
count = len(sys.argv)

if count <= 1:
    print('none')
else:
    # inputs = input('What was the parameter? ')
    # print('parameter:', count - 1)
    print()
    for i in range(1, len(sys.argv)):
        if 'ism' in sys.argv[i]:
            pass
        else:
            print(f'{sys.argv[i]}ism')


