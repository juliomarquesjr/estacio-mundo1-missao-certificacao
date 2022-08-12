import tkinter
from tkcalendar import DateEntry

from tkinter import Label, Button, Entry, PhotoImage
from sistema.centraliza_janelas import center

class GraficoReserva():
    def __init__(self):
        self.principal = tkinter.Toplevel()
        self.principal.geometry("440x210")
        self.principal.title('Reservas')
        self.principal.resizable(height=False, width=False)
        center(self.principal)

        ## Variaveis do tkinter - Usadas no calendário
        self.sel_retirada = tkinter.StringVar()  # declaring string variable
        self.sel_devolucao = tkinter.StringVar()  # declaring string variable

        ## Labels
        self.lb_nome = Label(self.principal, text="Nome: ")
        self.lb_cpf = Label(self.principal, text="CPF: ")
        self.lb_codigo = Label(self.principal, text="Código da Ferramenta: ")
        self.lb_dataretirada = Label(self.principal, text="Data Retirada: ")
        self.lb_datadevol = Label(self.principal, text="Data Devolução: ")
        self.lb_descricao = Label(self.principal, text="Descrição: ")

        ## Icones
        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_fechar = PhotoImage(file="assets/icones/icon_saida.png")

        ## Caixas de Texto
        self.cx_nome = Entry(self.principal, width=60)
        self.cx_cpf = Entry(self.principal, width=20)
        self.cx_codigo = Entry(self.principal, width=15)
        self.cx_dataretirada = DateEntry(self.principal, selectmode='day', textvariable=self.sel_retirada, date_pattern='dd/MM/yyyy')
        self.cx_datadevol = DateEntry(self.principal, selectmode='day', textvariable=self.sel_devolucao, date_pattern='dd/MM/yyyy')
        self.cx_descricao = Entry(self.principal, width=68)

        ## Botoes
        self.bt_salvar = Button(self.principal, text="Salvar", image=self.icon_salvar, compound='left', padx=5, height=22)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_fechar, compound='left', padx=5, height=22, command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_nome.place(x=10,y=10)
        self.lb_cpf.place(x=10, y=40)
        self.lb_codigo.place(x=195, y=40)
        self.lb_dataretirada.place(x=10, y=70)
        self.lb_datadevol.place(x=215, y=70)
        self.lb_descricao.place(x=10, y=100)

        self.cx_nome.place(x=60,y=10)
        self.cx_cpf.place(x=45, y=40)
        self.cx_codigo.place(x=330, y=40)
        self.cx_dataretirada.place(x=100, y=70)
        self.cx_datadevol.place(x=330, y=70)
        self.cx_descricao.place(x=10, y=130)

        self.bt_salvar.place(x=285,y=170)
        self.bt_fechar.place(x=360,y=170)

        self.principal.focus_force()  # Mantem o focus na janela ativa
        self.principal.grab_set()  # Matem no top até ser fechada

        self.principal.mainloop()