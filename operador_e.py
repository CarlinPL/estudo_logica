# Uma loja concede descontos para compras a cima de 100 reais e pagas com cartao de crédito

valor_compra = float(input('Insira o valor do produto : '))  # Pede o Valor da compra

forma_pgmnt = input('Forma de pagamento\n 1 - Cartão de Crédito\n 2 - Dinheiro\n') # Pede a forma de Pagamento // o '/n' pula uma linha

if forma_pgmnt == '1' and valor_compra >= 100:  # Se a forma de pagamento for igual a CREDITO E a compra for de um valor MAIOR ou IGUAL a R$100

    valor_compra = valor_compra * 0.9 # Informa que eu retirei o 0,1 e quero apenas o 0,9 restante do número informado.
    print('Parabéns você ganhou um desconto de 10% ')  # Emite a mensagem de parabéns e é dado o desconto

elif forma_pgmnt == '2' and valor_compra >=100: # Porém se a forma de pagamento for igual a DINHEIRO e a compra for MAIOR ou IGUAL a R$100
    print('Você não ganhou o desconto, pois você pagou a compra em dinheiro') # Emite a mensagem que não foi dado o desconto, pois a forma de pagamento foi em dinheiro e não em crédito

elif valor_compra < 100:
    print('você não tem direito a desconto porque sua compra foi menor que R$100,00')


print(f'o valor da compra é {valor_compra}')


