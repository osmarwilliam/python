# Faça um programa para determinar o número
# de dígitos de um número inteiro positivo
# informado
'''
def qtd_digitos(tamanho):
    count = 0
    tamanho_str = str(tamanho)
    for i in tamanho_str:
        count+= 1
    return count

print(f'{qtd_digitos(2000)}')
'''


def rev(w):
    w_int = w
    s = ''
    for i in w_int:
        s = i + s
    return s

print(rev('123'))
