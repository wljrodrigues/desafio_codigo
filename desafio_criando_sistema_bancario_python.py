def criar_usuario():
    nome = input("Informe o nome do cliente: ")
    while True:
        cpf = input("Informe o CPF do cliente (apenas números): ")
        if cpf.isdigit():
            break
        else:
            print("CPF inválido. Por favor, informe apenas números.")
    return {"nome": nome, "cpf": cpf}

def criar_conta_corrente(usuario):
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    return {"usuario": usuario, "saldo": saldo, "limite": limite, "extrato": extrato, "numero_saques": numero_saques, "LIMITE_SAQUES": LIMITE_SAQUES}
    

def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= conta["LIMITE_SAQUES"]
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def visualizar_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

def listar_contas(contas):
    print("\n================ CONTAS DE USUÁRIOS ================")
    for i, conta in enumerate(contas, 1):
        print(f"{i}. Nome: {conta['usuario']['nome']}, CPF: {conta['usuario']['cpf']}, Saldo: R$ {conta['saldo']:.2f}")
    print("=====================================================")

def deletar_conta(contas):
    listar_contas(contas)
    if contas:
        indice = int(input("Informe o número da conta que deseja deletar: "))
        if 1 <= indice <= len(contas):
            del contas[indice - 1]
            print("Conta deletada com sucesso.")
        else:
            print("Índice inválido.")
    else:
        print("Não há contas para deletar.")

def menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Contas
[x] Deletar Conta
[q] Sair

=> """

def main():
    contas = []
    
    while True:
        if not contas:
            print("Não existe contas cadastradas. Crie a primeira no sistema. Sua conta de acesso será: 1")
            opcao = input("Deseja criar uma conta agora? (s/n): ").lower()
            if opcao == "s":
                usuario = criar_usuario()
                conta = criar_conta_corrente(usuario)
                contas.append(conta)
            else:
                break

        else:
            conta_atual = None
            num_conta = input("Informe o número da sua conta para acessar ou digite 'c' para criar uma nova conta: ")
            
            if num_conta.lower() == "c":
                usuario = criar_usuario()
                conta_atual = criar_conta_corrente(usuario)
                contas.append(conta_atual)
            else:
                try:
                    num_conta = int(num_conta)
                    if 1 <= num_conta <= len(contas):
                        conta_atual = contas[num_conta - 1]
                      
                except ValueError:
                    pass
                
            if not conta_atual:
                print("Conta inválida.")
            else:                
                while True:
                    print("Conta criada com sucesso! Seu número de conta é:", len(contas))
                    opcao = input(menu())
                    if opcao == "d":
                        depositar(conta_atual)
                    elif opcao == "s":
                        sacar(conta_atual)
                    elif opcao == "e":
                        visualizar_extrato(conta_atual)
                    elif opcao == "l":
                        listar_contas(contas)
                    elif opcao == "x":
                        deletar_conta(contas)
                    elif opcao == "q":
                        break
                    else:
                        print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
