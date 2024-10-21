def por_extenso(num):
    unidades = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    teens = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove']
    dezenas = ['','dez','vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['','cem', 'dozentos', 'trezentos', 'quatrocentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
    
    if 0 <= num < 10:
        return unidades[num]
    elif 10 <= num < 20:
        return teens[num - 10]
    elif 20 <= num < 100:
        return dezenas[num // 10] + ('' if num % 10 == 0 else ' e ' + unidades[num % 10])
    elif 100 <= num < 1000:
        return centenas[num // 100] + ('' if num % 100 == 0 else ' e ' + por_extenso(num % 100))
    elif 1000 <= num < 10000:
        return unidades[num // 1000] + ' mil' + ('' if num % 1000 == 0 else ' ' + por_extenso(num % 1000))


numero = int(input("Digite um número entre 0 e 9999: "))

if 0 <= numero <= 9999:
    print(f"{numero} por extenso: {por_extenso(numero)}")
else:
    print("Número fora do intervalo permitido!")