# Находит средне арифметическое с точностью трех знаков после запятой(точки).

from statistics import mean


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

num_average = round(mean(numbers) ,3)

print('Arithmetical mean: ', num_average)
