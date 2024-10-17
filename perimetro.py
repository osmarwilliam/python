import math
raio = input('Digite o valor do raio da circunfência: ')
while raio.isdigit() == False:
    print('Digite um número: ')
    raio = input()

raio_int = int(raio)
circunferencia = 2 * raio_int * math.pi

print(f'A circunferência do raio {raio} é {circunferencia:.3f}')
