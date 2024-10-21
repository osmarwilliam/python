'''
Faça um programa para calcular a série de
Fibonacci para um número informado pelo

usuário, sendo F(0) = 0, F(1) = 1 e F(n)= F(n-
1)+F(n-2)

🞂 Por exemplo, caso o usuário informe o número 9, o
resultado seria:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''

def seq_fibonacci(num):
    f0 = 0
    f1 = 1
    fn = 0
    count = 0
    if f0 == 0:
        print(f0)
        count+= 1
    if f1 == 1:
        print(f1)
        count+= 1
    
    while count <= num:
        fn = f0 + f1
        print(fn)
        f0 = f1
        f1 = fn
        count +=1
    return ''

print(seq_fibonacci(150))