#Colaborador precisa selecionar o dia da semana, seg / ter / quar / quin / sex 
#Exibir no final qual dia foi escolhido pelos colaboradores
#Verifique o número de colaboradores que irão participar da votação

colaboradores = int(input("Insira o número de colaboradores que irão participar da votação : "))

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

for colaboradores in range(colaboradores):
    print("Qual o melhor dia para a sua Live ? \n 1 para Segunda \n 2 para Terça \n 3 para Quarta \n 4 para Quinta \n 5 para Sexta \n")
    voto = int(input("Insira o voto do colaborador : "))

    if voto == 1:
        segunda = segunda + 1
    
    elif voto == 2:
        terca = terca + 1

    elif voto == 3:
        quarta = quarta + 1
    
    elif voto == 4:
        quinta = quinta + 1
    
    elif voto == 5:
        sexta = sexta + 1
    

print(f"Os votos para Segunda foram {segunda}, para Terça foram {terca}, para Quarta foram {quarta}, para Quinta foram {quinta}, para Sexta foram {sexta}")

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta :
    print('O dia da live será Segunda')

elif terca > segunda and terca > quarta and terca > quinta and terca > sexta :
    print('O dia da live será Terça')

elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta :
    print('O dia da live será Quarta')

elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta :
    print('O dia da live será Quinta')

elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta :
    print('O dia da live será Sexta')

else :
    print('Houve um empate nos votos')



  
