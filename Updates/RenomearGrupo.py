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
getIdGrupo = int(input())
renomearGrupo = f'UPDATE Grupo SET Descricao = "{novoNome}" WHERE IdGrupo = {getIdGrupo}'
MyCursor.execute(renomearGrupo)
MyConnection.commit()

MyCursor.close()
MyConnection.close()