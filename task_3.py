# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list_1 = [7, 2, 5, 4, 7, 3, 6, 2, 5, 8, 13, 8]

def get_unique_numbers(list_1):
    list_of_unique_numbers = []
    unique_numbers = set(list_1)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers

print(get_unique_numbers(list_1))
