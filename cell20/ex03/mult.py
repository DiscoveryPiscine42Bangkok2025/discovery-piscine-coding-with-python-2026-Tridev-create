f_num = int(input('Enter first num: '))
s_num = int(input('Enter second num: '))

result = f_num * s_num

print(f'{f_num} * {s_num} =', result)

if result < 0:
    print('This number is negative.')
elif result > 0:
    print('This number is positive.')
else:
    print('This number is both positive and negative.')