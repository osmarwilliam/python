n, m = map(int, input().split())
total_minhocas = []
somador_por_coluna = [0] * m
somador_por_linha = [0] * n

for i in range(n):
    linha = list(map(int, input().split()))
    total_minhocas.append(linha)
    for j in range(m):
        somador_por_coluna[j] += total_minhocas[i][j]
        somador_por_linha[i] += linha[j]
maior_linha = max(somador_por_linha)
maior_coluna = max(somador_por_coluna)
print(maior_linha if maior_linha > maior_coluna else maior_coluna)