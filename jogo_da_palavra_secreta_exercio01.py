"""
PROPOSTA:

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
    na palavra secreta; exiba _.
Faça a contagem de erros do seu
usuário.

"""
import random
import os

lista_de_palavras_secretas = ["python", "sql", "programar", "desenvolvedor", "javascript", "node"]

palavra_secreta = random.choice(lista_de_palavras_secretas)

chances_de_errar = len(palavra_secreta) // 2

quantidade_de_erros = 0

# Os tracinhos da forca quando a pessoa começa o jogo
tracinhos = "_" * len(palavra_secreta)

while True:

    print("Jogo da forca!", end="\n\n")

    print(f"quantidade de erros = {quantidade_de_erros}", end="\n")
    print(f"chances totais = {chances_de_errar}",  end="\n\n")

    print(tracinhos, end="\n\n")

    letra_digitada = input("Digite uma letra: ").lower()

    if not letra_digitada or len(letra_digitada) > 1:

        os.system("cls")
        print("Você não digitou uma letra!", end="\n\n")

        continue
    
    if letra_digitada in palavra_secreta:

        novos_tracinhos = ""

        for letra in palavra_secreta:

            if letra_digitada == letra or letra in tracinhos:
                
                novos_tracinhos+= letra
                continue

            novos_tracinhos+= "_"

        tracinhos = novos_tracinhos

        if tracinhos == palavra_secreta:

            os.system("cls")

            print(f"Parabéns você ganhou! a palavra era '{palavra_secreta}' ", end="\n\n" )
            continuar = input("deseja continuar: (Digite não para sair):").lower()

            if continuar == "não" or continuar == "nao":
                break
                 
            palavra_secreta = random.choice(lista_de_palavras_secretas)
            chances_de_errar = len(palavra_secreta) // 2
            quantidade_de_erros = 0
            tracinhos = "_" * len(palavra_secreta)
         
        os.system("cls")

    else:

        quantidade_de_erros += 1

        if quantidade_de_erros == chances_de_errar:

            os.system("cls")

            print(f"Você não acertou a palvra ele era '{palavra_secreta}' ", end="\n\n")
            continuar = input("deseja continuar: (Digite não para sair):").lower()

            if continuar == "não" or continuar == "nao":
                break
                 
            palavra_secreta = random.choice(lista_de_palavras_secretas)
            chances_de_errar = len(palavra_secreta) // 2
            quantidade_de_erros = 0
            tracinhos = "_" * len(palavra_secreta)


        os.system("cls")



    