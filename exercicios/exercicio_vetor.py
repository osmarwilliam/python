vetor = []

for i in range(5):
    valor = int(input(f'Digite o valor para a {i + 1}º posição: '))
    vetor.append(valor)

x = int(input("Digite um valor para verificar se ele está presente no vetor: "))
if x in vetor:
    print(f'{x} está presente no {vetor}')
else:
    print('-1')