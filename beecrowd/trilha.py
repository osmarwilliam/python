x = int(input())
rotas = [float('inf'), 0]

for i in range(1,x+1):
    trilhas = list(map(int, input().split()[1:]))
    somador1, somador2 = 0, 0
    n = len(trilhas)
    for j in range(n - 1):
        if trilhas[j] < trilhas[j+1]:
            somador1 += trilhas[j+1] - trilhas[j]
        if trilhas[n-1-j] < trilhas[n-2-j]:
            somador2 += trilhas[n-j-2] - trilhas[n-j-1]
    menor_soma = min(somador1, somador2)
    if menor_soma < rotas[0]:
        rotas = [menor_soma, i]
print(rotas[1])