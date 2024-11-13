lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]

lista_intercalada = []
for _ in range(max(len(lista1), len(lista2))):
    if len(lista1) > _:
        lista_intercalada.append(lista1[_])
    if len(lista2) > _:
        lista_intercalada.append(lista2[_])
print(lista_intercalada)