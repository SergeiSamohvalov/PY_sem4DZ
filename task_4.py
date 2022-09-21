# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# import random
# from itertools import chain
# from itertools import zip_longest


# def input_data_check():
#     i = True
#     while i:
#         try:
#             input_number = int(input('Задайте натуральную степень k: '))
#             if input_number == 0:
#                 continue
#             i = False
#         except ValueError:
#             print('Ввод данных не верен, повторите ввод!')
#     return input_number


# def coeff(number):
#     coeffs = list()
#     for i in range(0, number + 1):
#         x = int(random.randint(0, 101))
#         coeffs.append(x)
#     while coeffs[0] == 0:
#         coeffs[0] = random.randint(1, 101)
#     # print(coeffs)
#     return coeffs


# def funct(number, coefs):
#     var = ['*x^']*(number-1) + ['*x']
#     function = [[a, b, c] for a, b, c in zip_longest(
#         coefs, var, range(number, 1, -1), fillvalue='') if a != 0]
#     # print(function)
#     for i in function:
#         i.append(' + ')
#     # print(function)
#     function = list(chain(*function))
#     # print(function)
#     function[-1] = ' = 0'
#     # print(function)
#     delimiter = ""
#     return delimiter.join(map(str, function))


# k = int(input_data_check())
# coeffs_new = coeff(k)
# func = funct(k, coeffs_new)
# print(func)
# result = open('file.txt', 'a')
# result.write(func)
# result.write('\n')
# result.close()

from random import randint

print('Чтобы сформировать многочлен степени k и записать в файл, введите степень k! ')
k = int(input("Введите степень k: "))

factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))

result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

record = open('data.txt', 'w')
record.write(''.join(result))
record.close()
