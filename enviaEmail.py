import smtplib as smt

class Email:
    def __init__(self, destinatario, assunto, host, usuario, senha, porta):
        self._destinatario = destinatario
        self._assunto = assunto
        self._host = host
        self._usuario = usuario
        self._senha = senha
        self._porta = porta

    def _conectar(self):
        server = smt.SMTP_SSL(self._host, self._porta)
        server.login(self._usuario, self._senha)
        return server

    def enviar_mensagem(self, mensagem):
        server = self._conectar()

        if(server):
            self.mensagem = mensagem
            server.sendmail(self._usuario, self._destinatario, f'Subject: {self._assunto}\n {self.mensagem}')
            server.quit()
            return True
        else:
            return False

if __name__ == "__main__":
    email = Email('juliomarquesjr@yahoo.com.br', 'Teste Classe Email', 'mail.maximweb.com.br','julio@maximweb.com.br', 'bTv6Y7QHw1ZT', '465')
    print("Mensagem Envida") if email.enviar_mensagem('Teste de email da classe Email') else print("Deu erro")