#coleta de Tipo de combustivel
combustivel = input("Digite o tipo de combustível (E para etanol, G para gasolina): ")

#exclusão para aceitar apenas o 'E','e','G' e 'g'.
if combustivel != 'E' and combustivel != 'e' and combustivel != 'G' and combustivel != 'g':
    print("seu combustivel não é valido")
else:
#calculos de de valores de litros para cada tipo de combustivel
    if combustivel == 'G' or combustivel =='g':
            litros = float(input("Litro da Gasolina:5.80\n"
                                 "Digite o número de litros de gasolina sendo comprado: "))
            #calculo adicionado dentro do if
            pagar = litros * 5.80
            print(f"O valor a ser pago é R${pagar:.2f}")
    else:
            litros = float(input("Litro da Etanol:4.90\n"
                                 "Digite o número de litros de etanol sendo comprado: "))
            pagar = litros * 4.90
            print(f"O valor a ser pago é R${pagar:.2f}")
