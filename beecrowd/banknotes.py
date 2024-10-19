def troco(valor): # o valor nesse caso é um parametro, e quando passamos algo quando a função é chamada é o que chamamos de argumento
    resto = valor
    resultado = {}
    for i in [100, 50, 20, 10, 5, 2, 1]:
        count = 0
        while resto >= i:
            count += 1
            resto -=  i
        resultado[i] = count
    return resultado

troco_valores = troco(596) # chamamos a função troco, e passamos 596 como argumento da função

for nota, quantidade in troco_valores.items():
    print(f'{quantidade} nota(s) de R$ {nota}')
