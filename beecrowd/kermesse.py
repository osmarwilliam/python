"""
Conhecendo a lista de participantes, por ordem de chegada, sua tarefa é determinar o número do bilhete vencedor, 
sabendo que o vencedor é o único participante que tem o número do bilhete igual à sua posição de entrada na festa.

Entrada:
A entrada consiste em vários conjuntos de teste. A primeira linha de um conjunto de testes contém um inteiro positivo N (0 ≤ N ≤ 10000) 
que indica o número de participantes. A próxima linha contém o seguinte, por ordem de entrada, de N ingressos de pessoas que participaram da festa. 
O fim da entrada é indicado quando N = 0. Para cada conjunto de teste de entrada, haverá um único vencedor.
"""

count = 1
controle_flag = True
while controle_flag: 
    qte_participantes = int(input())
    if qte_participantes == 0:
        break
    lista_participantes = [0] * qte_participantes
    lista = input().split()
    for i in range(qte_participantes):
        lista[i] = int(lista[i])
        lista_participantes[i] = lista[i]
    print(f'Teste {count}')
    for i in range(qte_participantes):
        if i + 1 == lista[i]: 
            print(i + 1)
    print('')
    count += 1
