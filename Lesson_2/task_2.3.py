"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843."""

print('BEGIN')
out_str = ''
inp_str = input('type a numb: ')
for s in inp_str:
    out_str = s + out_str
print(out_str)
print('END')
