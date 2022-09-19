# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))

def f(n, d=2):
    rez = []
    while d * d <= n:
        if n % d == 0:
            rez.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        rez.append(n)
    return rez
print(n,"=", "*".join(map(str, f(n))))
