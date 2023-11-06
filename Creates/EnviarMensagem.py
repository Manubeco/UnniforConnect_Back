import mysql.connector
from datetime import datetime

MyConnection = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    port="47637",
    user="root",
    password="AhcdF-Ch6BGh21Af6hAc2-FD51Hbca2d",
    database="railway",
   )

MyCursor = MyConnection.cursor()

# CREATE (Enviar mensagem no grupo)
getIdAluno = int(input())
getIdGrupo = int(input())
getConteudo = input()
getDataEnvio= datetime.now()
enviarMensagem = f'insert into Mensagens (IdAluno, IdGrupo,Conteudo,DataEnvio) values ({getIdAluno},{getIdGrupo},"{getConteudo}","{getDataEnvio}")'
MyCursor.execute(enviarMensagem)
MyConnection.commit()


MyCursor.close()
MyConnection.close()