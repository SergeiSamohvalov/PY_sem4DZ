# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091
x = int(input("Введите количество знаков после запятой в числе pi = "))

n = 0 
for i in range(x):
    n +=  1 / (16 ** i) * ( 4 / (8*i + 1) -  2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6))

print(f"{n:.{x}f}")
