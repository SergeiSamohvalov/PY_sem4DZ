# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# n = int(input('Введите натуральное число: '))

# def f(n, d=2):
#     rez = []
#     while d * d <= n:
#         if n % d == 0:
#             rez.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         rez.append(n)
#     return rez
# print(n,"=", "*".join(map(str, f(n))))

num = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")

