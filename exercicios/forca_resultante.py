"""
Faça um programa que leia dois vetores de 3 posições,
que representam forças sobre um ponto no espaço
3D, e escreva a força resultante
     Dica: força resultante é obtida pela soma dos valores das
    coordenadas correspondentes nos dois vetores: (x1 + x2),
(y1 + y2), (z1 + z2)
"""

vetor_1 = []
vetor_2 = []

def vetor_resultante(vetor_1, vetor_2):
    vetor = [0] * 3
    i = 0
    while i < 3:
        vetor[i] = vetor_1[i] + vetor_2[i]
        i += 1
    return vetor

verificador_flag = True
while verificador_flag:
    vetor_1 = input('Digite os valores para o primeiro vetor: ').split()
    vetor_2 = input('Digite os valores para o segundo vetor: ').split()
    if len(vetor_1) != 3 or len(vetor_2) != 3:
        print("Digite a três valores com espaço entre eles!")
        verificador_flag = True
        continue
    verificador_flag = False

for i in range(3):
    vetor_1[i] = float(vetor_1[i])
    vetor_2[i] = float(vetor_2[i])

vetor = vetor_resultante(vetor_1, vetor_2)
print(vetor)