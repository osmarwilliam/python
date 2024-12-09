import random

lista = [random.randint(0, 10) for _ in range(10)]
print(lista)
print(lista.count(10)) # count verifica quantos elementos de um determinado número está presente na lista

lista.append(4)
lista = [1,2,3,4,5]

print("--------------------")
def multavel(lista : list) -> None:
    lista.append(6) # o append altera diretamente no ponteiro da lista onde está na memória
    print(lista, "lista multavel")
    return;
multavel(lista)
print(lista)
print("--------------------")
def NotMultavel(lista : list) -> None:
    lista = lista + [7] # não altera a lista original, já que dentro dessa funcao é uma copia da lista original
    print(lista, "lista nao multavel")
    return;

NotMultavel(lista)
print("--------------------")
print(lista)


print("--------------------")
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]
lista1 = lista1 + lista2
print(lista1)

print("--------------------")
lista2.insert(2, 10)
print(lista2)

lista2.pop(2) # elimina o elemento com base no index
print(lista2)


lista2.remove(6) # elimina a primeira recorrencia

lista2 = lista1

print(lista.index(2)) # .index methd mostra o index de determinado número passado como argumento

lista2.reverse()
lista1[::-1]

print("--------------------")
print(lista1)

lista1[1:3] = [1,2,3,4,5]
print(lista1)

print("--------------------")
lista1[0::2] = [1,2,3,4,5]
print(lista1)

lista = [1,2,3,4,5]

print("--------------------")
lista[1:1] = "z"
print(lista)
print("--------------------")
lista[1:3] = [[7]]
print(lista)
print("--------------------")
lista[1:-1] = 8,9,10
print(lista)
print("--------------------")
lista[:2] = 1,2,3
print(lista)
print("--------------------")

lista1 = [1, 2, 3]
lista2 = lista1 # ao criar essa variável o ponteiro das duas estão apontando para o mesmo local da memória

# utilize o for ou o slice para resolver esse problema de ponteiro

lista2.append(4)
print(lista1)
print(lista2)

print("--------------------")
print("--------------------")

notas = [[5.0, 4.5, 7.0, 5.2, 6.1], [2.1, 6.5, 8.0, 7.0, 6.7],
[8.6, 7.0, 9.1, 8.7, 9.3]]

print(notas[0][1])

print(len(notas[1]))

notas = []
for i in range(3):
# cria linha vazia
    linha = []
    for j in range(5):
        #vai adicionando as notas na linha
        linha.append(input(f'Digite anota [{i}, {j}]: '))
        #adiciona a linha na matriz turma
    notas.append(linha)
    print(notas)

print(notas)


print("------------------------")
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]
def AlgoMultavel(lista : list, lista2 : list) -> None:
    lista = lista + lista2 # não altera a lista original, já que dentro dessa funcao é uma copia da lista original
    print(lista, "lista")
    return;

AlgoMultavel(lista1, lista2)
print(lista1)



c = list(map(int, input().split()))
print(c)