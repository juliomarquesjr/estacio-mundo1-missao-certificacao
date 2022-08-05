import smtplib as smt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from banco import Banco

class Email:
    def __init__(self, destinatario):

        #Consulta configurações no banco
        config_data = Banco().consultar_dados('configuracoes')[0]

        self._host = config_data[0]
        self._senha = config_data[2]
        self._porta = config_data[3]

        self.msg = MIMEMultipart()
        self.msg['From'] = config_data[1]
        self.msg['To'] = destinatario
        self.msg['Subject'] = config_data[5]

    def enviar_mensagem(self, mensagem):
        self. msg.attach(MIMEText(mensagem, 'plain'))

        try:
            server = smt.SMTP_SSL(self._host, self._porta)
            server.login(self.msg['From'], self._senha)
            server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
            return True
        except:
            print("Erro ao enviar email")
            return False
        finally:
            server.quit()

## Somente será usado para testar a classe isoladamente,
# sem vinculo com o restante do sistema
if __name__ == "__main__":
    #pass
    email = Email('juliomarquesjr@yahoo.com.br')
    print(email.enviar_mensagem('Teste de email da classe Email com banco'))