"""6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше
введенное пользователем число, чем то, что загадано. Если за 10 попыток
число не отгадано, вывести ответ."""
import random

print('game start')
hid_numb = random.randint(1, 100)
f_win = 0
for i in range(0, 10):
    est_numb = int(input('type estimated number: '))
    if est_numb == hid_numb:
        f_win = 1
        break
    elif est_numb > hid_numb:
        print('hidden number is less')
    elif est_numb < hid_numb:
        print('hidden number is more')
if f_win:
    print('you win')
else:
    print('you lose')
print('game end')
