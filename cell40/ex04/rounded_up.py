import sys
inputs= float(input(''))

if inputs <= 1:
    inputs = str(inputs)
    # print(inputs[3])
    print(inputs[-1])
else:
    inputs = round(inputs)
    print(inputs)

