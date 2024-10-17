'''Um número inteiro é considerado triangular se
este for o produto de 3 números inteiros
consecutivos, como, por exemplo, 120 = 4 x 5 x
6. Elabore um programa que, após ler um
número n do teclado, verifique se n é triangular'''
'''
import time

def triangular(intervalo):
    intervalo_int = int(intervalo)
    for i in range(intervalo):
        for x in range(1, int(i / 2)):
            if i == x * (x+1) * (x+2):
                print(f'{i} é um número triangular')

    return ''

inicio = time.time()
triangular(50000)

fim = time.time()
print(fim - inicio)
'''

# insertion sort
arr = [2,1,5,4,7,0,1,2,3,4,53,35,36,246,25,0]
for i in range(1,len(arr)):
    j = i
    while arr[j-1] > arr[j] and j>0:
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j -= 1
    
print(arr)
