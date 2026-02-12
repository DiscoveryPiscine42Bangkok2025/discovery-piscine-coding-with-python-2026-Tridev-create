import sys
inputs= int(input(''))

i = 0
j = 0
new_i = 0
while i < inputs:
    print(f'Table de {i}: 0 ', end='')
    while j < 10:
        new_i += i
        print("", new_i, end='')
        j += 1
    print()
    i+=1
    j = 0
    new_i = 0
