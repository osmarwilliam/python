matriz_1 = [[1 , 2],
            [3, 4]] 

matriz_2 = [[1 , 2],
            [3, 4]]

matriz_3 = [[0 , 0],
            [0, 0]]


for i in range(2):
    for j in range(2):
        matriz_3[i][j] = matriz_2[i][j] + matriz_1[i][j]
print(matriz_3)