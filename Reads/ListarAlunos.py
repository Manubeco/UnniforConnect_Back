import mysql.connector

MyConnection = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    port="47637",
    user="root",
    password="AhcdF-Ch6BGh21Af6hAc2-FD51Hbca2d",
    database="railway",
   )

MyCursor = MyConnection.cursor()

# # READ
getIdGrupo = int(input())
listarAlunos = f'select NomeAluno.NomeAluno from Aluno_Grupo inner join Aluno as NomeAluno on Aluno_Grupo.IdAluno = NomeAluno.IdAluno where Aluno_Grupo.IdGrupo = {getIdGrupo}'
MyCursor.execute(listarAlunos)
resultado = MyCursor.fetchall()
print(resultado)

MyCursor.close()
MyConnection.close()
