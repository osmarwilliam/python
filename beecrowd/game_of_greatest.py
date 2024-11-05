def greatest(rodadas: int) -> int:
    count = 0
    jogador1, jogador2 = 0, 0 
    while count < rodadas:
        jogadores = list(map(int, input().split()))
        if jogadores[0] > jogadores[1]:
            jogador1 += 1
        if jogadores[0] < jogadores[1]:
            jogador2 += 1
        count += 1
    return print(jogador1, jogador2) 

while (rodadas := int(input())) != 0:
    greatest(rodadas)