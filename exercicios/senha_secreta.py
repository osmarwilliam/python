"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

senha_secreta = "perfume"
senha_teste =  "*" *  len(senha_secreta)
letra = input()
for i in range(len(senha_secreta)):
    if letra == senha_secreta[i]:
        senha_teste = list(senha_teste)
        senha_teste[i] = letra
        senha_teste = "".join(senha_teste)
print(senha_teste)