import calc  ## Chama um arquivo que queremos incorcoporar ao código, utiliazando as funções criadas no mesmo

a = input('Digite um valor: ')
b = input('Digite outro valor: ')

soma = calc.dividir(a,b)  # Necessário informar o nome do Módulo ponto o nome da função para que possa ser executada

print(f'A soma é {soma}')

# podemos também utilizar a opção FROM 'nome do Módulo' IMPORT 'noma da função'
# isso faz com que podemos informar qual função vamos usar e no momento que formos executar apenas digitar o nome da funçao. Sem ser necessário o uso do módulo.função
# Existe também a opção de importar todas as funções de uma vez, através do comando FROM 'nome_módulo' IMPORT * // porém devemos tomar cuidado ao importar tudo, para não ficarmos com um programa extremamente lento.