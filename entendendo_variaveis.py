x = 10    # Dado inteiro
y = 30.3  # Dado Real
z = 'teste' # Dado String(STR) == Texto

print('o tipo da váriavel x é {}'.format(type(x))) # .Format faz com que o nome da váriavel apareça entre os '{}' na hora de ser printada

print('o tipo da váriavel x é ',type(x)) # Faz com que apareça na tela o tipo da váriavel

print('o tipo da váriavel y é {}'.format(type(y)))

print('o tipo da váriavel y é', type(y))

print('o tipo da váriavel z é {}' .format(type(z)))

print('o tipo da váriavel z é', type(z))


print(x)

x = float(x) # Transofrmou a  váriavel INT em FLOAT

print(x) # Printa o X como 10.0

print(type(x)) # Printa o X agora como número real/decimal == 10.0 

print(y)

y = int(y) ## Converte o número real/decimal em número inteiro // Quando feito isso o número após a virgula é ignorado

print(y)

print(type(y))

print(z)

print(len(z))  # imprime a quantidade de caracteres LEN = LENGHT(TAMANHO)

print(z.upper()) # Coloca todas os caracteres em letras maiúsculas
print(z.lower()) # Cooca todos os caracteres em letras mínusculas

print(z.split('s')) # Corta o texto ou letra que você deseja e declara entre as ASPAS