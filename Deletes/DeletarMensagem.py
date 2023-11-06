import mysql.connector

MyConnection = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    port="47637",
    user="root",
    password="AhcdF-Ch6BGh21Af6hAc2-FD51Hbca2d",
    database="railway",
   )

MyCursor = MyConnection.cursor()

# ------------------------ DELETE
getIdMensagem = int(input())
deletarMensagem = f'Delete from Mensagens where IdMensagem = {getIdMensagem}'
MyCursor.execute(deletarMensagem)
MyConnection.commit()


MyCursor.close()
MyConnection.close()
