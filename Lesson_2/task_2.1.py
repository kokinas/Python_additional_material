"""1. Написать программу, которая будет складывать, вычитать, умножать или делить два
числа. Числа и знак операции вводятся пользователем. После выполнения вычисления
программа не завершается, а запрашивает новые данные для вычислений. Завершение
программы должно выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать
об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о
невозможности деления на ноль, если он ввел его в качестве делителя."""

print('BEGIN')
while True:
    el1 = int(input('type the first numb: '))
    el2 = int(input('type the second numb: '))
    op = input('type operator + - * / or 0 to exit: ')
    if op == '+':
        print(f'sum is {el1 + el2}')
    elif op == '-':
        print(f'quotient is {el1 - el2}')
    elif op == '*':
        print(f'product is {el1 * el2}')
    elif op == '/':
        if el2 != 0:
            print(f'product is {el1 / el2}')
        else:
            print("don't divide by zero")
    elif op == '0':
        print('END')
        break
    else:
        print('incorrect input data')
