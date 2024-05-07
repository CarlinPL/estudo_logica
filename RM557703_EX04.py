#Tipo de investimento que deseja realizar o resgate 1 para CDB / 2 para LCI / 3 para LCA
#Valor a ser resgatado
#Tempo em dias que o valor permaneceu investido
#Valor do imposto de Renda  
# Se o metodo de investimento for CDB cobrar IR

print("Selecione o Tipo de Investimento Desejado: \n 1 - Para CDB \n 2 - Para LCI \n 3 - Para LCA \n")
tipo_investimento = int(input("Digite o Tipo de Investimento :"))
valor_resgatado = float(input("Insira o valor a ser resgatado :"))
dias = int(input("Informe o tempo em dias em que o valor solicitado permaneceu investido : "))

if dias <= 180 and tipo_investimento == 1:
    print(f'O Valor resgatado foi de R$:{valor_resgatado - valor_resgatado * 22.5/100:.2f}')

elif dias >= 181 and dias <= 360 and tipo_investimento == 1:
    print(f'O Valor resgatado foi de R$:{valor_resgatado - valor_resgatado * 20/100:.2f}')

elif dias >= 361 and dias <= 720 and tipo_investimento == 1:
    print(f'O Valor resgatado foi de R$:{valor_resgatado - valor_resgatado * 17.5/100:.2f}')

elif dias > 720 and tipo_investimento == 1:
    print(f'O Valor resgatado foi de R$:{valor_resgatado - valor_resgatado * 15/100:.2f}')

elif tipo_investimento == 2:
    print(f'O Valor resgatado foi de R$:{valor_resgatado:.2f}')

elif tipo_investimento == 3:
    print(f'O Valor resgatado foi de R$:{valor_resgatado:.2f}')

elif tipo_investimento != 1 or 2 or 3 :
    print('O tipo de investimento selecionado não é válido')


