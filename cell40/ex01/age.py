inputs = int(input('Please tell me your age: '))
print('You are currently', inputs)
for i in range(inputs+10, inputs+(10*4), 10):
    print("In 10 years, you'll be", i, 'years old')