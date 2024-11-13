lista = []
for i in range(300):
    lista.append(i)

print(lista)
proximo_id = len(lista) + 1
for _ in range(len(lista) - 1,0, -1):
    confirmacao = input(f'Responsavel com id {_}, voce gostaria de continuar'
                        'na fila? (S/N): ')
    if confirmacao.lower() == 'n':
        lista.pop(_)
        lista.append(proximo_id)
        proximo_id += 1
print(lista)