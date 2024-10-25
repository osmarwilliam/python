import time
import random

lista = [random.randint(1,100) for _ in range(100000)]
inicio = time.time()

def selection_sort(lista : list) -> list:
    tamanho = len(lista)
    for i in range(tamanho):
        min = i
        for j in range(i + 1,tamanho):
            if lista[j] < lista[min]:
                    min = j
        lista[min], lista[i] = lista[i], lista[min]    
    return lista

print(selection_sort(lista))
fim = time.time()
print(fim - inicio)

# levou 134 segundos para resolver o código usando selection Sort