#Dados os valores de horários abaixo, decifre a lógica e faça
#um código para executar.
#entrada01: 3:45
#entrada02: 14:20
#saída: 6:05

hora1=int(input("Informe o valor da hora: "))
minuto1=int(input("Informe o valor da minuto: "))
hora2=int(input("Informe o valor da hora: "))
minuto2=int(input("Informe o valor da minuto: "))

minutosoma=minuto1+minuto2
horasoma=(hora1+hora2)*60
minutototal=minutosoma+horasoma

#min//60 vai pegar todos os minutos e transformar em horas usando o resutado e o
# %12 vai usar o resto para definir em um limite de 12 no caso de 24:12
horafinal=(minutototal//60)%12

#vai usar o resto para pegar os minutos
minfinal=minutototal%60

print(f"Saida as :{horafinal:02d}:{minfinal:02d}")