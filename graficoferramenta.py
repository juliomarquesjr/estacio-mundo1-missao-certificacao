import tkinter
from tkinter import Label, Entry, Button, messagebox, PhotoImage

from sistema.centraliza_janelas import center
from ferramenta import Ferramenta

class GraficoFerramenta():
    def __init__(self):
        self._principal = tkinter.Toplevel()   # Top Level pois ela é filha de graficomain.py
        self._principal.geometry("480x230")
        self._principal.minsize(480, 230)
        self._principal.maxsize(480, 230)
        self._principal.title('Ferramentas')
        center(self._principal)

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

        self.cxcodigo = Entry(self._principal, width=20)
        self.cxtamanho = Entry(self._principal, width=25)
        self.cxvolts = Entry(self._principal, width=20)
        self.cxund = Entry(self._principal, width=20)
        self.cxtipo = Entry(self._principal, width=20)
        self.cxmat = Entry(self._principal, width=20)
        self.cxref = Entry(self._principal, width=30)
        self.cxtemp = Entry(self._principal, width=15)
        self.cxfab = Entry(self._principal, width=35)
        self.cxdesc = Entry(self._principal, width=65)

        self.btsalvar = Button(self._principal, image=self.icon_salvar, compound='left', height=22, padx=5,
                               text="Salvar", command=self.cadastrar)
        self.btfechar = Button(self._principal, image=self.icon_sair, compound='left', height=22, padx=5,
                               text="Fechar", command=self._principal.destroy)

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

        #self._preenche_campos()
        self._principal.mainloop()

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
        else:
            tkinter.messagebox.showerror("Falha ao cadastrar", "Deu uma ruim maluco!")

    # def _preenche_campos(self):
    #     pass
    #     dados = self._carregar_ferramentas()[0]
    #
    #     if dados != False:
    #         print(dados)
    #
    #         self.cxcodigo.insert(0, dados[0])
    #         self.cxtamanho.insert(0, dados[1])
    #         self.cxvolts.insert(0, dados[2])
    #         self.cxund.insert(0, dados[3])
    #         self.cxtipo.insert(0, dados[4])
    #         self.cxmat.insert(0, dados[5])
    #         self.cxref.insert(0, dados[6])
    #         self.cxtemp.insert(0, dados[7])
    #         self.cxfab.insert(0, dados[8])
    #         self.cxdesc.insert(0, dados[9])sudo apt-get update
    # sudo apt-get install libpq-dev python-dev
    # sudo pip install psycopg2


    # def _salvar(self):
    #     resposta = self._salvar_ferramentas(dados=(self.cxcodigo.get(),
    #                                                self.cxtamanho.get(),
    #                                                self.cxvolts.get(),
    #                                                self.cxund.get(),
    #                                                self.cxtipo.get(),
    #                                                self.cxmat.get(),
    #                                                self.cxref.get(),
    #                                                self.cxtemp.get(),
    #                                                self.cxfab.get(),
    #                                                self.cxdesc.get()))
    #
    #     if resposta:
    #         tkinter.messagebox.showinfo('Salvar Ferramentas', 'Dados salvos com sucesso!')
    #     else:
    #         tkinter.messagebox.showerror('Erro ao Salvar',
    #                                      "Erro ao salvar as informações. Por favor, verifique os campos.")
    #
    #     self._principal.lift()  # Puxa a janela novamente para frente após exibir o aviso
