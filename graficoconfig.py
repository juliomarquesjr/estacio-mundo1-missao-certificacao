import tkinter
from tkinter import Label, Button, Entry, messagebox, PhotoImage

from config import Config
from sistema.centraliza_janelas import center


class GraficoConfig(Config):
    def __init__(self):
        super().__init__()
        self._principal = tkinter.Toplevel() #Top Level pois ela é filha de graficomain.py

        ## Ajustar tamanho da janela e não permitir maximizar
        self._principal.geometry("250x175")
        self._principal.minsize(250, 175)
        self._principal.maxsize(250, 175)

        self._principal.title('Configurações')
        center(self._principal)

        self.lbhost = Label(self._principal, text="Host: ")
        self.lbusuario = Label(self._principal, text="Usuário: ")
        self.lbsenha = Label(self._principal, text="Senha: ")
        self.lbporta = Label(self._principal, text="Porta: ")

        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_sair = PhotoImage(file="assets/icones/icon_saida.png")

        self.cxhost = Entry(self._principal, width=20)
        self.cxusuario = Entry(self._principal, width=20)
        self.cxsenha = Entry(self._principal, width=20)
        self.cxporta = Entry(self._principal, width=20)

        self.btsalvar = Button(self._principal, image=self.icon_salvar, compound='left', height=22, padx=5,
                               text="Salvar", command=self._salvar)
        self.btfechar = Button(self._principal, image=self.icon_sair, compound='left', height=22, padx=5, text="Fechar",
                               command=self._principal.destroy)

        self.lbhost.place(x=20, y=10)
        self.cxhost.place(x=75, y=10)
        self.lbusuario.place(x=20, y=40)
        self.cxusuario.place(x=75, y=40)
        self.lbsenha.place(x=20, y=70)
        self.cxsenha.place(x=75, y=70)
        self.lbporta.place(x=20, y=100)
        self.cxporta.place(x=75, y=100)
        self.btsalvar.place(x=45, y=140)
        self.btfechar.place(x=120, y=140)

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

    def quit(self):
        self._principal.quit()

    def _salvar(self):
        resposta = self._salvar_configuracao(dados=(self.cxhost.get(),
                                                    self.cxusuario.get(),
                                                    self.cxsenha.get(),
                                                    self.cxporta.get()))

        if resposta:
            tkinter.messagebox.showinfo('Salvar Configuração', 'Dados salvos com sucesso!')
        else:
            tkinter.messagebox.showerror('Erro ao Salvar',
                                         "Erro ao salvar as informações. Por favor, verifique os campos.")

        self._principal.lift()  # Puxa a janela novamente para frente após exibir o aviso
