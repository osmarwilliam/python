dinheiro, rodadas = map(int, input().split())
d, e, f = [dinheiro] * 3
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
            if items[2] == "F":
                f -= int(items[3])
            elif items[2] == "E":   
                e -= int(items[3])
        elif items[1] == "E":
            e += int(items[3])
            if items[2] == "F":
                f -= int(items[3])
            elif items[2] == "D":   
                d -= int(items[3])
        elif items[1] == "F": 
            f += int(items[3])
            if items[2] == "D":
                d -= int(items[3])
            elif items[2] == "E":   
                e -= int(items[3])
        
print(f'{d} {e} {f}')