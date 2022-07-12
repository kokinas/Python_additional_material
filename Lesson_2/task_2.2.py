"""2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

print('BEGIN')
count_even = 0
count_odd = 0
inp_numb = int(input('type a number: '))
numb = inp_numb
while numb > 0:
    digit = numb % 10
    numb //= 10
    if digit % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f'count even digit in {inp_numb} is {count_even}')
print(f'count odd digit in {inp_numb} is {count_odd}')
print('END')
