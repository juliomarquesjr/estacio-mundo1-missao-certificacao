import tkinter
from tkinter import Label, Button, Entry, PhotoImage, Listbox
from tkcalendar import DateEntry

from sistema.centraliza_janelas import center

from reserva import Reserva

class GraficoReserva(Reserva):
    def __init__(self):
        self.principal = tkinter.Toplevel()
        self.principal.geometry("400x265")
        self.principal.title('Reservas')
        self.principal.resizable(height=False, width=False)
        center(self.principal)

        def scan_tecnico(event):
            val = event.widget.get()

            if val == '':
                data = lista_tecnicos
            else:
                data = []
                for item in lista_tecnicos:
                    if val.lower() in item.lower():
                        data.append(item)

            exibe_tecnicos(data)

        def scan_ferramenta(event):
            val = event.widget.get()

            if val == '':
                data = lista_ferramentas
            else:
                data = []
                for item in lista_ferramentas:
                    if val.lower() in item.lower():
                        data.append(item)

            exibe_ferramentas(data)

        def exibe_tecnicos(tecnicos):
            self.listbox_tecnico.delete(0, 'end')
            codigos_tecnicos = []
            for item in tecnicos:
                self.listbox_tecnico.insert('end', item[0])
                codigos_tecnicos.append(item[1])

            return codigos_tecnicos

        def exibe_ferramentas(ferramentas):
            self.listbox_ferramenta.delete(0, 'end')
            codigos_ferramentas = []

            for item in ferramentas:
                self.listbox_ferramenta.insert('end', f'{item[0]} - {item[1]}')
                codigos_ferramentas.append(item[0])

            return codigos_ferramentas

        ## Icones
        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_fechar = PhotoImage(file="assets/icones/icon_saida.png")

        ## Labels
        self.lb_nome = Label(self.principal, text="Nome: ")
        self.lb_codigo = Label(self.principal, text="Código da Ferramenta: ")
        self.lb_dataretirada = Label(self.principal, text="Data/Retirada: ")
        self.lb_datadevol = Label(self.principal, text="Data/Devolução: ")
        self.lb_descricao = Label(self.principal, text="Descrição: ")

        ## Caixas de texto
        self.nome_tecnico = Entry(self.principal, width=30)
        self.nome_tecnico.bind('<KeyRelease>', scan_tecnico)

        self.cod_ferramenta = Entry(self.principal, width=31)
        self.cod_ferramenta.bind('<KeyRelease>', scan_ferramenta)

        ## Listas
        self.listbox_tecnico = Listbox(self.principal, width=30, height=5)
        self.listbox_ferramenta = Listbox(self.principal, width=31, height=5)

        sel_retirada = tkinter.StringVar()
        sel_devolucao = tkinter.StringVar()

        self.cx_dataretirada = DateEntry(self.principal, selectmode='day', textvariable=sel_retirada,date_pattern='dd/MM/yyyy', state="readonly")
        self.cx_datadevol = DateEntry(self.principal, selectmode='day', textvariable=sel_devolucao, date_pattern='dd/MM/yyyy', state="readonly")
        self.cx_descricao = Entry(self.principal, width=52)
        self.bt_salvar = Button(self.principal, text="Salvar", image=self.icon_salvar, compound='left', padx=5,height=22, command=self.salvar_reserva)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_fechar, compound='left', padx=5,height=22, command=self.principal.destroy)

        lista_tecnicos = self.listar_tecnicos_cadastrados()
        lista_ferramentas = self.listar_ferramentas_cadastradas()

        self.lista_codigos_tecnicos = exibe_tecnicos(lista_tecnicos)
        self.lista_codigos_ferramentas = exibe_ferramentas(lista_ferramentas)

        ## Alinhamento dos elementos
        self.lb_nome.place(x=10, y=10)
        self.lb_codigo.place(x=200, y=10)
        self.nome_tecnico.place(x=10, y=30)
        self.cod_ferramenta.place(x=200, y=30)
        self.listbox_tecnico.place(x=10, y=60)
        self.listbox_ferramenta.place(x=200, y=60)

        self.lb_dataretirada.place(x=10, y=160)
        self.lb_datadevol.place(x=200, y=160)
        self.lb_descricao.place(x=10, y=190)

        self.cx_dataretirada.place(x=95, y=160)
        self.cx_datadevol.place(x=297, y=160)
        self.cx_descricao.place(x=74, y=191)

        self.bt_salvar.place(x=245, y=225)
        self.bt_fechar.place(x=320, y=225)

        self.principal.focus_force()
        self.principal.grab_set()

        self.principal.mainloop()

    def salvar_reserva(self):
        tecnico_selecionado = False
        ferramenta_selecionada = False

        for item in self.listbox_ferramenta.curselection():
            ferramenta_selecionada = self.lista_codigos_ferramentas[item]

        for item in self.listbox_tecnico.curselection():
            tecnico_selecionado = self.lista_codigos_tecnicos[item]

        cadastro = self.reservar_ferramenta(tecnico_selecionado, ferramenta_selecionada, self.cx_dataretirada, self.cx_datadevol)