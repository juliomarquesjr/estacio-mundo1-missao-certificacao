import tkinter
from tkinter import Label, ttk, Button, Entry

from sistema.centraliza_janelas import center

class GraficoTecnico:
    def __init__(self):

        self.principal = tkinter.Toplevel()
        self.principal.geometry("400x175")
        self.principal.title('Técnicos')
        center(self.principal)

        self.lbnome = Label(self.principal, text="Nome: ")
        self.lbcpf = Label(self.principal, text="CPF: ")
        self.lbtel = Label(self.principal, text="Telefone: ")
        self.lbequipe = Label(self.principal, text="Equipe: ")
        self.lbturno = Label(self.principal, text="Turno: ")

        self.cxnome = Entry(self.principal, width = 45)
        self.cxcpf = Entry(self.principal, width = 16)
        self.cxtel = Entry(self.principal, width = 14)
        self.cxequipe = Entry(self.principal, width = 35)
        self.cxturno = ttk.Combobox(self.principal)
        self.cxturno['values'] = ("Manhã","Tarde","Noite")

        self.bteditar = Button(self.principal, text="Editar", command=self.acao)
        self.btsalvar = Button(self.principal, text="Salvar", command=self.acao)
        self.btfechar = Button(self.principal, text="Fechar", command=self.principal.destroy)

        self.lbnome.place(x=10,y=10)
        self.cxnome.place(x=60,y=10)
        self.lbcpf.place(x=10,y=40)
        self.cxcpf.place(x=60,y=40)
        self.lbtel.place(x=185,y=40)
        self.cxtel.place(x=245,y=40)
        self.lbequipe.place(x=10,y=70)
        self.cxequipe.place(x=60,y=70)
        self.lbturno.place(x=10,y=100)
        self.cxturno.place(x=60,y=100)
        self.bteditar.place(x=10,y=140)
        self.btsalvar.place(x=290,y=140)
        self.btfechar.place(x=340,y=140)

        self.principal.mainloop()

    def acao(self):
        print("Pressionado")