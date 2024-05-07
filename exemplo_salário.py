nome = input('Informe o nome do funcionário : ') # Pede o nome do funcionário

salário = float(input('Informe o salário do funcionário : ')) # Pede o salário do funcionário

if salário < 0 :  # Se salário for menor que 0

    salário = abs(salário) # ABS == transforma o número NEGATIVO em POSITIVO

    print(' O salário é negativo') # Imprime na Tela que é negativo

    print(f'o funcionário {nome} tem um salário de R$:{salário}')