def somar(valor1, valor2): # Informa que a função precisa receber o valor da váriavel como parametro para poder executar o comando
    soma = valor1 + valor2
    print(soma)
    

valor1 = float(input('Insira o primeiro valor: ')) # Pede para inserir um valor que vai ser encaminhado para o parametro da função
valor2 = float(input('Insira o segundo valor: '))

somar(valor1,valor2)  ## Chama a função para ser executada.
