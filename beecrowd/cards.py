lista = input().split()
for i in range(5):
    lista[i] = int(lista[i])

def cards(lista):
    count = 0
    for i in range(4):
        if lista[i+1] > lista[i]:
            count += 1
            if count == 4:
                return 'C'
    count = 0            
    for i in range(4): 
        if lista[i + 1] < lista[i]:
            count += 1
            if count == 4:
                return 'D'
    else:
        return 'N'
    
print(cards(lista))