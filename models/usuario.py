from flask_login import UserMixin
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from database.db import GerenciarBanco

# gerenciar_banco = GerenciarBanco()
# conn = gerenciar_banco.conectar()
# cursor = conn.cursor()


class Usuario(UserMixin):
    def set_usuario(self, id_us, numfunc_us, email_us, nome_us, senha_us, id_jd, tipo_us, sessao_us):
        self.id_us = id_us
        self.NumFunc_us = numfunc_us
        self.email_us = email_us
        self.nome_us = nome_us
        self.senha_us = senha_us
        self.id_jd = id_jd
        self.tipo_us = tipo_us
        self.sessao_us = sessao_us

    def get_usuario(self):
        return self.id_us, self.NumFunc_us, self.email_us, self.nome_us, self.senha_us, self.id_jd, self.tipo_us, self.sessao_us

# sql = "SELECT * FROM usuario WHERE id_us = (?);"
# cursor.execute(sql, [2])
# res = cursor.fetchone()
# print(res)
# usuario = Usuario()
# usuario.set_usuario(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7])
# print(usuario.get_usuario())