num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = 0
while operacao != 6:
    print("Selecione a operação:\n"
          "1. Para soma.\n"
          "2. Para subtração.\n"
          "3. Para multiplicação.\n"
          "4. Para divisão.\n"
          "5. Para digitar novos números.\n"
          "6 Para sair")
    operacao = int(input("Escolha um numero: "))
    if operacao == 1:
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")
    elif operacao == 2:
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    elif operacao == 3:
        resultado = num1 * num2
        print(f"Resultado da multiplicacao: {resultado}")
    elif operacao == 4:
        resultado = num1 / num2
        print(f"Resultado da divisao: {resultado}")
    elif operacao == 5:
        num1 = float(input("Digite o novo primeiro número: "))
        num2 = float(input("Digite o novo segundo número: "))
    elif operacao == 6:
        print("obrigado pro usar o programa")
    else:
        print("Opção inválida, tente novamente.")
