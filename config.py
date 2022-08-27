from sistema.banco import Banco

class Config:
    def __init__(self):
        self._banco = Banco()

    def _salvar_configuracao(self, dados = False):
        if dados != False:
            return self._banco.atualizar_dados(tabela='configuracoes', where='id = 1',
                                        set=f"email_host = '{dados[0]}', "
                                            f"email_usuario = '{dados[1]}', "
                                            f"email_senha = '{dados[2]}', "
                                            f"email_porta = {dados[3]}, "
                                            f"email_remetente = '{dados[4]}', "
                                            f"email_destinatario = '{dados[5]}'" )

    def _carregar_configuracao(self):
        return self._banco.consultar_dados('configuracoes', f"id = 1")