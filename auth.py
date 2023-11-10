import hashlib
from bd import MyDb

class Autenticacao:

    def login(Mybd, matricula, senha):
        if matricula in Mybd.Aluno  :
            usuario = Mybd.Aluno[matricula]
            # Verifique a senha usando a função de hash
            senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            if senha_hash == MyDb.Aluno['senha']:
                return True
        return False

    def logout(self):
        # Lógica de logout - pode ser mais elaborada dependendo dos requisitos
        pass