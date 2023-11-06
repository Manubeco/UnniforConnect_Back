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
listarMensagens = f'select Conteudo, DataEnvio, Aluno.NomeAluno from Mensagens inner join Aluno on Mensagens.IdAluno = Aluno.IdAluno where IdGrupo = {getIdGrupo} order by DataEnvio;'
MyCursor.execute(listarMensagens)
resultado = MyCursor.fetchall()
print(resultado)

MyCursor.close()
MyConnection.close()
