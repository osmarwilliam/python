combustivel = input().split()

for i in range(len(combustivel)):
    combustivel[i] = float(combustivel[i])


def combustivel_economico(combustivel : list) -> str:
    alcool = combustivel[2] /  combustivel[0]  
    gasolina = combustivel[3] / combustivel[1] 
    if alcool > gasolina:
        return 'A'
    else:
        return 'G'

resultado = combustivel_economico(combustivel)
print(resultado)