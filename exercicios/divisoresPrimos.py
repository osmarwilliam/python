import time

def divisores(numero):
    count = 1
    numero_divisores = 0
    while count <= numero:
        if numero % count == 0:
            print(count)
            numero_divisores += 1
        count+=1

    if numero_divisores == 2:
        print(f'{numero} é primo')
    return ''


def divisores_n(intervalo):
    intervalos_int = int(intervalo)
    for m in range(2, intervalos_int):
        soma = 0
        for i in range(1, int(m/2)+1):
            if m % i == 0:
                soma+= i
        if m == soma:
            print(f'o {m} é perfeito')
        else:
            print(f'{m} não é perfeito')
    return ''

inicio = time.time()
divisores_n(100000)
fim = time.time()
print(fim - inicio)

