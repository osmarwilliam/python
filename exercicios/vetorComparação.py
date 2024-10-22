"""
Faça um programa que preencha por leitura um vetor
de 10 posições, e conta quantos valores diferentes
existem no vetor.
"""
vetor = [] 

for i in range(0, 10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    vetor.append(valor)

contagem = 0

for i in range(10):
    unico = True
    for j in range(i):
        if vetor[i] == vetor[j]:
            unico = False
            break
    if unico:
        contagem += 1

print(f"existem {contagem} valores diferentes no {vetor}")