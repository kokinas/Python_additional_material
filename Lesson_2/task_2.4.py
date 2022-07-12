"""4. Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры."""

print('BEGIN')
sum_el = 0
el = 1
n = int(input('type a numb: '))
for i in range(0, n):
    sum_el += el
    el /= (-2)
print(sum_el)
print('END')
