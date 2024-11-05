def par_impar(rodadas : int, test : int) -> None:
    jogador1, jogador2 = input(), input()
    print(f'Teste {test}')            
    for i in range(rodadas):
        valor1, valor2 = map(int, input().split())
        print(jogador1 if ((valor1 + valor2) % 2 == 0) else jogador2)
    print("")
i = 1
while (rodadas := int(input())) != 0:
    par_impar(rodadas, i)
    i += 1