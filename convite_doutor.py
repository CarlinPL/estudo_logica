### Doutor Henry vai convidar alunos com notas semestrais superiores a 8,5 programa deve solicitar o EMAIL e NOTA do Aluno

nota = float(input(' INSIRA A NOTA DO ALUNO : ')) # Pede a Nota do Aluno

email = input('INSIRA O EMAIL DO ALUNO : ')  # Pede o Email do Aluno 

if nota >= 8.5:    # Se nota for MAIOR ou IGUAL a 8.5
    print(f'Parabéns !, convite enviado para o email {email}')  # Emite o Parabens e é encaminhado o email para o aluno

else:
    print('Sinto Muito, sua nota não foi o suficiente') # Se não for MAIOR ou IGUAL a 8.5, informa que a nota não foi o suficiente.