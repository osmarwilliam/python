rodadas = int(input())

for i in range(rodadas):
    valor_1, valor_2 = list(map(str, input().split()))
    if len(valor_2) > len(valor_1):
        print("nao encaixa")
        continue
    flag = True
    tamanho = len(valor_2)
    for _ in range(tamanho):
        if valor_2[_] != valor_1[-tamanho]:
            flag = False
        tamanho -= 1
    print("encaixa" if flag == True else "nao encaixa")