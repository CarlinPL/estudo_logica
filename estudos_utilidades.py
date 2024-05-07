#valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]

print(f"A lista foi criada assim: {valores}") # Exibe os valores da lista

contagem = valores.count(7) # Conta quantas vezes o elemento específicado entre parenteses aparece na lista
print(f"Nessa lista o número 7 aparece {contagem} vezes")

valores.reverse() # Inverte a lista de trás para frente
print(f"A lista agora está invertida: {valores}")

valores.sort() # Ordena a lista em ordem Crescente / OU / Ordem alfabética caso os valores atribuidos sejam textos
print(f"A lista agora está ordenada: {valores}")