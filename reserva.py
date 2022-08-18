from sistema.banco import Banco

class Reserva:

    def reservar_ferramenta(self, cpf_tecnico, tecnico, cod_ferramenta,
                            ferramenta, data_retirada, hora_retirada, data_devolucao,
                            hora_devolucao, descricao):


        self.banco = Banco().adicionar_dados(tabela='reserva', dados=f"('{cpf_tecnico}', "
                                                                     f"'{tecnico}', "
                                                                     f"'{cod_ferramenta}', "
                                                                     f"'{ferramenta}', "
                                                                     f"'{data_retirada}', "
                                                                     f"'{hora_retirada}', "
                                                                     f"'{data_devolucao}', "
                                                                     f"'{hora_devolucao}', "
                                                                     f"'{descricao}')")
        return self.banco

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
