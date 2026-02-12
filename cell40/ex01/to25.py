input = int(input('Enter a number less than '))

if input > 25:
    print('Error')
else:
    for i in range(input, 26, 1):
        print('Inside the loop, my variable is',i)