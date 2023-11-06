import mysql.connector
import requests

MyConnection = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    port="47637",
    user="root",
    password="AhcdF-Ch6BGh21Af6hAc2-FD51Hbca2d",
    database="railway",
   )

MyCursor = MyConnection.cursor()

# CREATE (Inscrever no grupo)
getIdAluno = int(input())
getIdGrupo = int(input())
entrarGrupo = f'insert into Aluno_Grupo (IdAluno, IdGrupo) values ({getIdAluno},{getIdGrupo})'
MyCursor.execute(entrarGrupo)
MyConnection.commit()


MyCursor.close()
MyConnection.close()