from sistema.banco import Banco

class Reserva:

    def reservar_ferramenta(self, tecnico, ferramenta, data_retirada, data_entrega):
        dados = f"'{tecnico}', "
        f"'{ferramenta}', "
        f"'{data_retirada}', "
        f"'{data_entrega}'"

        print(dados)

        # self.banco = Banco().adicionar_dados(tabela='reserva', dados=f"'{tecnico}', "
        #                                                              f"'{ferramenta}', "
        #                                                              f"'{data_retirada}', "
        #                                                              f"'{data_entrega}'")
        # if self.banco:
        #     pass
        # else:
        #     pass

    def envia_email(self):
       pass

    def listar_tecnicos_cadastrados(self):
        self.lista_tecnicos = Banco().consultar_dados(tabela='tecnico')
        return self.lista_tecnicos

    def listar_ferramentas_cadastradas(self):
        self.lista_ferramentas = Banco().consultar_dados(tabela='ferramenta')
        return self.lista_ferramentas
