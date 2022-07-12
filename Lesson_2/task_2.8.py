"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности
чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""
digit = input('type a digit: ')
number = input('type a complicate nsumber: ')
count_numb = 0
for i in number:
    if i == digit:
        count_numb += 1
print(count_numb)
