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

# UPDATE (Renomear Grupo)
novoNome = "Segurança da informação"
renomearGrupo = f'UPDATE Curso SET NomeCurso = "{novoNome}" WHERE IdCurso = 4'
MyCursor.execute(renomearGrupo)
MyConnection.commit()

MyCursor.close()
MyConnection.close()