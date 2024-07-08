# Dicionário para armazenar usuários
usuarios = {}

# Dicionário para armazenar contas correntes
contas = {}

def cadastrar_usuario(nome, cpf):
    if cpf in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[cpf] = {"nome": nome, "cpf": cpf}
        contas[cpf] = {"saldo": 0.0, "extrato": []}
        print(f"Usuário {nome} cadastrado com sucesso.")

def depositar(cpf, valor):
    if cpf in contas:
        contas[cpf]["saldo"] += valor
        contas[cpf]["extrato"].append(f"Depósito: +R${valor:.2f}")
    else:
        print("Usuário não encontrado.")

def sacar(cpf, valor):
    if cpf in contas:
        if valor > contas[cpf]["saldo"]:
            print("Saldo insuficiente.")
        else:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["extrato"].append(f"Saque: -R${valor:.2f}")
    else:
        print("Usuário não encontrado.")

def transferir(cpf_origem, cpf_destino, valor):
    if cpf_origem in contas and cpf_destino in contas:
        if valor > contas[cpf_origem]["saldo"]:
            print("Saldo insuficiente para transferência.")
        else:
            contas[cpf_origem]["saldo"] -= valor
            contas[cpf_destino]["saldo"] += valor
            contas[cpf_origem]["extrato"].append(f"Transferência enviada: -R${valor:.2f} para {usuarios[cpf_destino]['nome']}")
            contas[cpf_destino]["extrato"].append(f"Transferência recebida: +R${valor:.2f} de {usuarios[cpf_origem]['nome']}")
    else:
        print("Usuário de origem ou destino não encontrado.")

def gerar_extrato(cpf):
    if cpf in contas:
        print(f"Extrato da conta de {usuarios[cpf]['nome']} (CPF: {usuarios[cpf]['cpf']}):")
        for item in contas[cpf]["extrato"]:
            print(item)
            print(f"Saldo atual: R${contas[cpf]['saldo']:.2f}")
    else:
        print("Usuário não encontrado.")

def editar_usuario(cpf):
    if cpf in usuarios:
        novo_nome = input("Digite o novo nome: ").strip()
        usuarios[cpf]['nome'] = novo_nome
        print(f"Dados do usuário {cpf} atualizados para: {usuarios[cpf]}")
    else:
        print("Usuário não encontrado.")


while True:

    print("""MENU:
         1 - Cadastrar usuário
         2 - Depositar
         3 - Sacar
         4 - Transferir
         5 - Gerar extrato
         6 - Editar usuário
         7 - Fechar conta
         8 - Consultar saldo
         9 - Sair""")
    opc = int(input("Escolha a opção:"))
    if opc == 1:
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o seu CPF: ")
        cadastrar_usuario(nome, cpf)
    elif opc == 2:
        cpf = input("Digite o CPF do usuário: ")
        valor = float(input("Digite o valor do depósito: "))
        depositar(cpf, valor)
        print(f"Deposito de {valor}R$ efetuado com sucesso!")
       #print(contas[cpf]["saldo"])
    #elif opc == 3:
    
    #elif opc == 4:
    
    #elif opc == 5:
    
    #elif opc == 6:
    
    #elif opc == 7:
    
    #elif opc == 8:
    
    #elif opc == 9:
    
    #else:
    #print("Escolha uma opção válida!")