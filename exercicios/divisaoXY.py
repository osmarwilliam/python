def divisão_resto(x, y):
    quociente = 0
    resto = abs(x)
    while resto >= abs(y):
        resto -= abs(y)
        quociente += 1
    return quociente, resto

# def resto(x,y):
# valor = divisão(x,y)

quaciente, resto = divisão_resto(27,4)

print(f'o quociente é {quaciente}')
print(f'o resto é {resto}') 