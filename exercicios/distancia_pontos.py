primeiro_x = input('Digite a coordenada X do primeiro ponto: ')
primeiro_y = input('Digite a coordenada Y do primeiro ponto: ')

segundo_x = input('Digite a coordenada X do segundo ponto: ')
segundo_y = input('Digite a coordenada Y do segundo ponto: ')

distancia = (((int(segundo_x) - int(primeiro_x)) ** 2) + (int(segundo_y) - int(primeiro_y))** 2)

print(f'{distancia}')