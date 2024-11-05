def notas(nota : int) -> str:
    if nota >= 86:
        return 'A'
    if nota >= 61:
        return 'B'
    if nota >= 36:
        return 'C'
    if nota >= 1:
        return 'D'
    return 'E'

print(notas(int(input())))