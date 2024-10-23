coordenadas = input().split()

for i in range(len(coordenadas)):
    coordenadas[i] = int(coordenadas[i])

distancia = abs(coordenadas[0] - coordenadas[2]) + abs(coordenadas[1] - coordenadas[3])
print(distancia)