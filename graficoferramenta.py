import tkinter

from tkinter import Label, Entry, Button, messagebox, PhotoImage

from ferramenta import Ferramenta
from sistema.centraliza_janelas import center


class GraficoFerramenta(Ferramenta):
    def __init__(self):
        #super().__init__()
        self._principal = tkinter.Toplevel() #Top Level pois ela é filha de graficomain.py
        self._principal.geometry("500x230")
        self._principal.minsize(500, 230)
        self._principal.maxsize(500, 230)
        self._principal.title('Ferramentas')
        center(self._principal)

        #self.icon_editar = PhotoImage(file="assets/icones/icon_editar.png")
        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_sair = PhotoImage(file="assets/icones/icon_saida.png")

        self.lbcodigo = Label(self._principal, text="Código: ")
        self.lbtamanho = Label(self._principal, text="Tamanho: ")
        self.lbvolts = Label(self._principal, text="Voltagem: ")
        self.lbund = Label(self._principal, text="Unidade: ")
        self.lbtipo = Label(self._principal, text="Tipo: ")
        self.lbmat = Label(self._principal, text="Material: ")
        self.lbref = Label(self._principal, text="Referência: ")
        self.lbtemp = Label(self._principal, text="Tempo Limite: ")
        self.lbfab = Label(self._principal, text="Fabricante: ")
        self.lbdesc = Label(self._principal, text="Descrição: ")

        self.cxcodigo = Entry(self._principal, width=15)
        self.cxtamanho = Entry(self._principal, width=25)
        self.cxvolts = Entry(self._principal, width=20)
        self.cxund = Entry(self._principal, width=20)
        self.cxtipo = Entry(self._principal, width=20)
        self.cxmat = Entry(self._principal, width=20)
        self.cxref = Entry(self._principal, width=30)
        self.cxtemp = Entry(self._principal, width=7)
        self.cxfab = Entry(self._principal, width=35)
        self.cxdesc = Entry(self._principal, width=65)

#bteditar = Button(principal, text="Editar", command=acao)
#btsalvar = Button(principal, text="Salvar", command=acao)
#btfechar = Button(principal, text="Fechar", command=principal.quit)

        self.bteditar = Button(self._principal, image=self.icon_editar, compound='left', height=22, padx=5,
                               text="Editar", command=self._editar)
        self.btsalvar = Button(self._principal, image=self.icon_salvar, compound='left', height=22, padx=5,
                               text="Salvar", command=self._salvar)
        self.btfechar = Button(self._principal, image=self.icon_sair, compound='left', height=22, padx=5,
                               text="Fechar", command=self._principal.destroy)

        self.lbcodigo.place(x=10, y=10)
        self.cxcodigo.place(x=60, y=10)
        self.lbtamanho.place(x=260, y=10)
        self.cxtamanho.place(x=320, y=10)
        self.lbvolts.place(x=10, y=40)
        self.cxvolts.place(x=70, y=40)
        self.lbund.place(x=295, y=40)
        self.cxund.place(x=350, y=40)
        self.lbtipo.place(x=10, y=70)
        self.cxtipo.place(x=45, y=70)
        self.lbmat.place(x=295, y=70)
        self.cxmat.place(x=350, y=70)
        self.lbref.place(x=10, y=100)
        self.cxref.place(x=75, y=100)
        self.lbtemp.place(x=340, y=100)
        self.cxtemp.place(x=425, y=100)
        self.lbfab.place(x=10, y=130)
        self.cxfab.place(x=75, y=130)
        self.lbdesc.place(x=10, y=160)
        self.cxdesc.place(x=75, y=160)
        self.bteditar.place(x=10, y=195)
        self.btsalvar.place(x=390, y=195)
        self.btfechar.place(x=440, y=195)

        if __name__ == "__main__":
            GraficoFerramenta()
