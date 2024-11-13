import random 

vetor = [0] * 6
print()
for _ in range(len(vetor)):
    vetor[_] = random.randint(1,6)

qtd = [0] * 6

for i in range(1,7):
    count = 0
    if i in vetor:
        for j in range(6):
            if i == vetor[j]:
                count += 1 
    qtd[i - 1] = count

print(vetor)
print(qtd)