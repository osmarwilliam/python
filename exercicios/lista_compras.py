import os
def limpar():
    os.system('cls') or None


lista = []
while True:
    print("Selecione uma opção: ")
    opcao = input("[i]nserir [a]pagar [l]istar: ").lower()
    limpar()

    if opcao == 'i':
        valor = input('Digite o valor para adicionar: ')
        lista.append(valor)

    elif opcao == 'a':
        if lista == []:
            print('Nada para apagar')
        else:
            indice = input("Escolha o índice para apagar: ")
            try:
                indice = int(indice)
                del lista[indice]
            except ValueError:
                print("Por favor digite número int.")
            except IndexError:
                print("Por favor digite um index valido")
    elif opcao == 'l':
        if lista == []:
            print('Nada para listar')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
    else:
        print("Digite algum valor valido.")
 