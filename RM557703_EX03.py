#Valor da divida 
#Taxa de Juros
#Número de parcelas para pagamento do empréstimo

valor_divida = float(input("Insira o valor o da dívida : "))

juros = 0
parcelas = 0

print(f"Total:R$ {valor_divida:.2f} Juros: R$ {juros} Numéro de parcelas: 1 Valor da Parcela: {valor_divida:.2f}")

juros = valor_divida * 0.05
for parcelas in range (3, 13, 3):
    juros += valor_divida * 0.05
    print(f"Total:R$ {valor_divida + juros:.2f} Juros: R$ {juros:.2f} Número de parcelas: {parcelas} Valor da Parcela : {(valor_divida + juros) / parcelas:.2f}")

