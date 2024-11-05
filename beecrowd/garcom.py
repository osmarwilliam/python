def garcom(rodadas : int) -> None:
    cont = 0
    for _ in range(rodadas):
        latas, copos = map(int, input().split())
        if latas > copos:
            cont += copos
    print(cont)
rodadas = int(input())
garcom(rodadas)