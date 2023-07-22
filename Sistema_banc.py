
deposito = 0
saldo = 0
saque = 0
operacao = 3
total_de_saques = 0
numero_de_saques = 0
total_de_depositos = 0
numero_de_depositos = 0

while True:
    menu = int(input("""
Sistema bancário, operações:
    [1] Depósito   
    [2] Saque
    [3] Extrato
    [4] Sair
Qual você quer realizar? """))


    if menu == 1:
        while True:
            deposito += float(input("\ndigite o valor do depósito: "))

            if deposito <= 0:
                print("\nNão é possível realizar este depósito\nTente novamente!")
                break
            
            saldo += deposito
            numero_de_depositos += 1
            total_de_depositos += deposito

            print(f"\nDepósito realizado com sucesso!\nSeu saldo atual é R${saldo:.2f}\n")
            break

        while True:    
            nova_operacao = input("""
Deseja realizar outra operação?
    [S] Sim                       
    [N] Não
Sua resposta: """)

            if nova_operacao == "S" or nova_operacao == "s":
                break
            elif nova_operacao == "N" or nova_operacao == "n":
                break
            else:
                print("\nTente novamente")


    elif menu == 2:
        while True:

            if operacao == 0:
                print("\nVocê ja atingiu o limite de saques por hoje.")
                break

            print(f"\nSeu limite de saque é de R$500 por operação e você ainda pode realizar {operacao} operações de saque!\n")

            saque = float(input("Quanto Você deseja sacar? "))

            if saque <= 0.0:
                print("\nNão é possível realizar este saque.\nTente novamente!")
                break

            elif saque > saldo:
                print("\nNão é possível realizar este saque por falta de saldo.\nTente novamente!")
                break
            
            elif saque > 500:
                print("\nNão é possível realizar saques acima de R$500.00!")
                break

            saldo -= saque
            operacao -= 1
            numero_de_saques += 1
            total_de_saques += saque

            print(f"\nO saque de R${saque:.2f} foi realizado com sucesso!, seu saldo agora é R${saldo:.2f}")
            print(f"Você ainda tem {operacao} operações de saque disponíveis por hoje.")
            break
        
        while True:    
            nova_operacao = input("""
Deseja realizar outra operação?
    [S] Sim                       
    [N] Não
Sua resposta: """)

            if nova_operacao == "S" or nova_operacao == "s":
                break
            elif nova_operacao == "N" or nova_operacao == "n":
                break
            else:
                print("\nTente novamente")



    elif menu == 3:
        print("Extrato".center(15, "="))
        print(f"""
Depósitos:
Número de depósitos = {numero_de_depositos}
Valor dos depósitos = {total_de_depositos}

Saques:
Número de saques = {numero_de_saques}
Valor dos saques = {total_de_saques}  

Saldo atual = {saldo}
""")
        
        while True:    
            nova_operacao = input("""
Deseja realizar outra operação?
    [S] Sim                       
    [N] Não
Sua resposta: """)

            if nova_operacao == "S" or nova_operacao == "s":
                break
            elif nova_operacao == "N" or nova_operacao == "n":
                break
            else:
                print("\nTente novamente")


    elif menu == 4:
        break

    else:
        print("""
    tente novamente
                    """)
    

    if nova_operacao == "N" or nova_operacao == "n":
        break
    