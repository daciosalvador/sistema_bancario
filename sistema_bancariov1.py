menu = """

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair

"""

saldo = 0
saque_diario = 500
num_saque = 0
extrato = ""
SAQUE_LIMITE = 3


while True:
    op = input(menu)
    
    if op == "1":
        valor = float(input("Valor do deposito:  "))        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {saldo:.2f}\n"
        else:
            print("Operação invalida!")
    elif op == "2":
        valor = float(input("Quanto deseja sacar? "))
        sem_saldo = valor > saldo
        sem_limite = valor > saque_diario
        limite_saque = num_saque >= SAQUE_LIMITE

        if sem_saldo:
            print("Você não tem saldo suficiente.")
        elif sem_limite:
            print(f"Valor excede o limite de saque diario no valor de R$ {saque_diario:.2f}.")
        elif limite_saque:  
            print("Quantidade de saques excedido.")    
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saque += 1           
        else:
            print("Valor informado invalido!")
    elif op == "3":
        sem_movimentacao = "Não foi realizado movimentações" if not extrato else extrato 
        print("--------- Extrato ---------")          
        print(sem_movimentacao)
        print(f"Saldo: {saldo:.2f}")
        print("--------- -------- ---------")
    elif op == "0":
        print("Sistema encerrado com sucesso!")
        break    
    else:
        print("Opção invalida!. Tente novamente")

    