"""7. Определить, является ли год, который ввел пользователь, високосным или не високосным."""
year = int(input('type a year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('year is leap')
        else:
            print('year is not leap')
    else:
        print('year is leap')
else:
    print('year is not leap')