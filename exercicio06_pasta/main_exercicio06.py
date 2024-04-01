from exercicio06_criando_um_sistema_de_banco import Cliente, Banco, ContaCorrente, ContaPoupanca

# Criando algumas contas
conta_corrente1 = ContaCorrente(12345, 56789, 1000, 500)
conta_poupanca1 = ContaPoupanca(12345, 98765, 2000)
conta_corrente2 = ContaCorrente(12345, 12345, 1500, 700)
conta_poupanca2 = ContaPoupanca(12345, 54321, 3000)

# Criando alguns clientes com as contas criadas
cliente1 = Cliente("João", 123456789, 30, conta_corrente1)
cliente2 = Cliente("Maria", 987654321, 25, conta_poupanca1)
cliente3 = Cliente("Pedro", 456789123, 35, conta_corrente2)
cliente4 = Cliente("Ana", 654321987, 28, conta_poupanca2)

lista_clientes = [cliente1, cliente2, cliente3, cliente4]

banco = Banco(12345, lista_clientes)

def validacao_valores(valor: str) -> float|bool:

    try:

        valor_convertido = float(valor)
        return valor_convertido
    
    except:

        print("Valor inválido")
        return False



while True:

    print("Bem vindo ao sistema do banco.")
    opcao = input("Digite qualquer tecla para entrar ou Sair para sair: ").upper()

    if opcao == "SAIR":
        break

    cpf = input("Digite o seu cpf: ")
    numero_agencia = input("Insira o número da agência ")
    numero_conta = input("Digite o número da conta: ")
    
    try:

        cpf = int(cpf)
        numero_agencia = int(numero_agencia)
        numero_conta = int(numero_conta)

    except:

        print("Você não digitou números válidos em algum dos campos")
        continue
    
    cliente = banco.verificar_cliente_existe(cpf, numero_agencia, numero_conta)

    if not isinstance(cliente, Cliente):
        
        print("Não encontramos você em nosso banco de dados")
        continue

    print(f"Bem vindo {cliente.nome}")

    opcao = input("Digite a operação (sacar/depositar): ").upper()
    

    if opcao == "SACAR":

        valor = input("Digite um valor para sacar: ")

        valor_convertido = validacao_valores(valor)

        if not isinstance(valor_convertido, float):
            continue

        conta = cliente.conta

        saque_sucedido = conta.sacar(valor_convertido)

        if not saque_sucedido:

            print("Você não pode sacar este valor")
            continue

        print(f"saque sucedido, saldo atual: {conta.saldo}")


    elif opcao == "DEPOSITAR":

        valor = input("Digite um valor para sacar: ")

        valor_convertido = validacao_valores(valor)

        if not isinstance(valor_convertido, float):
            continue

        conta = cliente.conta

        saque_sucedido = conta.depositar(valor_convertido)

        print(f"Depósito sucedido, saldo atual: {conta.saldo}")

    else:

        print("Opção não digitada corretamente")
        continue 






    