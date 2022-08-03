from sistema.banco import Banco

class Tecnico():
    def __init__(self, nome, cpf, telefone, turno, nome_equipe):
        self._nome = nome.title()
        self._cpf = cpf
        self._telefone = telefone
        self._turno = turno
        self._nome_equipe = nome_equipe

        #Verifica se o cadastro já existe no banco
        if Banco().consultar_dados(tabela='tecnico', where=f"cpf = '{self._cpf}'") == False:
            self.cadastra_banco()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        self._atualiza_banco()

    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone
        self.atualiza_banco()

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, novo_turno):
        self._turno = novo_turno
        self._atualiza_banco()

    @property
    def nome_equipe(self):
        return self._nome_equipe

    @nome_equipe.setter
    def nome_equipe(self, nova_equipe):
        self._nome_equipe = nova_equipe
        self._atualiza_banco()

    def consulta_banco(self):
        self.resp = Banco().consultar_dados(tabela='tecnico', where="cpf = '{}'".format(self._cpf))

        return self.resp

    def cadastra_banco(self):
        self.resp = Banco().adicionar_dados(tabela='tecnico', dados=(self._nome, self._cpf, self._telefone, self._turno, self._nome_equipe))
        return self.resp

    def remover_banco(self):
        self.resp = Banco().remover_dados(tabela='tecnico',
                                          where="cpf = '{}'".format(self.cpf))
        return self.resp

    def _atualiza_banco(self):
        self.resp = Banco().atualizar_dados(tabela='tecnico',
                                            set=f"nome = '{self.nome}', "
                                                f"telefone = '{self.telefone}', "
                                                f"turno = '{self.turno}', "
                                                f"nome_equipe = '{self.nome_equipe}'",
                                            where="cpf = '{}'".format(self.cpf))

    def __str__(self):
        return f'Técnico: {self._nome} - CPF: {self._cpf} - Telefone: {self._telefone}'

## Somente será usado para testar a classe isoladamente,
# sem vinculo com o restante do sistema
if __name__ == "__main__":
    pass
    #novo_tecnico = Tecnico(nome='Juca da Silva', cpf='452145785', telefone='887788995', turno='tarde', nome_equipe='beta')
    #novo_tecnico.nome = "Juca da Silveira"
    #print(novo_tecnico.consulta_banco())