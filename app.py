from flask import Flask, jsonify, request,session,redirect,url_for
import Reads.Gets
import Creates.Posts
import auth
import hashlib 

app = Flask(__name__)
app.secret_key = 'testando'


 # --------------- Autenticacao-------------------
#
# autenticacao = Autenticacao()
#
@app.route('/login', methods=['POST'])
def efetuarLogin():
    dados = request.json
    if dados["Matricula"] != None and dados["Senha"] != None:
        matriculaAluno = int(dados["Matricula"])
        senha = dados["Senha"]

        hash = senha + app.secret_key
        hash = hashlib.sha1(hash.encode())
        senha = hash.hexdigest()

        escrita = auth.Autenticacao().login(matriculaAluno, senha)
        return escrita
    return jsonify({'status': 'error'})
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
