sensores, num_carrinhos, rodadas = map(int, input().split())
valores = [[i,0] for i in range(1, num_carrinhos + 1)]
for i in range(rodadas):
    pos, sensor = map(int, input().split())
    valores[pos - 1][1] += sensor

for j in range(num_carrinhos - 1):
    mais_rapido = valores[0][0]
    valor = 0
    for i in range(num_carrinhos - 1):
        if valores[i][1] < valores[i+1][1]:
            mais_rapido = valores[i+1][0]
            valor = i + 1
    valores.pop(valor)
    num_carrinhos -= 1
    print(mais_rapido, end=" ")
print(valores[0][0])
