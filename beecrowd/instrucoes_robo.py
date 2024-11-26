n = int(input())
for i in range(n):
    rodadas= int(input())
    coordenadas = 0
    direcao = [0 for i in range(rodadas)]
    for j in range(rodadas):
        movimento = list(map(str, input().split()))
        if movimento[0] == "RIGHT":
            coordenadas += 1
            direcao[j] = "RIGHT"
        elif movimento[0] == "LEFT":
            coordenadas -= 1
            direcao[j] = "LEFT"
        else:
            valor = int(movimento[2]) - 1
            if direcao[valor] == "RIGHT":
                coordenadas += 1
                direcao[j] = "RIGHT"
            else:
                coordenadas -= 1          
                direcao[j] = "LEFT"
    print(coordenadas)