#entrada de tipo de combustivel e quantidade de litros
combustivel = input("Digite o tipo de combustível (E para etanol, G para gasolina): ")
litros = float(input("Digite o número de litros vendidos: "))

#logica de
if combustivel == 'G' or combustivel =='g':
    preco = 5.80
    print("voce escolheu gasolina")
if combustivel == 'E' or combustivel =='e':
    preco = 4.90
if combustivel != 'E' and combustivel != 'e' and combustivel != 'G' and combustivel != 'g':
    print("seu combustivel não é valido")

pagar = litros * preco
print(f"O valor a ser pago é R$ {pagar:.2f}")