risada = input()
lista = ['a','e','i','o','u']
tamanho = len(risada)
nova_risada = ""
for i in range(tamanho):
    if risada[i] in lista:
        nova_risada = nova_risada + risada[i]
print("S" if nova_risada == nova_risada[::-1] else "N")    