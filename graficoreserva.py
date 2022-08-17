import tkinter
from tkinter import Label, Button, Entry, PhotoImage, Listbox, Scrollbar, Frame
from tkcalendar import DateEntry

from sistema.centraliza_janelas import center

from reserva import Reserva

class GraficoReserva(Reserva):
    def __init__(self):
        self.principal = tkinter.Toplevel()
        self.principal.geometry("450x265")
        self.principal.title('Reservas')
        self.principal.resizable(height=False, width=False)
        center(self.principal)

        def exibe_tecnicos(tecnicos):
            self.listbox_tecnico.delete(0, 'end')
            codigos_tecnicos = []
            for item in tecnicos:
                self.listbox_tecnico.insert('end', f'{item[1]} - {item[0]}')
                codigos_tecnicos.append(item[1])

            return codigos_tecnicos

        def exibe_ferramentas(ferramentas):
            self.listbox_ferramenta.delete(0, 'end')
            codigos_ferramentas = []

            for item in ferramentas:
                self.listbox_ferramenta.insert('end', f'{item[0]} - {item[1]}')
                codigos_ferramentas.append(item[0])

            return codigos_ferramentas

        def selecionatecnico(event):
            self.selection1 = event.widget.curselection()
            self.index1 = self.selection1[0]
            self.value1 = event.widget.get(self.index1)
            self.lb_tecnicosel = Label(self.principal, text = self.value1)
            self.lb_tecnicosel.place(x=10, y=34)
            self.listbox_tecnico.configure(state=tkinter.DISABLED)

        def selecionaferramenta(event):
            self.selection2 = event.widget.curselection()
            self.index2 = self.selection2[0]
            self.value2 = event.widget.get(self.index2)
            self.lb_ferramentasel = Label(self.principal, text = self.value2)
            self.lb_ferramentasel.place(x=250, y=34)
            self.listbox_ferramenta.configure(state=tkinter.DISABLED)

        ## Icones
        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_fechar = PhotoImage(file="assets/icones/icon_saida.png")

        ## Labels
        self.lb_nome = Label(self.principal, text="Nome: ")
        self.lb_codigo = Label(self.principal, text="Código da Ferramenta: ")
        self.lb_dataretirada = Label(self.principal, text="Data/Retirada: ")
        self.lb_datadevol = Label(self.principal, text="Data/Devolução: ")
        self.lb_descricao = Label(self.principal, text="Descrição: ")

        ## Listas
        self.listbox_tecnico = Listbox(self.principal, width=36, height=5)
        self.listbox_ferramenta = Listbox(self.principal, width=31, height=5)
        self.listbox_tecnico.bind('<<ListboxSelect>>', selecionatecnico)
        self.listbox_ferramenta.bind('<<ListboxSelect>>', selecionaferramenta)

        self.scrolltecnico = Scrollbar(self.principal)
        self.scrolltecnico.place(x=223, y=60,height=85)
        self.listbox_tecnico.config(yscrollcommand=self.scrolltecnico.set)
        self.scrolltecnico.config(command=self.listbox_tecnico.yview)

        self.scrollferramenta = Scrollbar(self.principal)
        self.scrollferramenta.place(x=422, y=60, height=85)
        self.listbox_ferramenta.config(yscrollcommand=self.scrollferramenta.set)
        self.scrollferramenta.config(command=self.listbox_tecnico.yview)

        sel_retirada = tkinter.StringVar()
        sel_devolucao = tkinter.StringVar()

        self.cx_dataretirada = DateEntry(self.principal, selectmode='day', textvariable=sel_retirada,date_pattern='dd/MM/yyyy', state="readonly")
        self.cx_datadevol = DateEntry(self.principal, selectmode='day', textvariable=sel_devolucao, date_pattern='dd/MM/yyyy', state="readonly")
        self.cx_descricao = Entry(self.principal, width=59)
        self.bt_salvar = Button(self.principal, text="Salvar", image=self.icon_salvar, compound='left', padx=5,height=22)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_fechar, compound='left', padx=5,height=22, command=self.principal.destroy)

        lista_tecnicos = self.listar_tecnicos_cadastrados()
        lista_ferramentas = self.listar_ferramentas_cadastradas()

        self.lista_codigos_tecnicos = exibe_tecnicos(lista_tecnicos)
        self.lista_codigos_ferramentas = exibe_ferramentas(lista_ferramentas)

        ## Alinhamento dos elementos
        self.lb_nome.place(x=10, y=12)
        self.lb_codigo.place(x=250, y=10)
        self.listbox_tecnico.place(x=10, y=62)
        self.listbox_ferramenta.place(x=250, y=60)

        self.lb_dataretirada.place(x=10, y=160)
        self.lb_datadevol.place(x=243, y=160)
        self.lb_descricao.place(x=10, y=190)

        self.cx_dataretirada.place(x=95, y=160)
        self.cx_datadevol.place(x=342, y=160)
        self.cx_descricao.place(x=74, y=191)

        self.bt_salvar.place(x=295, y=225)
        self.bt_fechar.place(x=370, y=225)

        self.principal.focus_force()
        self.principal.grab_set()

        self.principal.mainloop()