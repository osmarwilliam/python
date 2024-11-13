n = int(input())
secao = list(map(int, input().split()))

count = [0,0]
for i in range(len(secao)):
    count[0] += secao[i]

count[1] = count[0] / 2
count[0] = 0
for j in range(len(secao)):
    count[0] += secao[j]
    if count[1] == count[0]:
        print(j + 1)