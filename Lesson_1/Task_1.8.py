"""8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""
a = int(input('type a the first numb: '))
b = int(input('type b the second numb: '))
c = int(input('type c the third numb: '))
if a < b < c:
    print(f'b = {b} is middle')
else:
    if c < b < a:
        print(f'b = {b} is middle')
    else:
        if b < a < c:
            print(f'a = {a} is middle')
        else:
            if c < a < b:
                print(f'a = {a} is middle')
            else:
                if a < c < b:
                    print(f'c = {c} is middle')
                else:
                    if b < c < a:
                        print(f'c = {c} is middle')
                    else:
                        print('data is incorrect')
