import json
from datetime import datetime
from flask import Flask, jsonify, request
from bd import MyDb

app = Flask(__name__)

# Função para listar todos os grupos de uma disciplina
# Recebe o Id da disciplina pelo URL e retorna todos os grupos
def criarGrupos(idD,nomeGrupo):
    myCursor = MyDb.cursor()

    postGrupo = f"INSERT INTO Grupo (Descricao, IdDisciplina) VALUES (%s,%s)"
    valores = (nomeGrupo,idD)

    myCursor.execute(postGrupo,valores)
    MyDb.commit()

    return ("Grupo criado com sucesso")

#
#
def entrarGrupos(idG,matriculaAluno):
    myCursor = MyDb.cursor()

    getIdAluno = f'select idAluno from Aluno where Matricula = %s'
    myCursor.execute(getIdAluno,(matriculaAluno,))
    idAluno = myCursor.fetchone()

    if idAluno:
        idAluno = idAluno[0]

        alocarGrupo = f'insert into Aluno_Grupo (IdAluno, IdGrupo) values (%s,%s)'
        valores = (idAluno,idG)

        myCursor.execute(alocarGrupo, valores)
        MyDb.commit()
        return jsonify("Você entrou no grupo!")

    else:
        return jsonify("Aluno não encontrado")

#
#
def enviarMensagens(idG,matriculaAluno,mensagem):
    myCursor = MyDb.cursor()

    getIdAluno = f'select idAluno from Aluno where Matricula = %s'
    myCursor.execute(getIdAluno, (matriculaAluno,))
    idAluno = myCursor.fetchone()

    if idAluno:
        idAluno = idAluno[0]

        getDataEnvio = datetime.now()
        enviarMensagem = f'insert into Mensagens (IdAluno, IdGrupo,Conteudo,DataEnvio) values (%s,%s,%s,%s)'
        valores =  (idAluno,idG,mensagem,getDataEnvio)

        myCursor.execute(enviarMensagem, valores)
        MyDb.commit()

        return jsonify("Mensagem enviada!")

    else:
        return jsonify("Um erro aconteceu")


    myCursor.execute(enviarMensagem)


