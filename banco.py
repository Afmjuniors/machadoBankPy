from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print("===================================================")
    print("=======================ATM=========================")
    print("===================Machado Bank====================")
    print("===================================================")

    print('Selecione uma opção do menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar deposito')
    print('4 - Efetuar transferencia')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    if opcao == 2:
        efetuar_saque()
    if opcao == 3:
        efetuar_deposito()
    if opcao == 4:
        efetuar_transferencia()
    if opcao == 5:
        listar_contas()
    if opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente')
    print('----------------------------')
    nome: str = input('Nome do cliente:')
    email: str = input('Email do cliente')
    cpf: str = input('CPF do cliente')
    data_nascimento: str = input('Data de nascimento do cliente')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criado com sucesso')
    print('Dados da conta')
    print('-----------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta'))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o numero {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da  conta'))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do deposito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com o numero {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o numero da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)
        if conta_o:
            numero_d: int = int(input('Informe o numero da conta de destino'))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da tranferencia'))

                conta_o.transferir(conta_d, valor)

            else:
                print(f'Não foi encontrada a conta de destino com o numero {numero_o}')
        else:
            print(f'Não foi encontrada a conta com o numero {numero_o}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Lista de contas')
        print('--------------------')
        for conta in contas:
            print(conta)
            print('--------------------')
            sleep(1)
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


if __name__ == '__main__':
    main()
