dinheiro, rodadas = map(int, input().split())
d, e, f = [dinheiro] * 3

def compra(pessoa : str, valor : int) -> None:
    if pessoa == "d":
        d -= valor
    if pessoa == "e":
        e -= valor
    else: 
        f -= valor
    

for _ in range(rodadas):
    items = input().split()
    if items[0] == 'C':
        if items[1] == "D":
            d -= int(items[2])
        elif items[1] == "E":
            e -= int(items[2])
        else: 
            f -= int(items[2])
    elif items[0] == 'V':
        if items[1] == "D":
            d += int(items[2])
        elif items[1] == "E":
            e += int(items[2])
        else: 
            f += int(items[2])
    else: 
        if items[1] == "D":
            d += int(items[3])
        elif items[1] == "E":
            e += int(items[3])
        else: 
            f += int(items[3])
print(f'{d} {e} {f}')