'''
    10. Faça um programa que calcule o número de
    dias corridos entre duas datas, para vários
    pares de datas, considerando a possibilidade de
    ocorrência de anos bissextos, sendo que:
        🞂 A primeira data é sempre a mais antiga
        🞂 O ano é fornecido com 4 dígitos
        🞂 A data fornecida com ZERO dias é o sinal para
        encerrar a entrada de dados
'''


def tempo(inicio, final):
    inicio_int = int(inicio)
    final_int = int(final)
    count = 0
    for i in range(inicio_int, final_int + 1):
        if i % 4 == 0:
            count += 366
        else: 
            count += 365
    return count

print(tempo(400, 2024))
