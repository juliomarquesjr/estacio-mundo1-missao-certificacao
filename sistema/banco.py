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
        print('Conectou o banco')

    def adicionar_dados(self):
        pass

    def atualizar_dados(self):
        pass

    def remover_dados(self):
        pass

    def consultar_dados(self, tabela):
        self.sql = f'SELECT * FROM {tabela}'
        self.conexao = self.conectar()
        self.cursor = self.conexao.cursor()
        self.cursor.execute(self.sql)

        recset = self.cursor.fetchall()
        registros = []
        for rec in recset:
            registros.append(rec)

        print(registros)

        self.cursor.close()
        self.conexao.close()

        return registros


if __name__ == "__main__":
     Banco().consultar_dados('testes')