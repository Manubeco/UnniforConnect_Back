from flask import Flask, jsonify, request,session,redirect,url_for
from bd import MyDb
from auth import Autenticacao
import Reads.Gets
import Creates.Posts

app = Flask(__name__)
app.secret_key = 'testando'


 # --------------- Autenticacao-------------------
#
# autenticacao = Autenticacao()
#
# @app.route('/login', methods=['POST'])
# def login():
#     dados = request.json
#     matricula = dados.get("Matricula")
#     senha = dados.get("Senha")
#
#     if autenticacao.login(matricula, senha):
#         session['matricula'] = matricula
#         return jsonify({"mensagem": "Login bem-sucedido!"})
#     else:
#         return jsonify({"mensagem": "Usuário ou senha incorretos"}), 401
#
# @app.route('/logout', methods=['POST'])
# def logout():
#     autenticacao.logout()
#     session.pop('matricula', None)
#     return jsonify({"mensagem": "Logout bem-sucedido!"})
#
# @app.route('/restrito', methods=['GET'])
# def rota_restrita():
#     if 'matricula' in session:
#         return jsonify({"mensagem": "Conteúdo restrito. Você está logado!"})
#     else:
#         return jsonify({"mensagem": "Acesso não autorizado"}), 401
#
# if __name__ == '__main__':
#     app.run(debug=True)





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
    idD = int(dados[0]["IdDisciplina"])
    nomeGrupo = str(dados[0]["NomeGrupo"])

    escrita = Creates.Posts.criarGrupos(idD,nomeGrupo)
    return escrita

@app.route('/entrar',methods=['POST'])
def entrarGrupo():
    dados = request.json
    idG = int(dados[0]["IdGrupo"])
    matriculaAluno = int(dados[0]["Matricula"])

    escrita = Creates.Posts.entrarGrupos(idG,matriculaAluno)
    return escrita

@app.route('/grupo/chat',methods=['POST'])
def enviarMensagem():
    dados = request.json
    idG = int(dados[0]["IdGrupo"])
    matriculaAluno = int(dados[0]["Matricula"])
    mensagem = dados[0]["Mensagem"]

    escrita = Creates.Posts.enviarMensagens(idG,matriculaAluno,mensagem)
    return escrita

app.run(port=5000,host='localhost',debug=True)
