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
# ------------------ CRUD ----------------------------------

# MyConnection.commit() ||| Edita o banco de dados
# resultado = MyCursor.fetchall() ||| Ler o banco de dados

# CREATE (Criar Curso)
getNomeGrupo = input()
getIdDiscilplina = int(input())
criarCurso = f'INSERT INTO Grupo (descricao, iddisciplina) VALUE ("{getNomeGrupo}",{getIdDiscilplina})'
MyCursor.execute(criarCurso)
MyConnection.commit()


MyCursor.close()
MyConnection.close()
