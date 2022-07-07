"""6. По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой треугольник
существует, то определить, является ли он разносторонним, равнобедренным или равносторонним."""
a = float(input('type length the first side of triangle: '))
b = float(input('type length the second side of triangle: '))
c = float(input('type length the third side of triangle: '))
if a + b > c and a + c > b and b + c > a:
    print('triangle is exist')
else:
    print('triangle is not exist')
