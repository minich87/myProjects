# Находит сколько из введенных чисел являются положительными/отрицательными.

length_array  = None
while length_array  == None:
    try:
        length_array = int(input('Enter array length: '))
    except ValueError:
        print('Error! Enter array length!')

numbers = []

i = 0
while i < length_array:
    try:
        string = 'Enter number № ' + str(i+1) + ': '
        numbers.append(float(input(string)))
        i += 1
    except ValueError:
        print('Error! Enter only numbers!')

positive_nums = 0
negative_nums = 0
zero_nums = 0

for x in numbers:
    if x > 0:
        positive_nums += 1
    elif x < 0:
        negative_nums += 1
    else:
        zero_nums += 1

print('Positive numbers:', positive_nums)
print('Negative numbers:', negative_nums)
print('Zero numbers:', zero_nums)
