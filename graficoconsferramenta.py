import tkinter
from tkinter import Label, Entry, Button

from sistema.centraliza_janelas import center

class GraficoConsultaTecnico:
    def __init__(self):
        self.principal = tkinter.Toplevel()
        self.principal.geometry("450x300")
        self.principal.title('Consultas - Ferramentas')
        center(self.principal)

        self.lbbusca = Label(self.principal, text="Buscar Ferramenta: ")
        self.lblista = Label(self.principal, text="Lista de Ferramentas: ")

        self.cxbusca = Entry(self.principal, width=60)

        self.btpesquisa = Button(self.principal, text="Pesquisar", command=self.acao)
        self.btcadastrar = Button(self.principal, text="Cadastrar", command=self.acao)
        self.btvisul_edit = Button(self.principal, text="Visualizar/Editar", command=self.acao)
        self.btremover = Button(self.principal, text="Remover", command=self.acao)
        self.btfechar = Button(self.principal, text="Fechar", command=self.principal.quit)

        self.lbbusca.place(x=10, y=10)
        self.cxbusca.place(x=10, y=40)
        self.btpesquisa.place(x=380, y=35)
        self.lblista.place(x=10, y=80)
        # self.btcadastrar.place(x=290,y=140)
        # self.btvisul_edit.place(x=10,y=140)
        # self.btremover.place(x=290,y=140)
        # self.btfechar.place(x=340,y=140)

        self.principal.mainloop()

    def acao(self):
        print("Pressionado")