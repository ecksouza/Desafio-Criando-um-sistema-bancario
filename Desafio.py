menu = """

[1] Depositar
[2] Sacar
[5] Extrato
[4] Saldo
[0] Sair

=> """

saldo = 1800
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuario = "Erick"

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0 and valor <= 1000:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Você depositou R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido ou excede o limite de R$ 1000,00.")
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
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
        print(f"Saque de R$ {valor:.2f} realizado com sucesso")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato, usuario):
    print(f"\n================ EXTRATO - {usuario} ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def exibir_saldo(saldo):
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
    elif opcao == "5":
        exibir_extrato(saldo, extrato, usuario)
    elif opcao == "4":
        exibir_saldo(saldo)
    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")