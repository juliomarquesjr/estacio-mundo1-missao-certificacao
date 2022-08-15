import tkinter
from tkinter import Label, Button, Entry, PhotoImage, Listbox
from tkcalendar import DateEntry

from sistema.centraliza_janelas import center
from sistema.banco import Banco

class GraficoReserva():
    def __init__(self):
        principal = tkinter.Toplevel()
        principal.geometry("400x265")
        principal.title('Reservas')
        principal.resizable(height=False, width=False)
        center(principal)

        def scan_tecnico(event):

            val = event.widget.get()

            if val == '':
                data = lista_tecnicos
            else:
                data = []
                for item in lista_tecnicos:
                    if val.lower() in item.lower():
                        data.append(item)

            atualiza_tecnico(data)

        def atualiza_tecnico(data):

            listbox_tecnico.delete(0, 'end')

            # put new data
            for item in data:
                listbox_tecnico.insert('end', item)

        def consulta_tecnicos():
            consulta = Banco().consultar_dados('tecnico')
            for valor in consulta:
                print(valor[0])

        def scan_ferramenta(event):

            val = event.widget.get()

            if val == '':
                data = lista_ferramentas
            else:
                data = []
                for item in lista_ferramentas:
                    if val.lower() in item.lower():
                        data.append(item)

            atualiza_ferramenta(data)

        def atualiza_ferramenta(data):

            listbox_ferramenta.delete(0, 'end')

            # put new data
            for item in data:
                listbox_ferramenta.insert('end', item)

        icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        icon_fechar = PhotoImage(file="assets/icones/icon_saida.png")

        lb_nome = Label(principal, text="Nome: ")
        lb_codigo = Label(principal, text="Código da Ferramenta: ")
        lb_dataretirada = Label(principal, text="Data/Retirada: ")
        lb_datadevol = Label(principal, text="Data/Devolução: ")
        lb_descricao = Label(principal, text="Descrição: ")

        nome_tecnico = Entry(principal, width=30)
        nome_tecnico.bind('<KeyRelease>', scan_tecnico)

        cod_ferramenta = Entry(principal, width=31)
        cod_ferramenta.bind('<KeyRelease>', scan_ferramenta)

        listbox_tecnico = Listbox(principal, width=30, height=5)
        listbox_ferramenta = Listbox(principal, width=31, height=5)

        sel_retirada = tkinter.StringVar()
        sel_devolucao = tkinter.StringVar()

        cx_dataretirada = DateEntry(principal, selectmode='day', textvariable=sel_retirada,date_pattern='dd/MM/yyyy', state="readonly")
        cx_datadevol = DateEntry(principal, selectmode='day', textvariable=sel_devolucao, date_pattern='dd/MM/yyyy', state="readonly")
        cx_descricao = Entry(principal, width=52)
        bt_salvar = Button(principal, text="Salvar", image=icon_salvar, compound='left', padx=5,height=22)
        bt_fechar = Button(principal, text="Fechar", image=icon_fechar, compound='left', padx=5,height=22)

        lista_tecnicos = ('Diego Gomes', 'Julio Marques', 'Kauã Marques', 'Valéria Souza')
        lista_ferramentas = ('001 - Alicate', '002 - Chave de Fenda', '003 - Chave Philips', '004 - Parafuso', '005 - Broca')
        atualiza_tecnico(lista_tecnicos)
        atualiza_ferramenta(lista_ferramentas)

        lb_nome.place(x=10, y=10)
        lb_codigo.place(x=200, y=10)
        nome_tecnico.place(x=10, y=30)
        cod_ferramenta.place(x=200, y=30)
        listbox_tecnico.place(x=10, y=60)
        listbox_ferramenta.place(x=200, y=60)

        lb_dataretirada.place(x=10, y=160)
        lb_datadevol.place(x=200, y=160)
        lb_descricao.place(x=10, y=190)

        cx_dataretirada.place(x=95, y=160)
        cx_datadevol.place(x=297, y=160)
        cx_descricao.place(x=74, y=191)

        bt_salvar.place(x=245, y=225)
        bt_fechar.place(x=320, y=225)

        principal.focus_force()
        principal.grab_set()

        principal.mainloop()