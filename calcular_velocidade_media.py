def calcularVelocidadeMedia(distancia, tempo):

    velocidade_media = distancia / tempo    ### Não são todas as funções que precisam de return, somente se for necessário retoranr algo ao usuário.
    return velocidade_media


distancia = float(input('Insira a distância percorrida: '))
tempo = float(input('Insira o tempo que levou para percorrer a distância informada: '))

print(f'A velocidade média é de {calcularVelocidadeMedia(distancia, tempo)}Km/h')