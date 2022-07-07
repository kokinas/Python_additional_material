"""3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""
import random

a = int(input('type int a: '))
b = int(input('type int b: '))
print(random.randint(a, b))
a = float(input('type float a: '))
b = float(input('type float b: '))
print(random.uniform(a, b))
a = ord((input('type symbol a: ')))
b = ord(input('type symbol b: '))
print(chr(random.randint(a, b)))
