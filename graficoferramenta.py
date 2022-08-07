import tkinter
from tkinter import Label, Entry, Button, messagebox, PhotoImage

from sistema.centraliza_janelas import center

class GraficoFerramenta():
    def __init__(self):
        self._principal = tkinter.Toplevel()   # Top Level pois ela é filha de graficomain.py
        self._principal.geometry("500x230")
        self._principal.minsize(500, 230)
        self._principal.maxsize(500, 230)
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

        self.cxcodigo = Entry(self._principal, width=15)
        self.cxtamanho = Entry(self._principal, width=15)
        self.cxvolts = Entry(self._principal, width=15)
        self.cxund = Entry(self._principal, width=15)
        self.cxtipo = Entry(self._principal, width=15)
        self.cxmat = Entry(self._principal, width=15)
        self.cxref = Entry(self._principal, width=15)
        self.cxtemp = Entry(self._principal, width=10)
        self.cxfab = Entry(self._principal, width=15)
        self.cxdesc = Entry(self._principal, width=15)

        self.btsalvar = Button(self._principal, image=self.icon_salvar, compound='left', height=22, padx=5,
                               text="Salvar")
        self.btfechar = Button(self._principal, image=self.icon_sair, compound='left', height=22, padx=5,
                               text="Fechar", command=self._principal.destroy)

        self.lbcodigo.place(x=7, y=40)
        self.cxcodigo.place(x=60, y=40)
        self.lbtamanho.place(x=260, y=10)
        self.cxtamanho.place(x=327, y=10)
        self.lbvolts.place(x=9, y=70)
        self.cxvolts.place(x=80, y=70)
        self.lbund.place(x=260, y=40)
        self.cxund.place(x=320, y=40)
        self.lbtipo.place(x=7, y=10)
        self.cxtipo.place(x=45, y=10)
        self.lbmat.place(x=265, y=70)
        self.cxmat.place(x=327, y=70)
        self.lbref.place(x=10, y=100)
        self.cxref.place(x=87, y=100)
        self.lbtemp.place(x=280, y=100)
        self.cxtemp.place(x=380, y=100)
        self.lbfab.place(x=10, y=130)
        self.cxfab.place(x=85, y=130)
        self.lbdesc.place(x=10, y=160)
        self.cxdesc.place(x=80, y=160)
        self.btsalvar.place(x=10, y=190)
        self.btfechar.place(x=400, y=190)

        self._preenche_campos()
        self._principal.mainloop()

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
