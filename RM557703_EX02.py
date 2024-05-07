#Recebe o valor do carro
#Valor final
#Quantidades de parcelas
#Valor das parcelas

# Compra a viste tem 20% de desconto
#Quantidades de parcela 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60

valor_carro = float(input('Insira o valor total do carro : '))
desconto = valor_carro * 0.2

print(f'O preço final á vista com desconto de 20% é : {valor_carro - desconto}')

juros = 0.03

for parcela in range (6, 61, 6):
    valor_final = valor_carro * (1 + juros)
    juros = juros + 0.03
    print(f'O preço final parcelado em {parcela}X é de {valor_final:.2f} com parcelas de {valor_final / parcela:.2f}')