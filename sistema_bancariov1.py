menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cc] Criar Usuario
[c] Criar Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
conta = []


def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extratos(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def saque(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def criar_usuario(usuarios):

    nome = input("Digite nome: ")    
    cpf = input("Digite CPF: ")

    cpf_existe = False

    for user in usuarios:
        if user['cpf'] == cpf:
            cpf_existe = True
            break

    if cpf_existe:
        print("CPF Já Cadastro")
    else:
        clientes = {
            "nome": nome,
            "cpf": cpf
        }
    
        usuarios.append(clientes)

    return cpf

def criar_conta(conta, usuarios):
    cpf = criar_usuario(usuarios)

    n_conta = len(conta) + 1
        
    conta_corrente = {
        "n_conta" : n_conta,
        "agencia": "0001",
        "usuario": cpf
    }

    conta.append(conta_corrente)
    print(f"Conta {n_conta} criada para o usuário com CPF {cpf}.")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)       

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))        
        saldo, extrato = saque(valor=valor, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)     

    elif opcao == "e":
        extratos(saldo, extrato=extrato)

    elif opcao == "cc":
        criar_usuario(usuarios)

    elif opcao == "c":
        criar_conta(conta, usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")