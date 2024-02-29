import random
import os

def printar_perguntas_e_opcoes(pergunta_para_responder):

    print("pergunta:", pergunta_para_responder["pergunta"])
        
    for indice, opcao in enumerate(pergunta_para_responder["opcoes"], start=1):

        print(f"{indice}. {opcao}")


def verificar_resposta(pergunta_para_responder, resposta_usuario):
        
    try:
        resposta_usuario = int(resposta_usuario)

    except:

        print("Você não digitou um valor!")
        return None
    

    if resposta_usuario < 1 or resposta_usuario > 4:
        print("Você não digitou uma opção válida!")
        return None

    resposta_correta = pergunta_para_responder["resposta"]

    indice_da_resposta_correta = (pergunta_para_responder["opcoes"].index(resposta_correta) + 1)

    return True if indice_da_resposta_correta == resposta_usuario else False

while True:

    perguntas_respostas = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": ["Rio de Janeiro", "São Paulo", "Brasília", "Belo Horizonte"],
            "resposta": "Brasília"
        },
        {
            "pergunta": "Quem escreveu 'Dom Quixote'?",
            "opcoes": ["William Shakespeare", "Miguel de Cervantes", "Charles Dickens", "Johann Wolfgang von Goethe"],
            "resposta": "Miguel de Cervantes"
        },
        {
            "pergunta": "Qual é o maior planeta do Sistema Solar?",
            "opcoes": ["Terra", "Júpiter", "Saturno", "Marte"],
            "resposta": "Júpiter"
        },
        {
            "pergunta": "Qual é o elemento químico representado pelo símbolo 'H'?",
            "opcoes": ["Hélio", "Hidrogênio", "Carbono", "Oxigênio"],
            "resposta": "Hidrogênio"
        },
        {
            "pergunta": "Quem pintou a Mona Lisa?",
            "opcoes": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "resposta": "Leonardo da Vinci"
        }
    ]

    qtd_de_perguntas = len(perguntas_respostas)
    contador_de_acertos = 0

    print("Bem vindo ao teste de conhecimentos gerais!", end="\n\n")

    iniciar_teste = input("Digite qualquer coisa para começar ou [S]air para sair: ", ).upper()
    print()
    
    if iniciar_teste == "S":
        print("Adeus!")
        break
    
    while perguntas_respostas:

        pergunta_para_responder = random.choice(perguntas_respostas)

        printar_perguntas_e_opcoes(pergunta_para_responder)

        resposta_usuario = input("Digite uma resposta: ")

        resposta_validada = verificar_resposta(pergunta_para_responder, resposta_usuario)

        if resposta_validada is None:

            os.system("cls")
            print("Você não digitou algo válido")
            continue

        elif resposta_validada == True:

            os.system("cls")

            print("Resposta Correta!")
            contador_de_acertos+= 1

        else:

            os.system("cls")

            print("Resposta Incorreta!")

        perguntas_respostas.remove(pergunta_para_responder)


    print(f"Parabéns você acertou {contador_de_acertos} de {qtd_de_perguntas}")

        