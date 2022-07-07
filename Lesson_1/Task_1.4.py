"""4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
 и сколько между ними находится букв.
"""
a = ord(input('type the first char a to z: '))
b = ord(input('type the second char a to z: '))
if 96 < a < 123 and 96 < b < 123:
    a_pos = a - 96
    b_pos = b - 96
    dif = b - a - 1
    print(f'position the first char is {a_pos}\nposition the second char is {b_pos}\nnumb of chars between {dif}')
else:
    print('input data is incorrect')