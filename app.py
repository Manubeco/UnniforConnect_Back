from flask import Flask, jsonify, request
from bd import MyDb
import Reads
import Creates

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
@app.route('/grupo/<int:getIdGrupo>',methods=['GET'])
def consultaMensagens (getIdGrupo):
    consulta = Reads.Gets.listarMensagens(getIdGrupo)
    return consulta

# ---------------------------- PATH GETS ----------------------------------

@app.route('/grupo/<int:getIdGrupo>',methods=['GET'])
def criarGrupo (getIdGrupo):
    escrita = Creates.Posts.criarGrupos(getIdGrupo)
    return consulta


app.run(port=5000,host='localhost',debug=True)
