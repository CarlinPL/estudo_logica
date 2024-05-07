pontos = int(input('Insira a sua pontuação')) # Pede a pontuação do cliente

if pontos >= 1000:    # Verifica se a pontuação é MAIOR OU IGUAL a 1000
    print('O cliente possui direito a mais 3Gbs de dados') 

elif pontos > 500:  # Verifica se a pontuação é MAIOR que 500
    print('O cliente possui direito a mais 1,5Gbs')

elif pontos > 200:  # Verifica se a pontuação é MAIOR que 200
    print('O cliente tem direito a mais 500Mbs')
            
else:  # Se os paramatros anteriores resultarem em falsos, é executado esse comando.
    print('O cliente não tem direito a nenhum bonus')