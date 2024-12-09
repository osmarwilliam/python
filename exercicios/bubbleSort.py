import time
import random

lista = [random.randint(0,1000) for _ in range(100000)]

inicio = time.time()

def bubble_sort(lista : list) -> list:     
    tamanho = len(lista)
    j = 0
    flag = True # *
    while tamanho != j or flag != True:
        for i in range(1, tamanho - j):
            if lista[i] < lista[i - 1]:
                lista[i],lista[i - 1] = lista[i - 1], lista[i]
            else: # *
                flag == False # *  (adicionado uma saída caso a lista esteja ordenada)
        j += 1
    return lista

print(bubble_sort(lista))
fim = time.time()
print(fim - inicio)

# usando bubbleSort levou 406.34 segundos para realizar o código
# com as alterações em "*" o código levou 381 segundos, uma significativa melhora