# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Это решение справедлито только  для одинаково записанных файла

# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
#     if file1[i-1] != '^':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close

# # 5*x^2+20x+5
# # 4*x^2+22x+1

import random
def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res


def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res


f = open('dz40.txt', 'w')
f.write(nmnogochlen1())
print(nmnogochlen1())
f.close()

f = open('dz41.txt', 'w')
f.write(nmnogochlen2())
print(nmnogochlen2())
f.close()

f = open('dz42.txt', 'w')
f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
f.close()

