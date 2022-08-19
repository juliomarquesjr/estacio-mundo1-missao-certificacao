from sistema.banco import Banco

class Reserva:
    def __init__(self, cpf_tecnico=False, tecnico=False, cod_ferramenta=False,
                            ferramenta=False, data_retirada=False, hora_retirada=False, data_devolucao=False,
                            hora_devolucao=False, descricao=False):
        self._cpf_tecnico = cpf_tecnico
        self._tecnico = tecnico
        self._cod_ferramenta = cod_ferramenta
        self._ferramenta = ferramenta
        self._data_retirada = data_retirada
        self._hora_retirada = hora_retirada
        self._data_devolucao = data_devolucao
        self._hora_devolucao = hora_devolucao
        self._descricao = descricao

    def reservar_ferramenta(self):
        self.resp = Banco().adicionar_dados(tabela='reserva', dados=f"('{self._cpf_tecnico}', "
                                                                     f"'{self._tecnico}', "
                                                                     f"'{self._cod_ferramenta}', "
                                                                     f"'{self._ferramenta}', "
                                                                     f"'{self._data_retirada}', "
                                                                     f"'{self._hora_retirada}', "
                                                                     f"'{self._data_devolucao}', "
                                                                     f"'{self._hora_devolucao}', "
                                                                     f"'{self._descricao}')")
        return self.resp

    def atualiza_banco(self, set, where):
        self.resp = Banco().atualizar_dados(tabela='reserva', set=set, where=where)
        return self.resp

    def remover_banco(self, id):
        self.resp = Banco().remover_dados(tabela='reserva',
                                          where="id = '{}'".format(id))
        return self.resp

    def envia_email(self):
       pass

    def listar_tecnicos_cadastrados(self):
        lista_tecnicos = Banco().consultar_dados(tabela='tecnico')
        return lista_tecnicos

    def listar_ferramentas_cadastradas(self):
        lista_ferramentas = Banco().consultar_dados(tabela='ferramenta')
        return lista_ferramentas

    def listar_reservas_cadastradas(self):
        lista_reservas = Banco().consultar_dados(tabela='reserva')
        return lista_reservas

    def pesquisar_banco(self, campo, pesquisa):
        lista_pesquisa_reserva = Banco().consultar_nomes('reserva', campo, like=pesquisa)
        return lista_pesquisa_reserva

    def consulta_banco(self, codigo):
        self.resp = Banco().consultar_dados(tabela='reserva', where=f"id = '{codigo}'")
        return self.resp
