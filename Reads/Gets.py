from flask import Flask, jsonify, request
from bd import MyDb

app = Flask(__name__)

# Função para listar todos os grupos de uma disciplina
# Recebe o Id da disciplina pelo URL e retorna todos os grupos
def listarGrupos(getIdDisciplina):
    myCursor = MyDb.cursor()

    listarGrupos = (f'SELECT Grupo.Descricao,NomeDisciplina.Descricao from Grupo '
                    f'inner join Disciplina as NomeDisciplina on Grupo.IdDisciplina = NomeDisciplina.IdDisciplina '
                    f'where Grupo.IdDisciplina = {getIdDisciplina}')
    myCursor.execute(listarGrupos)
    resultado = myCursor.fetchall()
    return jsonify(resultado)

# Função para listar todos os alunos de um grupo
# Recebe o Id do grupo pelo URL e retorna todos os alunos
def listarAlunos_Grupo(getIdGrupo):
    myCursor = MyDb.cursor()

    listarAlunos = (f'select Descricao, NomeAluno.NomeAluno from Aluno_Grupo '
                    f'inner join Aluno as NomeAluno on Aluno_Grupo.IdAluno = NomeAluno.IdAluno '
                    f'inner join Grupo as NomeGrupo on Aluno_Grupo.IdGrupo = NomeGrupo.IdGrupo '
                    f'where Aluno_Grupo.IdGrupo = {getIdGrupo}')
    myCursor.execute(listarAlunos)
    resultado = myCursor.fetchall()
    return jsonify(resultado)

# Função para listar todas as mensagens de um grupo
# Recebe o Id do grupo pelo URL e retorna todas as mensagens
def listarMensagens(getIdGrupo):
    myCursor = MyDb.cursor()

    listarMensagens = (f'select Aluno.NomeAluno, Conteudo, DataEnvio from Mensagens '
                       f'inner join Aluno on Mensagens.IdAluno = Aluno.IdAluno '
                       f'where IdGrupo = {getIdGrupo} order by DataEnvio;')
    myCursor.execute(listarMensagens)
    resultado = myCursor.fetchall()
    return jsonify(resultado)
