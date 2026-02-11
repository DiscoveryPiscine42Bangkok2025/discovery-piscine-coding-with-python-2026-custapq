array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for i in range(len(array)):
    if array[i] > 5 and array[i] not in new_array:
        new_array.append(array[i])

print(f'original array: {array}')
for i in range(len(new_array)):
    new_array[i] += 2

print(f'new array: {new_array}')