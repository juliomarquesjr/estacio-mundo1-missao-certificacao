import psycopg2

class Banco:
    def __init__(self):
        self._host = 'ec2-44-206-137-96.compute-1.amazonaws.com'
        self._usuario = 'bxbdmvmqpovnon'
        self._senha = '9be6c16d7cc05d0de7872cd14ab3ea8a1ce2a86a92b24a397f4686c0321ff30c'
        self._porta = '5432'
        self._banco = 'd7v4r0efu4qak2'

        # self._host = 'localhost'
        # self._usuario = 'postgres'
        # self._senha = '123456'
        # self._porta = '5432'
        # self._banco = 'postgres'

    def conectar(self):
        try:
            conn = psycopg2.connect(host=self._host,
                                         database=self._banco,
                                         user=self._usuario,
                                         password=self._senha,
                                         port=self._porta)
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            return False


    def adicionar_dados(self, tabela, dados):
        self.sql = f"INSERT into {tabela} values {dados}"

        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor()

        try:
            self.cursor.execute(self.sql)
            self.conexao.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conexao.rollback()
            return False
        finally:
            self.cursor.close()
            self.conexao.close()

    def atualizar_dados(self, tabela, set, where):
        self.sql = f"UPDATE {tabela} SET {set} WHERE {where}"

        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor()

        try:
            self.cursor.execute(self.sql)
            self.conexao.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conexao.rollback()
            return False
        finally:
            self.cursor.close()
            self.conexao.close()

    def remover_dados(self, tabela, where):
        self.sql = f'DELETE from {tabela} WHERE ({where})'

        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor()

        try:
            self.cursor.execute(self.sql)
            self.conexao.commit()

            if self.cursor.rowcount == 1:
                return True
            else:
                return False

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conexao.rollback()
            return False
        finally:
            self.cursor.close()
            self.conexao.close()

    def consultar_dados(self, tabela, where = 'none'):
        if where == 'none':
            self.sql = f'SELECT * FROM {tabela}'
        else:
            self.sql = f'SELECT * FROM {tabela} WHERE ({where})'

        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor()

        try:
            self.cursor.execute(self.sql)

            recset = self.cursor.fetchall()
            registros = []
            for rec in recset:
                registros.append(rec)

            return (*registros, )

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conexao.rollback()
            return False
        finally:
            self.cursor.close()
            self.conexao.close()

    def consultar_nomes(self, tabela, campo='none', like='none'):
        self.sql = f"SELECT * FROM {tabela} WHERE {campo} ILIKE '%{like}%'"

        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor()

        try:
            self.cursor.execute(self.sql)

            recset = self.cursor.fetchall()
            registros = []
            for rec in recset:
                registros.append(rec)

            return (*registros, )

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conexao.rollback()
            return False
        finally:
            self.cursor.close()
            self.conexao.close()