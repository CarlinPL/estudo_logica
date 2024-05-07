trap = ['Derek', 'Veigh', 'Teto', 'Wiu'] # Armazena várias informaçoes à variável

print(trap)
trap.append('Vino') # Adiciona um valor na ultima posição da minha lista
print(trap)

trap.append(input('Digite o nome do seu trapper Favorito: ')) # Permie que o usuário digite/ adicione um valor à lista

for nome in trap:  # Exibe em sequencia as informações á variáveis
    print(nome)

# APPENDE sempre cria um novo espaço no final da lista e adiciona o elemento