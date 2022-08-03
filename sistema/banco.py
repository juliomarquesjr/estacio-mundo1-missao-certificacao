import psycopg2

class Banco:
    def __init__(self):
        self._host = 'localhost'
        self._usuario = 'postgres'
        self._senha = '123456'
        self._porta = '5432'
        self._banco = 'postgres'

    def conectar(self):
        self.conn = psycopg2.connect(host=self._host,
                                     database=self._banco,
                                     user=self._usuario,
                                     password=self._senha,
                                     port=self._porta)

        return self.conn

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

    def atualizar_dados(self):
        pass

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


    def consultar_dados(self, tabela):
        self.sql = f'SELECT * FROM {tabela}'

        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor()
        self.cursor.execute(self.sql)

        recset = self.cursor.fetchall()
        registros = []
        for rec in recset:
            registros.append(rec)

        self.cursor.close()
        self.conexao.close()

        return registros[0]

## Somente será usado para testar a classe isoladamente,
# sem vinculo com o restante do sistema
if __name__ == "__main__":
    pass
    #print(Banco().adicionar_dados('configuracoes', ('mail.maximweb.com.br', 'julio@maximweb.com.br', 'bTv6Y7QHw1ZT', 465)))
    #print(Banco().remover_dados('testes','id = 4'))

    #Banco().consultar_dados('configuracoes')

