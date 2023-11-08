import json

from flask import Flask, jsonify, request
from bd import MyDb

app = Flask(__name__)

# Função para listar todos os grupos de uma disciplina
# Recebe o Id da disciplina pelo URL e retorna todos os grupos
def criarGrupos(idD,nomeGrupo):
    myCursor = MyDb.cursor()

    postGrupo = f"INSERT INTO Grupo (Descricao, IdDisciplina) VALUES ({nomeGrupo},{idD})"
    myCursor.execute(postGrupo)
    MyDb.commit()

    return ("Grupo criado com sucesso")

#
# def listarAlunos_Grupo(getIdGrupo):
#     myCursor = MyDb.cursor()
#
#     listarAlunos = (f'select Descricao, NomeAluno.NomeAluno from Aluno_Grupo '
#                     f'inner join Aluno as NomeAluno on Aluno_Grupo.IdAluno = NomeAluno.IdAluno '
#                     f'inner join Grupo as NomeGrupo on Aluno_Grupo.IdGrupo = NomeGrupo.IdGrupo '
#                     f'where Aluno_Grupo.IdGrupo = {getIdGrupo}')
#     myCursor.execute(listarAlunos)
#     resultado = myCursor.fetchall()
#     return jsonify(resultado)
#
#
# def listarMensagens(getIdGrupo):
#     myCursor = MyDb.cursor()
#
#     listarMensagens = (f'select Aluno.NomeAluno, Conteudo, DataEnvio from Mensagens '
#                        f'inner join Aluno on Mensagens.IdAluno = Aluno.IdAluno '
#                        f'where IdGrupo = {getIdGrupo} order by DataEnvio;')
#     myCursor.execute(listarMensagens)
#     resultado = myCursor.fetchall()
#     return jsonify(resultado)
