import time
import random

inicio = time.time()

lista = [random.randint(0,1000) for x in range(100000)]
def insertion_sort(lista : list) -> list:
    for i in range(1,len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]  # Shift elements to the right
            j -= 1
        lista[j+1] = key
    return(lista)
print(insertion_sort(lista))
fim = time.time()
print(fim - inicio)

# Levou 146.64 segundos para realizar utilizando insertionSort