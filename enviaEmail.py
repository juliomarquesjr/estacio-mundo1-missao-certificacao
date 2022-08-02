import smtplib as smt

class Email:
    def __init__(self, destinatario, assunto):
        self._destinatario = destinatario
        self._assunto = assunto
        self._host = 'mail.maximweb.com.br' #Buscar info do banco de dados
        self._usuario = 'julio@maximweb.com.br' #Buscar info do banco de dados
        self._senha = 'bTv6Y7QHw1ZT' #Buscar info do banco de dados
        self._porta = 465 #Buscar do banco de dados

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

if __name__ == "__main__":
    email = Email('juliomarquesjr@yahoo.com.br', 'Teste Classe Email')
    print(email.enviar_mensagem('Teste de email da classe Email'))