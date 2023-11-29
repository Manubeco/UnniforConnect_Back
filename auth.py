from flask import request, jsonify, session
from bd import MyDb
import app

class Autenticacao:
    def login(Mybd, matricula, senha):

        # Verifica se conta existe no Banco
        myCursor = MyDb.cursor()
        myCursor.execute('SELECT * FROM Aluno WHERE Matricula = %s AND senha = %s', (matricula, senha,))
        # retorna o resultado
        account = myCursor.fetchone()
        # Se a conta existir na tabela no banco
        if account:
            # Cria uma sessão, podemos acessar esses dados em outras rotas
            session['loggedin'] = True
            session['id'] = account['id']
            session['Matricula'] = account['Matricula']

            return 'Você entrou com sucesso!'
        else:
            # Se a conta não assistir existir ou Matricula/Senha estiver incorreta
            msg = 'Matricula ou senha inválida!'

    def logout(self):

        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('Matricula', None)

        return jsonify("Você saiu com sucesso!")