import MySQLdb

class FabricaConexao():

    @staticmethod
    def conectar():
        db = MySQLdb.connect(user='root', passwd='@Primeirasenha01', db='treinaweb_clientes', autocommit=True)

        return db