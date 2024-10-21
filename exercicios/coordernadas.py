import math

x1 = int(input('Informe o x1:'))
y1 = int(input('Informe o y1:'))

x2 = int(input('Informe o x2:'))
y2 = int(input('Informe o y2:'))

x3 = int(input('Informe o x3:'))
y3 = int(input('Informe o y3:'))

d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
d2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
d3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)


if d1 == d2 == d3:
    print('Esse triangulo é equilátero')
elif d1 == d2 != d3 or d1 == d3 != d2 or d1 != d2 == d3:
    print('Esse triangulo é Isósceles')
else:
    print('Esse triangulo é escaleno')
