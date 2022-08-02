class Tecnico:
    def __init__(self, nome, cpf, telefone, turno, nome_equipe):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._turno = turno
        self._nome_equipe = nome_equipe

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    def consulta_tecnico(self):
        pass

    def __str__(self):
        return f'Tecnico: {self._nome} - CPF: {self._cpf} - Telefone: {self._telefone}'

## Somente será usado para testar a classe isoladamente, sem vinculo com o restante do sistema
if __name__ == "__main__":
    print(Tecnico('Nome Teste', '123456', '1199998888', 'manha', 'beta'))