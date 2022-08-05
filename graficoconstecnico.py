import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button

from sistema.centraliza_janelas import center

class GraficoConsultaTecnico:
    def __init__(self):
        self._principal = tkinter.Toplevel()
        self._principal.geometry("450x300")
        self._principal.title('Consultas - Técnicos')
        center(self._principal)

        self.lbbusca = Label(self._principal, text="Buscar Técnico: ")
        self.lblista = Label(self._principal, text="Lista de Técnicos: ")

        self.cxbusca = Entry(self._principal, width=60)

        self.btpesquisa = Button(self._principal, text="Pesquisar", command=self.acao)
        self.btcadastrar = Button(self._principal, text="Cadastrar", command=self.acao)
        self.btvisul_edit = Button(self._principal, text="Visualizar/Editar", command=self.acao)
        self.btremover = Button(self._principal, text="Remover", command=self.acao)
        self.btfechar = Button(self._principal, text="Fechar", command=self._principal.quit)

        self.lbbusca.place(x=10, y=10)
        self.cxbusca.place(x=10, y=40)
        self.btpesquisa.place(x=380, y=35)
        self.lblista.place(x=10, y=80)
        self.btcadastrar.place(x=290,y=140)
        self.btvisul_edit.place(x=10,y=140)
        self.btremover.place(x=290,y=140)
        self.btfechar.place(x=340,y=140)

        self._principal.mainloop()

    def acao(self):
        print("Pressionado")

