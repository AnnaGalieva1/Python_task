#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите коорджинату x:'))
y = int(input('Введите коорджинату y:'))
if x == 0 and y == 0:
    print('точка в начале координат')
elif x == 0:
    print('точка на оси x')
elif y == 0:
    print('точка на оси y')

if x > 0 and y > 0:
    print(f'точка ({x}, {y}) - в 1 четверти')
elif x < 0 and y > 0:
    print(f'точка ({x}, {y}) - во 2 четверти')
elif x < 0 and y < 0:
    print(f'точка ({x}, {y}) - в 3 четверти')
elif x > 0 and y < 0:
    print(f'точка ({x}, {y}) - в 4 четверти')