vetor = []
pos = []
semdup = []
for i in range(20):
    print(f"Digite o valor para a posição {i}: ", end="")
    vetor.append(int(input()))
    if vetor[i] > 0:
        pos.append(vetor[i])

for i in range(len(pos)):
    if pos[i] not in semdup:
        semdup.append(pos[i])

print(vetor)
print(pos)
print(semdup)