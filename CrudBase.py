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

# Operadores banco
# MyConnection.commit() ||| Edita o banco de dados
# resultado = MyCursor.fetchall() ||| Ler o banco de dados

# ------------------------ CREATE (Criar Curso)
# nameCurso = "Ciências da computação"
# criarCurso = f'INSERT INTO Curso (NomeCurso) VALUE ("{nameCurso}")'
# MyCursor.execute(criarCurso)
# MyConnection.commit()

# ------------------------ READ (listar grupos)
# listarGrupos = f'SELECT Grupo.Descricao,NomeDisciplina.Descricao from Grupo inner join Disciplina as NomeDisciplina where Grupo.IdDisciplina = NomeDisciplina.IdDisciplina'
# MyCursor.execute(listarGrupos)
# resultado = MyCursor.fetchall()
# print(resultado)


# ------------------------ UPDATE
# novoNome = "Segurança da informação"
# renomearGrupo = f'UPDATE Curso SET NomeCurso = "{novoNome}" WHERE IdCurso = 4'
# MyCursor.execute(renomearGrupo)
# MyConnection.commit()

# ------------------------ DELETE
cursoSelecionado = 5
deletarCurso = f'Delete from Curso where Idcurso = "{cursoSelecionado}"'
MyCursor.execute(deletarCurso)
MyConnection.commit()




MyCursor.close()
MyConnection.close()
