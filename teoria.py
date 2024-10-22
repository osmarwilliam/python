"""
Algoritmos:
    *   passos para resolver um tipo de problema, 
    lembrando sempre que são passo finitos 

Processamento de informações:
    * o sistema de processamento de dados começa com a entrada de 
    dados(input), e depois de realizar uma serie de instruções,
    muitas vezes realizadas pelos algoritmos escritos, é retornado 
    algum valor, que é conhecido como saída de dados (output)  
    * Quando trato de informações que são recebidas pelas máquinas
    nos inputs, elas podem variar bastante, sendo essas partindo 
    de simples dados de textos, ou vídeos, áudios, imagens, tudo 
    isso representada como informação

Exercício:
    1- Três tipos de agentes computacionais:
        * ser humano, um computador, uma Tv
    2 - Escreva um algoritmo que descreva a segunda parte do 
    processo de fazer  o troco(contando as moedas e notas:
        * 
    3 - In what sense is a laptop computer a general-purpose 
    problem-solving machine?
        * o laptop sendo uma máquina capaz de ler inputs, e por meio
        de algoritmos (escritos por um ser humano) é capaz de gerar 
        um output, resolvendo assim o problema de interesse

The Structure of a Modern Computer System:
    - Um computador moderno consiste de duas partes
        Hardware e Software
            * Hardware é a parte física onde é executada os algoritmos
            * Software é a parte onde os algoritmos são escritos

    Computer Hardware:
        * memory, central procesing unit e vários inputs/outputs devices
        
    Software:
        * o software é aquele responsável pela forma do algoritmo, 
        basicamento ele é capaz determinar as instruções para o hardware,
        dessa forma, o software, é o complemento do hardware, muita vezes
        o que não colocamos no hardware, é responsabilidade do software resolver

    Sistema operaciona:
        * é o responsável por lidar com toda informção, todas entradas e 
        todas saídas de dados, lidando com elas da forma mais eficiente,
        * lidam com a execução dos programas, como a memória deve ser 
        gerida
        * Além de providenciar o que é chamado de user-interface, uma
        maneira de permitir o usuário e a máquina de se comunicarem

    Exercises
        1. List two examples of input devices and two examples of output devices.
            * monitor e caixa de som

        2. What does the central processing unit (CPU) do?
            * é responsável pela execução do algoritmo, ou seja, das instruções 
            que foram passadas para resolver um determinado problema, é capaz de 
            designar esse problema se for necessário para outros componentes. 

        3. How is information represented in hardware memory?
            * Toda informação é representada em binário
        
        4. What is the difference between a terminal-based interface and a graphical user interface?
            * o terminal-base interface é onde o ser humano consegue comunicar com a máquina de forma mais abstrata possível,
            já a graphical user interface (GUI) é uma metáfora do terminal-based interface, mostrando de uma maneira mais amigável, 
            pelo monitor, usando icones para mostrar arquivos, aplicações, sendo também capaz de ser manipulado por meio de um dispositvo, como mouse 
        
        5. What role do translators play in the programming process?
            * é importante para realizar a comunicação com a máquina, visto que, está só conversa em binário, logo, como escrevemos códigos em 
            linguagem de alto nível, é necessario a compilação ou interpretação desse código


"""

print(1 + 1)

# isso é um comentário

"""
    isso nao é um comentário, é uma Docstring, visto que o interpretador 
    ler elas, em vez de ignorar
"""

print(12, 34, sep="", end="\n") # argumentos são passados nas funções
print(56, 78, 1001, sep="--")

'''
    
    ------ Tipos de Dados em PYTHON -------

    tipo de tipagem = Dinâmica / Forte    
        * ser dinâmica significa que o python já sabe qual o tipo sem você 
        precisar dizer para ele (ex: C é estática, visto que é necessário declarar)    

        * ser forte significa que uma variável de um tipo não pode jamais 
        ser tratada como sendo de outro tipo
    
        str --> string --> texto


'''

print("osi")
print('Osi')

# escape
print("osmar \"william\"")

# r
print(r"osmar \"william\"")  # para imprimir as barras também


# Tipos int e float

print(1.2, 10.11)

print(type(12.12))
print(type(12))
print(type(True))
print(type("ola"))

# Tipo Bool (boolean)

print(10 == 10)
print(10 == 11)
print(type(10 == 11))

# conversão de tipos/ coerção / type convertion / typecasting / coercion
# ato de converter um tipo em outro
# Tipos imutáveis e primitivos 
# str, int, float, bool

print(1 + int('1'))
print(bool(' '))

#  variáveis

nome = "william"
idade = 13


nome = "osmar"
sobrenome = "william"
idade = 23
ano_nascimento = 2001
maior_de_idade = idade >= 18
altura = 1.88

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura:", altura)

# operadores aritméticos

    # +, -, *, /, // (divisão inteira), ** (exponenciacao), % (modulo)

nome = "osmar william"
idade = 23
altura = 1.77
peso = 94

imc = peso / altura**2

print(nome, "tem", altura, "de altura")
print("pesa", peso, "quilos e seu imc é:", imc)

# formatação de strings (f string)

linha_1 = f'{nome} tem {altura:.2f} de altura'
print(linha_1)
print(f"pesa {peso} quilos e seu imc é: {imc:.2f}")


a = 'A'
b = 'B'
c = 1.000000011
string = 'a= {nome1}, b= {nome2}, c= {nome3:.2f}'
formato = string.format(nome1 = a, nome2 = b , nome3= c)  
# toda string é um objeto, e sendo um objeto ela possui métodos, e dentro desses métodos é possível passar argumentos 

print(formato)

# INPUT
"""
nome = input('Qual o seu nome? ') # sempre será retornado um valor em str, lembre-se da coerção/
print(f'o seu nome é {nome=}')
"""
# condicionais python   if / elif / else 

'''entrada = input('voce quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('voce entrou!')
elif entrada == 'sair':
    print('voce n entrou')    
else:
    print('voce nao digitou nem entrar e nem sair')
'''

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    pass
elif condicao2:
    pass
elif condicao3:
    pass
elif condicao4:
    ...
else:
    print('fim!')

# operadores de comparação (relacionais)

"""
    >
    >=
    <
    <=
    == igual
    != diferente

"""
'''
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

while primeiro_valor.isdigit() == False:
    print(f'{primeiro_valor=} é uma string, digite um número: ', end="")
    primeiro_valor = input()    

while segundo_valor.isdigit() != True: # toda string é um objeto, e sendo um objeto tem seus métodos, e dentro desses métodos é possível passar argumentos
    print(f'{segundo_valor=} é uma string, digite outro valor: ', end="")
    segundo_valor = input()

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)

if primeiro_valor_int > segundo_valor_int:
    print(f'{primeiro_valor_int=} é maior que o {segundo_valor_int=}')
elif segundo_valor_int > primeiro_valor_int:
    print(f'{segundo_valor_int=} é maior que o {primeiro_valor_int=}')
else:
    print(f'{primeiro_valor_int=} e {segundo_valor_int=} são iguais!')

'''
# primeiro_valor_int = int(primeiro_valor)
# segundo_valor_int = int(segundo_valor)

#if primeiro_valor  :

# operadores lógicos
"""
    and, or, not
    falsy in python = 0, 0.0, False, ""  
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print('Sair')

"""

# operadores in e not in
# string são iteráveis

# Interpolação
nome = 'osmar'
print('c' in nome)
preco = 10000.232452
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %015x' % (15,15 ))

# f-string

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}..')
print(f'{variavel:0<10}..')
print(f'{variavel: ^10}')
print(f'{variavel:s^10}')

print(f'o hexadecimal de 1500 é {1500:08x}')


# fatiamento de strings
1001
variavel = '1001'
print(variavel[4:])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[::-1])

var2 = variavel[::-1]
print(var2)
if var2 == variavel:
    print('sao iguais')
# Exercício
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios')
'''


# Introdução ao TRY/EXPECT
# try -> tentar executar código
# except -> ocorreu algum erro ao tentar executar

'''
numero_str = input('Vou dobrar o número que vc digitar: ')
try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')
'''
'''
linha_1 = input().split()
code1 = int(linha_1[0]) 
number_product1 = int(linha_1[1]) 
units1 = float(linha_1[2])

linha_2 = input().split()
code2 = int(linha_2[0]) 
number_product2 = int(linha_2[1]) 
units2 = float(linha_2[2])

valor_total = number_product1 * units1 + number_product2 * units2
print(f'VALOR A PAGAR: R$ {valor_total}')
'''
'''
linha_1 = input().split()
a = float(linha_1[0])
b = float(linha_1[1])
c = float(linha_1[2])

triangulo = (a * c) / 2
print(f'TRIANGULO: {triangulo:.3f}')
circulo = 3.14159 * c ** 2
print(f'CIRCULO: {circulo:.3f}')
trapezio = (a + b) * c / 2
print(f'TRAPEZIO: {trapezio:.3f}')
quadrado = b * b
print(f'QUADRADO: {quadrado:.3f}')
retangulo = a * b
print(f'RETANGULO: {retangulo:.3f}')
'''

'''
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
maior1 = (a + b + abs(a-b)) / 2
maior2 = int((maior1 + c + abs(maior1 - c)) / 2)
print(f'{maior2} eh o maior')
'''

'''
trip = int(input())
speed = int(input())

media = (trip * speed) / 12
print(f'{media:.3f}') 
'''


'''
arr = [99, 100, 240, 134, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in range(len(arr)):
  min_index = i
  for j in range(i+1, len(arr)):
    if arr[j] < arr[min_index]:
      min_index = j
  arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

arr = [99, 100, 240, 134, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in range(len(arr)):
  min_index = i
  for j in range(i+1, len(arr)):
    if arr[j] < arr[i]:
      min_index = j
  arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
'''



arr = [2,1,5,4,7,0,1,2,3,4,53,35,36,246,25,0]
for i in range(1,len(arr)):
    j = i
    while arr[j-1] > arr[j] and j>0:
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j -= 1
print(arr)

def mult(valor1, valor2): # tanto o valor 1 como o valor 2 são parametros
    return valor1 * valor2

mult(10, 20) # 10 e o 20 são argumentos


# tipagem dinamica e forte
#x = "olá"
#y = 2
#
#print(x + y)

velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print("Velocidade carro passou do radar 1")

if local_carro >= (LOCAL_1 - RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('Carro multado em radar 1')

#   Flag (bandeira) - Marcar um local
#   None = Não valor
#   is e is not = é ou nãp é (tipo, valor, identidade)
#   id = Identidade

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2)) # identidade do objeto, onde ele está na memória

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
a = 7.3
b = int(a)
print(b)

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite um numero inteiro: ")
# try:
#     num_int =  int(numero)
#     par_impar = num_int % 2 == 0
#     par_impar_text = 'impar'
# 
#     if par_impar:
#         par_impar_text = 'par'    
#     
#     print(f'O número {num_int} é {par_impar_text}')
# 
# except:
#     print("Não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horas = input("Que horas são: ")
# try:
#     horas_int = int(horas)
#     if 0 <= horas_int <= 11:
#         print("Bom Dia")
#     elif 12 <= horas_int <= 17:
#         print("Bom Tarde")
#     elif 18 <= horas_int <= 23:
#         print("Boa Noite")
#     else:
#         print("Fora do escopo")
# except:
#     print("Digite um número")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite o seu nome: ')
# tamanho_nome = len(nome)
# if tamanho_nome <= 4:
#     print('Seu nome é curto')
# elif 5 < tamanho_nome < 6:
#     print('Seu nome é normal')
# else:
#     print('Seu nome é muito grande')
 

"""
    https://docs.python.org/3/library/stdtypes.html
    Tipos build-in methods
"""

string = 'Osmar William'
outra_string = f'{string[:3]}ABC{string[4:]}'
print(outra_string) 
print(string.capitalize())
print(string.zfill(20))

"""
    Repetições
    While (enquanto)
"""

condicao = True
while condicao:
    print('Olá')
    break 
contador = 0
while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('não será mostrado o 6')
        continue
    if 10 <= contador <= 27:
        print('não será mostrado o ', contador)
        continue
    
    print(contador)

    if contador == 40:
        break

nome = 'osmar william'
tamanho_nome = len(nome)
contador = 0
novo_nome = ""
while contador < tamanho_nome:
    novo_nome += f'*{nome[contador]}'
    contador += 1
print(novo_nome)

""" While/else """

string = 'Valor qualquer'
i = 0
while i < len(string):
    letra = string[i]
    print(letra)
else:
    print("O else foi executado")

frase = "O Python é uma linguagem de programação" \
    'multiparadigma.'\
    'Python foi criado por Guildo van Rossum.'

i = 0
apareceu_mais_vezes = ...
letra_que_apareceu_mais_vezes = ...
while i < len(frase):
    letra_atual = frase[i]
    i += 1
