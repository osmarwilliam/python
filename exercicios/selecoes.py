'''
(a) o total de faltas do campeonato
(b) o time que fez mais faltas
(c) o time que fez menos faltas
'''

lista = [['Brasil', 'Italia', [10, 9]], ['Brasil',
'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

faltas = 0
posicao = 2
mais_falta = lista[0][2][0]
mais_falta1 = lista[0][0]
menos_faltas = lista[0][2][0]
menos_faltas1 = lista[0][0]
for _ in range(3):
    for x in range(2):
        faltas += lista[_][2][x]
    for j in range(2):
        if mais_falta < lista[_][2][j]:
            mais_falta = lista[_][2][j]
            mais_falta1 = lista[_][j]
        if menos_faltas > lista[_][2][j]:
            menos_faltas = lista[_][2][j]
            menos_faltas1 = lista[_][j]
print(faltas)
print(mais_falta1)
print(menos_faltas1)