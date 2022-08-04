import tkinter
from tkinter import Label, Button, Entry
from config import Config

class GraficoConfig(Config):
    def __init__(self):
        super().__init__()
        self._principal = tkinter.Tk()
        self._principal.geometry("200x175")
        self._principal.title('Configurações')

        self.lbhost = Label(self._principal, text="Host: ")
        self.lbusuario = Label(self._principal, text="Usuário: ")
        self.lbsenha = Label(self._principal, text="Senha: ")
        self.lbporta = Label(self._principal, text="Porta: ")

        self.cxhost = Entry(self._principal, width=15)
        self.cxusuario = Entry(self._principal, width=15)
        self.cxsenha = Entry(self._principal, width=15)
        self.cxporta = Entry(self._principal, width=15)

        self.btsalvar = Button(self._principal, text="Salvar", command=self._salvar)
        self.btfechar = Button(self._principal, text="Fechar", command=self._principal.quit)

        self.lbhost.place(x=20, y=10)
        self.cxhost.place(x=75, y=10)
        self.lbusuario.place(x=20, y=40)
        self.cxusuario.place(x=75, y=40)
        self.lbsenha.place(x=20, y=70)
        self.cxsenha.place(x=75, y=70)
        self.lbporta.place(x=20, y=100)
        self.cxporta.place(x=75, y=100)
        self.btsalvar.place(x=90, y=140)
        self.btfechar.place(x=140, y=140)

        self._preenche_campos()
        self._principal.mainloop()

    def _preenche_campos(self):
        dados = self._carregar_configuracao()[0]

        if dados != False:
            print(dados)
            self.cxhost.insert(0, dados[0])
            self.cxusuario.insert(0, dados[1])
            self.cxsenha.insert(0, dados[2])
            self.cxporta.insert(0, dados[3])

    def _salvar(self):
        self._salvar_configuracao(dados=(self.cxhost.get(),
                                         self.cxusuario.get(),
                                         self.cxsenha.get(),
                                         self.cxporta.get()))


janela = GraficoConfig()