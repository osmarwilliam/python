pontos_de_agua, distancia_max = map(int, input().split())
posicao = list(map(int, input().split())) + [42195]

def prova(lista : list, distancia : int) -> str:
    for i in range(len(lista) - 1):
        if lista[i + 1] - lista[i] > distancia:
            return 'N'
    return 'S'

print(prova(posicao, distancia_max)) 