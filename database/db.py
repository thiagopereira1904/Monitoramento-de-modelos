import pyodbc

class GerenciarBanco():
    def conectar(self):
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=DESKTOP-J3BEJ2O;'
            'Database=db;'
            'Trusted_Connection=yes;')
        return conn

    def fechar(self, conn):
        try:
            conn.close()
            return True
        except:
            return "Erro ao fechar conexão!"