idade = int(input('Insira a sua idade :')) # Pede para o Aluno informar a idade e converte em número Inteiro

rm = input('insira o seu RM :') # Pede para o aluno digitar seu RM e grava a informação em formato de texto

if idade >= 18 :  # Se idade for MENOR ou IGUAL a 18

    print(f'aluno do rm {rm}, sua inscrição foi aprovada') # Aprova a inscrição

else :  # Se não for MAIOR ou IGUAL anula a inscrição 
    print(f'aluno do rm {rm}, sua inscrição não foi aprovado, pois sua idade é menor de 18 anos')



