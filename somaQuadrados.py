n = int(input('Digite o número de valores: '))

soma_quadrados = 0

for i in range(n):
    valor = float(input(f'Digite o valor {i + 1}: '))
    soma_quadrados += valor ** 2

print(f'A soma dos quadrados dos {n} valores é: {soma_quadrados}')