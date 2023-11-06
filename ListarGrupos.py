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

# # READ
listarGrupos = f'SELECT Grupo.Descricao,NomeDisciplina.Descricao from Grupo inner join Disciplina as NomeDisciplina where Grupo.IdDisciplina = NomeDisciplina.IdDisciplina'
MyCursor.execute(listarGrupos)
resultado = MyCursor.fetchall()
print(resultado)

MyCursor.close()
MyConnection.close()
