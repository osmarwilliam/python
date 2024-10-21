centavos = input('Digite a quantidade de centavos: ')

while centavos.isdigit() == False:
    print("digite um número: ", end="")
    centavos = input()
centavos_int = int(centavos)
'''
resto = 0
real = moedas_int // 100 
resto = moedas_int -  (real * 100)

cinquenta_centavos = resto // 50
resto = resto - (cinquenta_centavos * 50)

vinte_cinco = resto // 25
resto = resto - (vinte_cinco * 25)

dez_centavos = resto // 10
resto = resto - (dez_centavos * 10)

cinco_centavos = resto // 5
resto = resto - (cinco_centavos  * 5)

um_centavo = resto

print(f'Quantidade de moedas de 1 real = {real} \n'
      f'Quantidade de moedas de 50 centavos = {cinquenta_centavos}\n'
      f'Quantidade de moedas de 25 centavos = {vinte_cinco}\n'
      f'Quantidade de moedas de 10 centavos = {dez_centavos}\n'
      f'Quantidade de moedas de 5 centavos = {cinco_centavos}\n'
      f'Quantidade de moedas de 1 centavos = {um_centavo}')
'''

moedas = [100, 50, 25, 10, 5, 1]

for moeda in moedas:
    qtd_usadas = centavos_int//moeda
    centavos_int = centavos_int - qtd_usadas * moeda
    print(f'Moedas de {moeda} centavo(s): {qtd_usadas}')
