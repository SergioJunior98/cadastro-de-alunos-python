# ------------------------------------------------------------------------------------------
############################################################################################
# ------------------------ CRIADOR: SERGIO LUCIO DE OLIVEIRA JUNIOR ------------------------
############################################################################################
# ------------------------------------------------------------------------------------------


import sqlite3
escolha = 0

cursos = ['Análise e Desenvolvimento de Sistemas',
          'Ciência da Computação',
          'Redes de Computadores',
          'Defesa Cibernética',
          'Gestão de TI']

def sair_do_programa():
    print("Saindo...")
    exit()


# Cria a conexão com o banco de dados
conexao = sqlite3.connect("Banco de Dados de Alunos.db")
cursor = conexao.cursor()  # Define o Cursor para dar entrada com o banco


def cadastro_aluno():

    # Declara que o nome é invalido para entrar no loop do While
    nomeValido = False

    # Faz o loop para verificar se o nome é valido e não sai enquanto não for um nome válido
    while nomeValido == False:

        # Sempre declara e limpa a lista
        lista_caracteresinvalidos = []

        # Pergunta ao usuário qual o nome do aluno
        nomeAluno = input("Digite o nome do aluno: ")
        # Temporáriamente o nome é tratado como válido, ainda irá passar pela conferência de segurança de nenhum caractere inválido
        nomeValido = True

        # Ajusta o nome do aluno com primeira Maiúscula e restantes minúsculas
        novoNome = ""
        palavras = nomeAluno.split()

        for i, palavra in enumerate(palavras):
            if i == len(palavras) - 1:
                novoNome += palavra.capitalize()
            else:
                novoNome += palavra.capitalize() + " "

        nomeAluno = novoNome

        # Percorre por cada caractere do nome do aluno digitado
        for caractere in nomeAluno:
            # Se não for alfabética
            if not caractere.isalpha() and not caractere.isspace():
                # Adiciona o caractere inválido à lista de caracteres inválidos
                lista_caracteresinvalidos.append(caractere)
                # Declara que o nome não é válido
                nomeValido = False
        if nomeAluno == "":
            nomeValido = False
            print('Nome não pode ser nulo. Tente novamente!')

        # Se não for um nome válido
        if not nomeValido == True and nomeAluno != "":
            print("Você digitou um nome com caractere(s) invalido(s):")
            # percorre por cada caractere dentro da lista de caracteres inválidos
            for caractere in lista_caracteresinvalidos:
                # Se for o último caractere, finaliza com "." (ponto)
                if lista_caracteresinvalidos.index(caractere) == len(lista_caracteresinvalidos)-1:
                    # Exibe o último caractere e "."
                    print(f"{caractere}.")
                # Se não for o último caractere
                else:
                    # Exibe o caractere percorrido e adiciona vírgula e espaço, finalizando com end="" para não pular linha e mostrar os caracteres em um única linha para o usuário
                    print(f"{caractere}, ", end="")
            # Exibe a mensagem para uma nova tentativa.
            print('Tente novamente!')

    # Declara a idade como 0 para entrar no loop de verificação
    idadeAluno = 0
    # Enquanto idade for 0 faça o loop de verificação
    while idadeAluno == 0:
        # Tente receber a idade
        try:
            # Recebe a idade
            idadeAluno = int(
                input(f"Digite a idade de {nomeAluno} (Somente números): "))
            # Se não é igual ou maior que 16 e menor ou igual à 65
            if not idadeAluno >= 16 or not idadeAluno <= 65 or idadeAluno == "":
                # Reseta a idade para continuar no loop
                idadeAluno = 0
                # Exibe a mensagem de erro e pede para tentar novamente
                print(
                    "Você não digitou uma idade válida (Entre 16 e 65 anos). Tente novamente!")
        # Caso não recebe uma idade com valor em inteiro
        except:
            # Trata o erro mostrando a mensagem que a idade não é válida e pede para tentar novamente
            print("Você não digitou uma idade válida. Tente novamente!")

    # Turma do Aluno
    turmaAluno = input("Digite a turma do aluno:")

    raAluno = input("Digite o RA do aluno:")

    print("=" * 20)
    print(f"{'CURSOS':=^20}")
    for id, curso in enumerate(cursos):
        print(f"[{id}] - {curso}")
    escolhaCurso = -1
    while escolhaCurso < 0 or escolhaCurso > 4:
        try:
            escolhaCurso = int(input("Digite o número do curso: "))
            if (escolhaCurso < 0 or escolhaCurso > 4):
                escolhaCurso = -1
                print("Digite um número entre 0 e 4. Tente novamente!")
        except:
            escolhaCurso = -1
            print("Digite um número válido.")

    cursoAluno = cursos[escolhaCurso]

    nota1 = -1
    while nota1 < 0 or nota1 > 10:
        try:
            nota1 = float(input("Digite a nota da NP1: "))
            if nota1 < 0 or nota1 > 10:
                nota1 = -1
                print("Digite uma nota entre 0 e 10. Tente novamente!")
        except:
            nota1 = -1
            print("Digite uma nota válida. Tente novamente.")
    nota2 = -1
    while nota2 < 0 or nota2 > 10:
        try:
            nota2 = float(input("Digite a nota da NP2: "))
            if nota2 < 0 or nota2 > 10:
                nota2 = -1
                print("Digite uma nota entre 0 e 10. Tente novamente!")
        except:
            nota2 = -1
            print("Digite uma nota válida. Tente novamente.")

    notaPIM = -1
    while notaPIM < 0 or notaPIM > 10:
        try:
            notaPIM = float(input("Digite a nota do PIM: "))
            if notaPIM < 0 or notaPIM > 10:
                notaPIM = -1
                print("Digite uma nota entre 0 e 10. Tente novamente!")
        except:
            notaPIM = -1
            print("Digite uma nota válida. Tente novamente.")

    mediaSemestral = (nota1*4 + nota2*4 + notaPIM *2) / 10
    # Exibe no console o nome e a idade
    print(f"Inserindo o aluno:\n"
          f"Nome: {nomeAluno} | Idade: {idadeAluno} | Turma: {turmaAluno} | RA: {raAluno} | Curso: {cursoAluno} | Nota NP1: {nota1} | Nota NP2: {nota2} | Nota PIM: {notaPIM} | Media: {mediaSemestral}")

    cursor.execute(
        f" INSERT INTO ALUNOS ( NOME, IDADE, TURMA, RA, CURSO, NP1, NP2, PIM, MEDIA) VALUES ('{nomeAluno}', {idadeAluno}, '{turmaAluno}', '{raAluno}', '{cursoAluno}', {nota1}, {nota2}, {notaPIM}, {mediaSemestral});")
    print("Aluno inserido. Salvando...")
    conexao.commit()  # Aqui faz o salvamento
    print("Salvamento concluído.")

    inicio_programa()


def consulta_banco():
    cursor.execute(" SELECT * FROM ALUNOS ")
    resultado = cursor.fetchall()

    if not resultado:
        print("Nenhum aluno cadastrado.\n")
        inicio_programa()
        return

    espacamentoID = 2
    espacamentoNome = 4
    espacamentoIdade = 5
    espacamentoTurma = 5
    espacamentoRA = 4
    espacamentoCurso = 5
    espacamentoNP1 = 3
    espacamentoNP2 = 3
    espacamentoPIM = 3
    espacamentoMedia = 5
    for i in resultado:
        if len(str(i[0])) > espacamentoID:
            espacamentoID = len(str(i[0]))
        if len(i[1]) > espacamentoNome:
            espacamentoNome = len(i[1])
        if len(str(i[2])) > espacamentoIdade:
            espacamentoIdade = len(str(i[2]))
        if len(i[3]) > espacamentoTurma:
            espacamentoTurma = len(i[3])
        if len(i[4]) > espacamentoRA:
            espacamentoRA = len(i[4])
        if len(i[5]) > espacamentoCurso:
            espacamentoCurso = len(i[5])
        if len(str(i[6])) > espacamentoNP1:
            espacamentoNP1 = len(str(i[6]))
        if len(str(i[7])) > espacamentoNP2:
            espacamentoNP2 = len(str(i[7]))
        if len(str(i[8])) > espacamentoPIM:
            espacamentoPIM = len(str(i[8]))
        if len(str(i[9])) > espacamentoMedia:
            espacamentoMedia = len(str(i[9]))
    print(f"{'ID':^{espacamentoID}} | {'NOME':^{espacamentoNome}} | {'IDADE':^{espacamentoIdade}} | {'TURMA':^{espacamentoTurma}} | {'RA':^{espacamentoRA}} | {'CURSO':^{espacamentoCurso}} | {'NP1':^{espacamentoNP1}} | {'NP2':^{espacamentoNP2}} | {'PIM':^{espacamentoPIM}} | {'MEDIA':^{espacamentoMedia}}")
    for i in resultado:
        print(
            f"{i[0]:^{espacamentoID}} | {i[1]:<{espacamentoNome}} | {i[2]:^{espacamentoIdade}} | {i[3]:^{espacamentoTurma}} | {i[4]:^{espacamentoRA}} | {i[5]:^{espacamentoCurso}} | {i[6]:^{espacamentoNP1}} | {i[7]:^{espacamentoNP2}} | {i[8]:^{espacamentoPIM}} | {i[9]:^{espacamentoMedia}}")
    print()
    inicio_programa()


def remover_aluno():

    resultado = cursor.execute(" SELECT * FROM ALUNOS ")

    print(f"{'ID':<4} | {'NOME':<3} | {'IDADE':<3}")
    for i in resultado:
        print(f"{i[0]:<4} | {i[1]:<3} | {i[2]:<3}")
    print()

    idRemover = 0
    while idRemover == 0:
        # try:
        idRemover = int(input("Escolha o ID do aluno que deseja remover:"))
        if idRemover <= 0:
            idRemover = 0
            print("ID inválido. Tente novamente!")
        else:
            nomeAlunoRemovido = cursor.execute(
                f"SELECT NOME FROM ALUNOS WHERE ID = {idRemover}"
            ).fetchone()

            if nomeAlunoRemovido is not None:
                cursor.execute(f"DELETE FROM ALUNOS WHERE ID = {idRemover}")
                cursor.execute(
                    "UPDATE sqlite_sequence SET seq = 0 WHERE name = 'ALUNOS'")
                print(f"ID: {idRemover} | Aluno: {nomeAlunoRemovido[0]}")
                print("Aluno removido com sucesso!")
            else:
                print("Nenhum aluno encontrado com esse ID.")

            inicio_programa()

        # except:
        # idRemover = 0
        # print("ID inválido. Tente novamente!")


def inicio_programa():
    escolha = 0

    print("="*40)
    print(f"{' Tabela de Cadastro de Alunos ':=^40}")
    print("="*40)
    print()

    print(" 1 - Cadastrar um aluno\n"
          " 2 - Remover um aluno\n"
          " 3 - Consultar os alunos cadastrados\n"
          " 4 - Sair")
    print()
    print("="*40)

    while escolha == 0:
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha <= 0 or escolha > 4:
                escolha = 0
                print("Opção inválida. Tente novamente!")
        except:
            print("Opção inválida. Tente novamente!")
            escolha = 0

    cursor.execute(
        " CREATE TABLE IF NOT EXISTS ALUNOS ( ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR, IDADE INTEGER NOT NULL, TURMA VARCHAR, RA VARCHAR, CURSO VARCHAR, NP1 FLOAT, NP2 FLOAT, PIM FLOAT, MEDIA FLOAT); ")

    match escolha:
        case 1: cadastro_aluno()
        case 2: remover_aluno()
        case 3: consulta_banco()
        case 4: sair_do_programa()
        case _: inicio_programa()


inicio_programa()
