"""5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""
a = int(input('type numb of symbol alphabet: '))
if 0 < a < 27:
    char_a = chr(a + 96)
    print(f'symbol is {char_a}')
else:
    print('input data is incorrect')