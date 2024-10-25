import random
def ocorrencia() -> float:
    vetor = []
    ocorrencia = 0
    for i in range(1000):
        vetor.append(random.randint(1,6))
        if vetor[i] == 6:
            ocorrencia += 1
    return ocorrencia / 1000 * 100

print(ocorrencia())

