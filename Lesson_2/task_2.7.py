"""7. Написать программу, доказывающую или проверяющую, что для множества натуральных
чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число."""
n = 9999999
sum_numb1 = 0
for i in range(1, n + 1):
    sum_numb1 += i
    sum_numb2 = i * (i + 1) / 2
    if sum_numb1 != sum_numb2:
        print('theory is false')
print('theory is truth')
