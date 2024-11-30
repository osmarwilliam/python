import os

def get_str_input(prompt: str) -> str:
    while True:
        user_input = input(prompt)
        if user_input.isalpha() == True:
            return user_input
        else:
            print("Digite um valor válido!!")
    
def get_letra_input(letra: str) -> str:
    while True:
        user_input = input(letra)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print('Digite uma letra válida!') 

def verificar_letra(letra : str, palavra : str, palavra_secreta : str):
    flag = False
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            palavra = list(palavra)
            palavra[i] = letra
            palavra = "".join(palavra) 
            flag = True 
    return flag, palavra

def desenho_forca(erros: int, palavra : str):
    estagios = [
        f"""
           ------
           |    |
                |
                |
                |
                |
        {palavra_escondida}
        """,
        f"""
           ------
           |    |
           O    |
                |
                |
                |
        {palavra_escondida}
        """,
        f"""
           ------
           |    |
           O    |
           |    |
                |
                |
        {palavra_escondida}
        """,
        f"""
           ------
           |    |
           O    |
          /|    |
                |
                |
        {palavra_escondida}
        """,
        f"""
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        {palavra_escondida}
        """,
        f"""
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        {palavra_escondida}
        """,
        f"""
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        {palavra_escondida}
        """,
    ]
    print(estagios[erros])




palavra_secreta = get_str_input("Digite a palavra secreta (não deixe o amiguinho vê-la): ")
palavra_escondida = "_" * len(palavra_secreta)
os.system('clear') or None
print("Palavra armazenada com sucesso!!")

tentativas = 0
max_tentativas = 6

print(f'A partir de agora voce tem {max_tentativas} tentativas para acertar!')
while palavra_secreta != palavra_escondida:

    letra = get_letra_input("Digite uma letra: ")
    flag, palavra_escondida = verificar_letra(letra, palavra_escondida, palavra_secreta)
    if flag == True:
        pass
    else:
        max_tentativas -= 1
        tentativas += 1
        print(f'Alternativa incorreta, tentativas restantes: {max_tentativas}')

    if tentativas == 6:
        print(f"Você perdeu. A palavra era: {palavra_secreta}")
        break
    desenho_forca(tentativas, palavra_escondida)

    if palavra_escondida == palavra_secreta:
        print("Você venceu, parabéns!!!")
    