n, media = map(int, input().split())
alturas = list(map(int, input().split()))

count = 0
while (min(alturas) != media) or (max(alturas) != media):
    menor = min(alturas)
    maior = max(alturas)
    if menor < media:
        count += 1
        flag = 0
        for j in range(len(alturas)):
            if alturas[j] < media:
                alturas[j] += 1
                flag += 1
                if flag == 2:
                    break
            
    if maior > media:
        count += 1
        flag = 0
        for j in range(len(alturas)):
            if alturas[j] > media:
                alturas[j] -= 1
                flag += 1
                if flag == 2:
                    break
print(count)

'''
total = 0
for i in range(1, n):
    if media >= alturas[i - 1]:
        alturas[i] += media - alturas[i - 1]
    else:
        alturas[i] -= alturas[i - 1] - media
    total += abs(media - alturas[i - 1])
print(total)
'''