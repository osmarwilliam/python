import time
import random

lista = [random.randint(0,1000) for _ in range(100000)]

inicio = time.time()

def bubble_sort(lista : list) -> list:     
    tamanho = len(lista)
    j = 0
    while tamanho != j:
        for i in range(1, tamanho - j):
            if lista[i] < lista[i - 1]:
                lista[i],lista[i - 1] = lista[i - 1], lista[i]
        j += 1
    return lista

print(bubble_sort(lista))
fim = time.time()
print(fim - inicio)

# usando bubbleSort levou 406.34 segundos para realizar o código