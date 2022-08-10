import tkinter
from tkinter import Label, Entry, Button, messagebox, PhotoImage

from sistema.centraliza_janelas import center
from ferramenta import Ferramenta

class GraficoFerramenta():
    def __init__(self):
        self.principal = tkinter.Toplevel()   # Top Level pois ela é filha de graficomain.py
        self.principal.geometry("480x230")
        self.principal.minsize(480, 230)
        self.principal.maxsize(480, 230)
        self.principal.title('Ferramentas')
        center(self.principal)

        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_sair = PhotoImage(file="assets/icones/icon_saida.png")

        self.lbcodigo = Label(self.principal, text="Código: ")
        self.lbtamanho = Label(self.principal, text="Tamanho: ")
        self.lbvolts = Label(self.principal, text="Voltagem: ")
        self.lbund = Label(self.principal, text="Unidade: ")
        self.lbtipo = Label(self.principal, text="Tipo: ")
        self.lbmat = Label(self.principal, text="Material: ")
        self.lbref = Label(self.principal, text="Referência: ")
        self.lbtemp = Label(self.principal, text="Tempo Limite: ")
        self.lbfab = Label(self.principal, text="Fabricante: ")
        self.lbdesc = Label(self.principal, text="Descrição: ")

        self.cxcodigo = Entry(self.principal, width=20)
        self.cxtamanho = Entry(self.principal, width=25)
        self.cxvolts = Entry(self.principal, width=20)
        self.cxund = Entry(self.principal, width=20)
        self.cxtipo = Entry(self.principal, width=20)
        self.cxmat = Entry(self.principal, width=20)
        self.cxref = Entry(self.principal, width=30)
        self.cxtemp = Entry(self.principal, width=15)
        self.cxfab = Entry(self.principal, width=35)
        self.cxdesc = Entry(self.principal, width=65)

        self.btsalvar = Button(self.principal, image=self.icon_salvar, compound='left', height=22, padx=5,
                               text="Salvar", command=self.cadastrar)
        self.btfechar = Button(self.principal, image=self.icon_sair, compound='left', height=22, padx=5,
                               text="Fechar", command=self.principal.destroy)

        self.lbtipo.place(x=10, y=10)
        self.cxtipo.place(x=47, y=10)
        self.lbtamanho.place(x=250, y=10)
        self.cxtamanho.place(x=315, y=10)
        self.lbcodigo.place(x=10, y=40)
        self.cxcodigo.place(x=65, y=40)
        self.lbund.place(x=285, y=40)
        self.cxund.place(x=345, y=40)
        self.lbvolts.place(x=10, y=70)
        self.cxvolts.place(x=75, y=70)
        self.lbmat.place(x=287, y=70)
        self.cxmat.place(x=345, y=70)
        self.lbref.place(x=10, y=100)
        self.cxref.place(x=80, y=100)
        self.lbtemp.place(x=290, y=100)
        self.cxtemp.place(x=375, y=100)
        self.lbfab.place(x=10, y=130)
        self.cxfab.place(x=80, y=130)
        self.lbdesc.place(x=10, y=160)
        self.cxdesc.place(x=75, y=160)
        self.btsalvar.place(x=325, y=190)
        self.btfechar.place(x=400, y=190)

        self.principal.focus_force()  # Mantem o focus na janela ativa
        self.principal.grab_set()  # Matem no top até ser fechada

        self.principal.mainloop()

    def cadastrar(self):
        self.nova_ferramenta = Ferramenta(self.cxcodigo.get(),
                                          self.cxdesc.get(),
                                          self.cxfab.get(),
                                          self.cxvolts.get(),
                                          self.cxref.get(),
                                          self.cxtamanho.get(),
                                          self.cxund.get(),
                                          self.cxtipo.get(),
                                          self.cxmat.get(),
                                          self.cxtemp.get())

        if self.nova_ferramenta.cadastra_banco():
            tkinter.messagebox.showinfo("Cadastro de Ferramenta", "Cadastro realizado com sucesso!")
            self.principal.destroy()
        else:
            tkinter.messagebox.showerror("Falha ao cadastrar", "Deu uma ruim maluco!")
            self.principal.lift()

