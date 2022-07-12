"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""
str_numbs = input('type numbers in format split space: ')
numbs = str_numbs.split()
sum_digit = 0
max_sum_digit = 0
max_numb = 0
for numb in numbs:
    for digit in numb:
        sum_digit += int(digit)
    if sum_digit > max_sum_digit:
        max_sum_digit = sum_digit
        max_numb = numb
    sum_digit = 0
print(max_numb, max_sum_digit)
