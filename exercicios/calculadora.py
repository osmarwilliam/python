# Calculadora com while

while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')

    numero_flag = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_flag = True
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
    except:
        numero_flag = None

    if numero_flag is None:
        print('Digite valores númericos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Foi digitado um operador inválido, tente novamente!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    if operador == '+':
        print(f'A soma de {numero_1_float} + {numero_2_float} = {numero_2_float + numero_2_float}')
    elif operador == '-':
        print(f'A subtração de {numero_1_float} - {numero_2_float} = {numero_2_float - numero_2_float}')
    elif operador == '/':
        print(f'A divisão de {numero_1_float} / {numero_2_float} = {numero_2_float / numero_2_float}')
    elif operador == '*':
        print(f'A multiplicação de {numero_1_float} * {numero_2_float} = {numero_2_float * numero_2_float}')
    else:
        print("Ocorreu algum erro!!")
        
    sair = input('Quer sair? [s]im:').lower().startswith('s')
    if sair is True:
        break