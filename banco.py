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
    print('>>>>>>MENU<<<<<<')
    print('1. Cadastrar usuário')
    print('2. Depositar')
    print('3. Sacar')
    print('4. Transferir')
    print('5. Gerar extrato')
    print('6. Editar usuário')
    print('7. Sair')

    opcao = input('Digite a opção.')
        
    if opcao == '1':
        pass
        
    elif opcao == '2':
        pass
        
    elif opcao == '3':
        pedir_cpf = input('Infome seu CPF: ')
        valor_sacado = float(input('Digite o valor para ser sacado: '))
        sacar(pedir_cpf, valor_sacado)
        
    elif opcao == '4':
        valor_transf = float(input("Digite o valor a ser transferido: "))
        transferencia_origem = str(input('Digite seu CPF: '))
        transferencia_destino = str(input('Digite o CPF destino: '))
        
        transferir(transferencia_origem, transferencia_destino, valor_transf)

    elif opcao == '5':
        pass
        
    elif opcao == '6':
        pass
        
    elif opcao == '7':
        pass

    else:
        break
    