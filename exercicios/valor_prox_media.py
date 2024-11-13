lista = [2.5, 7.5, 10.0, 4.0,7.3,7.2]

media = 0
for _ in range(len(lista)):
    media += lista[_]
media = media / len(lista)
print(media)
menor_valor = abs(lista[0] - media)
num_index = 0
for _ in range(1,len(lista)):
    if abs(lista[_] - media) < menor_valor:
        num_index = _
        menor_valor = abs(lista[_] - media)

print(lista[num_index])