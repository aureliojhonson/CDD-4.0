cadastro=[0]*10
senha=[0]*10
tamca=len(cadastro)
tent=0

operacao = 0
while operacao != 4:
    print("Selecione a operação:\n"
          "1. Cadastro.\n"
          "2. Mostrar.\n"
          "3. Login.\n"
          "4. Sair.\n")
    operacao = int(input("Escolha um numero: "))
    if operacao == 1:
        for a in range (tamca):
            cadastro[a]=input("Digite seu nome de Login: ")
            senha[a]=input("Digite seu nome de login: ")
#limite para a lista
            if a<tamca-1:
                continuar = input("Deseja cadastrar outro usuário? (s/n): ")
                if continuar != 's' or 'S':
                    break
            else:
                print("Limite de cadastro atingido.")
    if operacao == 2:
        for b in range (tamca):
            print(f"o usuario na posição {b}-{cadastro[b]} \n"
                  f"senha:{senha[b]}")
    if operacao == 3:
        for c in range(tamca):
            cadastro[c]=input("Digite seu nome de Login: ")
            senha[c]=input("Digite seu nome de login: ")
            if cadastro[c]==cadastro:
                cadastro[c]==tent

    if operacao == 4:
        print("Obrigado por usar o Programa")
    else:
        print("Opção inválida, tente novamente.")