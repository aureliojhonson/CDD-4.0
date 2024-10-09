cadastro = [0] * 5
senha = [0] * 5
tam = len(cadastro)

operacao = 0

while operacao != 4:
    print("Selecione a operação:\n"
          "1. Cadastro.\n"
          "2. Mostrar.\n"
          "3. Login.\n"
          "4. Sair.\n")
    operacao = int(input("Escolha um número: "))
#cadastro de usuarios
    if operacao == 1:
        for a in range (tam):
            if cadastro[a] == 0:
                cadastro[a]=input("Digite seu nome de Login: ")
                senha[a]=input("Digite sua senha: ")
            else:
                print("limite de cadastros no maximo")
                break
#mostrar cadastros em lista
    elif operacao == 2:
        for b in range(tam):
            if cadastro[b] != 0:
                print(f"Usuário na posição {b} - Nome: {cadastro[b]} \n"
                      f"Senha: {senha[b]}")
    elif operacao==3:

        nome = input("CADASTRO:")
        password = input("SENHA:")
        for c in range(tam):
            if cadastro[c] == nome and senha[c] == password:
                tentativa = 0

                while tentativa < 3 and senha[c] != password:
                    tentativa += 1
                    if tentativa < 3:
                        print("Senha Incorreta. Tente Novamente!!!")
                        password = input(f"{3 - tentativa} tentativas restantes - Informe a senha: ")
                if senha[c] == password:
                    print("Senha Correta.\n"
                          "Acesso Autorizado")
                    break
                else:
                    print("Número máximo de tentativas atingido. Essa conta será bloqueada!!!")

            else:
                print("Usuário não cadastrado.")
                break

#Fechar programa
    elif operacao == 4:
        print("Obrigado por usar o Programa")
    else:
        print("Opção inválida, tente novamente.")
