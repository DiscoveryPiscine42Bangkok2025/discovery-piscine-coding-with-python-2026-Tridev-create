array = [2,6,4,7,10,12]
new_array = []

print('Original array:', array)

for i in array:
    if i > 5:
        i+=2
        new_array.append(i)

print('New array', new_array)