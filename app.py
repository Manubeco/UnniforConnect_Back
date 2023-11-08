from flask import Flask, jsonify, request
from bd import MyDb
import json
import Reads.Gets
import Creates.Posts

app = Flask(__name__)

# ---------------------------- PATH GETS ----------------------------------

# Passar Id da disciplina no URL
@app.route('/grupos_disciplina/<int:getIdDisciplina>',methods=['GET'])
def consultarGrupos(getIdDisciplina):
    consulta = Reads.Gets.listarGrupos(getIdDisciplina)
    return consulta

# Passar Id do grupo no URL
@app.route('/alunos_grupo/<int:getIdGrupo>',methods=['GET'])
def consultaAlunos (getIdGrupo):
    consulta = Reads.Gets.listarAlunos_Grupo(getIdGrupo)
    return consulta

# Passar Id do grupo no URL
@app.route('/grupo/<int:getIqdGrupo>',methods=['GET'])
def consultaMensagens (getIdGrupo):
    consulta = Reads.Gets.listarMensagens(getIdGrupo)

    return consulta

# ---------------------------- PATH POSTS ----------------------------------

@app.route('/grupo',methods=['POST'])
def criarGrupo():
    dados = request.json
    lerJson = json.load(dados)
    idD = lerJson['IdDisciplina']
    nomeGrupo = lerJson['NomeGrupo']
    idD = int(idD)

    escrita = Creates.Posts.criarGrupos(idD,nomeGrupo)
    return escrita


app.run(port=5000,host='localhost',debug=True)
