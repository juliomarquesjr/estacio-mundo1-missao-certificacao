import smtplib as smt
from banco import Banco

class Email:
    def __init__(self, destinatario, assunto):

        #Consulta configurações no banco
        config_data = Banco().consultar_dados('configuracoes')
        print(config_data)

        self._destinatario = destinatario
        self._assunto = assunto
        self._host = config_data[0]
        self._usuario = config_data[1]
        self._senha = config_data[2]
        self._porta = config_data[3]

    def enviar_mensagem(self, mensagem):
        try:
            server = smt.SMTP_SSL(self._host, self._porta)
            server.login(self._usuario, self._senha)
            self.mensagem = mensagem
            server.sendmail(self._usuario, self._destinatario, f'Subject: {self._assunto} \n{self.mensagem}')
            return True
        except:
            print("Erro ao enviar email")
            return False
        finally:
            server.quit()

## Somente será usado para testar a classe isoladamente,
# sem vinculo com o restante do sistema
if __name__ == "__main__":
    email = Email('juliomarquesjr@yahoo.com.br', 'Teste Classe Email - Banco')
    print(email.enviar_mensagem('Teste de email da classe Email com banco'))