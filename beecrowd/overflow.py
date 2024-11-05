def overflow(largest_number : int) -> None:
    valores = input().split()
    num1, num2, operator  = int(valores[0]), int(valores[2]), valores[1]
    result = num1 + num2 if operator == "+" else num1 * num2
    print('OK' if result <= largest_number else 'OVERFLOW')

overflow(int(input()))