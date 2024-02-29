"""
Proposta
criar um gerador de cpfs

Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Para o segundo digito refaça a mesma coisa porém agora comece a multiplicação
"""

import os
import random 

def validar_decimo_digito_do_cpf(primeiros_9_numeros_do_cpf):

    primeiros_9_numeros_do_cpf_em_string = str(primeiros_9_numeros_do_cpf)

    contador = 10
    soma_dos_digitos = 0

    for numeros in primeiros_9_numeros_do_cpf_em_string:

        soma_dos_digitos += int(numeros) * contador
        contador -= 1

    multiplicacao_final_do_cpf = soma_dos_digitos * 10 

    decimo_digito_do_cpf = multiplicacao_final_do_cpf % 11

    return decimo_digito_do_cpf if decimo_digito_do_cpf <= 9 else 0


def validar_decimo_primeiro_digito_do_cpf(primeiros_10_numeros_do_cpf):
    
    primeiros_10_numeros_do_cpf_em_string = str(primeiros_10_numeros_do_cpf)

    contador = 11
    soma_dos_digitos = 0

    for numeros in primeiros_10_numeros_do_cpf_em_string:

        soma_dos_digitos += int(numeros) * contador
        contador -= 1

    multiplicacao_final_do_cpf = soma_dos_digitos * 10 

    decimo_digito_do_cpf = multiplicacao_final_do_cpf % 11

    return decimo_digito_do_cpf if decimo_digito_do_cpf <= 9 else 0


while True:

    print("Bem vindo ao gerador de CPFS !")

    opcao_digitada = input('Digite "gerar" para gerar para gerar um cpf "validar" para validar\
 um cpf ou "sair" para sair da aplicação: ').lower()

    if opcao_digitada == "sair":
        print("Adeus!")
        break

    elif opcao_digitada == "gerar":

        primeiros_9_numeros_do_cpf = random.random() * 1000000000

        primeiros_9_numeros_do_cpf = int(primeiros_9_numeros_do_cpf)

        decimo_digito = validar_decimo_digito_do_cpf(primeiros_9_numeros_do_cpf)

        primeiros_10_numeros_do_cpf = (primeiros_9_numeros_do_cpf * 10) + decimo_digito

        decimo_primeiro_digito = validar_decimo_primeiro_digito_do_cpf(primeiros_10_numeros_do_cpf)

        cpf_final = (primeiros_10_numeros_do_cpf * 10) + decimo_primeiro_digito

        os.system("clear")
        print(f"CPF gerado: {cpf_final}")

    elif opcao_digitada == "validar":

        os.system("clear")

        decimo_e_decimo_primeiro_digito = []
        primeiros_9_numeros_do_cpf = ""
        cpf_para_validar = input("Digite o cpf (apenas o numero): ")

        if ".- " in cpf_para_validar or len(cpf_para_validar) != 11:
            
            print("você não digitou o cpf no formato correto!")
            continue

        for indice, digito in enumerate(cpf_para_validar):

            if indice > 8:

                decimo_e_decimo_primeiro_digito.append(digito)

            else:

                primeiros_9_numeros_do_cpf += digito

        # 10 Digito que foi validado pelo sistema 
        decimo_digito_verdadeiro = validar_decimo_digito_do_cpf(int(primeiros_9_numeros_do_cpf))

        primeiros_10_numeros_do_cpf = primeiros_9_numeros_do_cpf + decimo_e_decimo_primeiro_digito[0]

        # 11 Digito que foi validado pelo sistema
        decimo_primeiro_digito_verdadeiro = validar_decimo_primeiro_digito_do_cpf(primeiros_10_numeros_do_cpf)

        cpf_validado = primeiros_9_numeros_do_cpf + str(decimo_digito_verdadeiro) + str(decimo_primeiro_digito_verdadeiro)

        if cpf_validado == cpf_para_validar: 
            
            print("CPF VALIDADO")

        else:

            print("CPF INVALIDO")

    else:
        
        os.system("clear")
        print("Você não digitou uma opção válida!")
        continue
