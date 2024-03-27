#Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
# Conta (ABC)
#     ContaCorrente
#     ContaPoupanca
# Pessoa (ABC)
#     Cliente
#         Clente -> Conta
# Banco
#     Banco -> Cliente
#     Banco -> Conta

from abc import ABC, abstractmethod


class Conta(ABC):
    """Classe abstrata de Contas de bancos
    
    Classe abstrata para configurara contas genéricas de um banco, o método 
    depositar deve ser feito nas classes específicas.
    """

    def __init__(self, numero_agencia: int, numero_conta: int, saldo: float|int) -> None:
        
        self._numero_agencia = numero_agencia 
        self._numero_conta = numero_conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor_saque: int|float) ->  bool: ... 

    def depositar(self, valor_depositado: float|int) -> None:

        self._saldo += valor_depositado

    @property
    def numero_agencia(self) -> int: 

        return self._numero_agencia


    @numero_agencia.getter
    def numero_agencia(self, novo_numero_agencia: int) -> None:

        self._numero_agencia = novo_numero_agencia


    @property
    def numero_conta(self) -> int: 

        return self._numero_conta


    @numero_conta.getter
    def numero_conta(self, novo_numero_conta: int) -> None:

        self._numero_conta = novo_numero_conta


    @property
    def saldo(self) -> int|float: 

        return self._saldo
    
    def __repr__(self) -> str:
        return f"{self.__dict__}"



class ContaCorrente(Conta):

    def __init__(self, numero_agencia: int, numero_conta: int, saldo: float | int, limite_extra_retirada: int|float) -> None:
        super().__init__(numero_agencia, numero_conta, saldo)
        self.__limite_extra_retirada = limite_extra_retirada

    def sacar(self, valor_saque: int|float) -> bool:

        saldo_com_limite_extra = self._saldo + self.__limite_extra_retirada

        if valor_saque <= saldo_com_limite_extra:

            self._saldo -= valor_saque

            return True

        return False        

    @property
    def limite_extra(self) -> int|float: 

        return self.__limite_extra_retirada


    @limite_extra.getter
    def limite_extra(self, novo_limite_extra: int) -> None:

        self.limite_extra_retirada =  novo_limite_extra



class ContaPoupanca(Conta):

    def sacar(self, valor_saque: int|float) -> bool:

        if valor_saque <= self._saldo:

            self._saldo -= valor_saque

            return True

        return False    
    


class Pessoa(ABC):

    def __init__(self, nome: str, cpf: int, idade: int) -> None:
       
       self._nome = nome
       self._cpf = cpf 
       self._idade = idade

    
    
    
    
    def __repr__(self) -> str:
        return f"{self.__dict__}"
    


conta = ContaCorrente(1234, 5584, 2000, 250)

print(conta)