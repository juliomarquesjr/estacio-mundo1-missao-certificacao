import tkinter
from tkinter import Label, Button, Entry, PhotoImage, Listbox, Scrollbar, messagebox
from tkcalendar import DateEntry
import datetime
from  datetime import date

from sistema.centraliza_janelas import center

from reserva import Reserva
from sistema.enviaEmail import Email

class GraficoReserva:
    def __init__(self, codigo=False):
        self.principal = tkinter.Toplevel()
        self.principal.geometry("535x265")
        self.principal.title('Reservas')
        self.principal.resizable(height=False, width=False)
        center(self.principal)
        self.codigo = codigo

        def exibe_tecnicos(tecnicos):
            self.listbox_tecnico.delete(0, 'end')
            codigos_tecnicos = []
            for item in tecnicos:
                self.listbox_tecnico.insert('end', f'{item[1]} > {item[0]}')
                codigos_tecnicos.append(item[1])

            return codigos_tecnicos

        def exibe_ferramentas(ferramentas):
            self.listbox_ferramenta.delete(0, 'end')
            print(ferramentas)
            codigos_ferramentas = []

            for item in ferramentas:
                self.listbox_ferramenta.insert('end', f'{item[9]} > {item[0]}')
                codigos_ferramentas.append(item[0])

            return codigos_ferramentas

        def selecionatecnico(event):
            self.selection1 = event.widget.curselection()
            self.index1 = self.selection1[0]
            self.value1 = event.widget.get(self.index1)
            self.lb_tecnicosel = Label(self.principal, text = self.value1)
            self.texto_lb_tecnico = self.value1
            self.lb_tecnicosel.place(x=10, y=34)
            self.listbox_tecnico.configure(state=tkinter.DISABLED)

        def selecionaferramenta(event):
            self.selection2 = event.widget.curselection()
            self.index2 = self.selection2[0]
            self.value2 = event.widget.get(self.index2)
            self.lb_ferramentasel = Label(self.principal, text = self.value2)
            self.texto_lb_ferramenta = self.value2
            self.lb_ferramentasel.place(x=270, y=34)
            self.listbox_ferramenta.configure(state=tkinter.DISABLED)

        ## Icones
        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_fechar = PhotoImage(file="assets/icones/icon_saida.png")

        self.texto_lb_tecnico = tkinter.StringVar()
        self.texto_lb_tecnico = ""
        self.texto_lb_ferramenta = tkinter.StringVar()
        self.texto_lb_ferramenta = ""

        ## Labels
        self.lb_tecnicosel = Label(self.principal, text=self.texto_lb_tecnico)
        self.lb_ferramentasel = Label(self.principal, text=self.texto_lb_ferramenta)

        self.lb_nome = Label(self.principal, text="Nome: ")
        self.lb_codigo = Label(self.principal, text="Código da Ferramenta: ")
        self.lb_dataretirada = Label(self.principal, text="Data/Retirada: ")
        self.lb_datadevol = Label(self.principal, text="Data/Devolução: ")
        self.lb_descricao = Label(self.principal, text="Descrição: ")

        ## Listas
        self.listbox_tecnico = Listbox(self.principal, width=39, height=5)
        self.listbox_ferramenta = Listbox(self.principal, width=41, height=5)
        self.listbox_tecnico.bind('<<ListboxSelect>>', selecionatecnico)
        self.listbox_ferramenta.bind('<<ListboxSelect>>', selecionaferramenta)

        self.scrolltecnico = Scrollbar(self.principal)
        self.scrolltecnico.place(x=230, y=60,height=85)
        self.listbox_tecnico.config(yscrollcommand=self.scrolltecnico.set)
        self.scrolltecnico.config(command=self.listbox_tecnico.yview)

        self.scrollferramenta = Scrollbar(self.principal)
        self.scrollferramenta.place(x=502, y=60, height=85)
        self.listbox_ferramenta.config(yscrollcommand=self.scrollferramenta.set)
        self.scrollferramenta.config(command=self.listbox_tecnico.yview)

        sel_retirada = tkinter.StringVar()
        sel_devolucao = tkinter.StringVar()

        self.cx_dataretirada = DateEntry(self.principal, selectmode='day', textvariable=sel_retirada,date_pattern='dd/MM/yyyy', state="readonly")
        self.cx_datadevol = DateEntry(self.principal, selectmode='day', textvariable=sel_devolucao, date_pattern='dd/MM/yyyy', state="readonly")
        self.cx_temp_retirada = Entry(self.principal, width=8)
        self.cx_temp_retirada.bind("<KeyRelease>", self.format_tempo_retirada)
        self.cx_temp_devolucao = Entry(self.principal, width=8)
        self.cx_temp_devolucao.bind("<KeyRelease>", self.format_tempo_devolucao)
        self.cx_descricao = Entry(self.principal, width=74)

        ## Botoes
        self.bt_salvar = Button(self.principal, text="Salvar", image=self.icon_salvar, compound='left', padx=5,height=22, command=self.salvar)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_fechar, compound='left', padx=5,height=22, command=self.principal.destroy)

        self.lista_tecnicos = Reserva().listar_tecnicos_cadastrados
        self.lista_ferramentas = Reserva().listar_ferramentas_cadastradas

        self.lista_codigos_tecnicos = exibe_tecnicos(self.lista_tecnicos())
        self.lista_codigos_ferramentas = exibe_ferramentas(self.lista_ferramentas())

        ## Alinhamento dos elementos
        self.lb_nome.place(x=10, y=12)
        self.lb_codigo.place(x=270, y=12)
        self.listbox_tecnico.place(x=10, y=62)
        self.listbox_ferramenta.place(x=270, y=60)

        self.lb_dataretirada.place(x=10, y=160)
        self.lb_datadevol.place(x=270, y=160)
        self.lb_descricao.place(x=10, y=190)

        self.cx_dataretirada.place(x=95, y=160)
        self.cx_temp_retirada.place(x=194, y=161)
        self.cx_datadevol.place(x=370, y=160)
        self.cx_temp_devolucao.place(x=469, y=161)
        self.cx_descricao.place(x=74, y=191)

        self.bt_salvar.place(x=377, y=225)
        self.bt_fechar.place(x=455, y=225)

        self.principal.focus_force()
        self.principal.grab_set()

        if self.codigo:
            self.preencher_campos()

        self.principal.mainloop()

    def salvar(self):
        if self.codigo == False:
            self.cadastrar()
        else:
            self.editar()

    def preencher_campos(self):
        self.dados = Reserva().consulta_banco(self.codigo)
        self.lb_tecnicosel = Label(self.principal, text=self.dados[0][0] + ' > ' + self.dados[0][1])
        self.lb_tecnicosel.place(x=10, y=34)
        self.lb_ferramentasel = Label(self.principal, text=self.dados[0][2] + ' > ' + self.dados[0][3])
        self.lb_ferramentasel.place(x=270, y=34)
        x1 = self.dados[0][4]
        y1 = x1.split("/")
        z1 = list(map(int, y1))
        dt1 = date(z1[2], z1[1], z1[0])
        self.cx_dataretirada.set_date(dt1)
        self.cx_temp_retirada.insert(0, self.dados[0][5])
        x2 = self.dados[0][6]
        y2 = x2.split("/")
        z2 = list(map(int, y2))
        dt2 = date(z2[2], z2[1], z2[0])
        self.cx_datadevol.set_date(dt2)
        self.cx_temp_devolucao.insert(0, self.dados[0][7])
        self.cx_descricao.insert(0, self.dados[0][8])

    def format_tempo_retirada(self, event=None):
        texto = self.cx_temp_retirada.get().replace(".", "").replace("-", "")[:6]
        novo_texto = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(texto)):
            if not texto[index] in "0123456789": continue
            if index in [1]:
                novo_texto += texto[index] + ":"
            elif index == 4:
                novo_texto += texto[index] + ":00"
            else:
                novo_texto += texto[index]

        self.cx_temp_retirada.delete(0, "end")
        self.cx_temp_retirada.insert(0, novo_texto)

    def format_tempo_devolucao(self, event=None):
        texto = self.cx_temp_devolucao.get().replace(".", "").replace("-", "")[:6]
        novo_texto = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(texto)):
            if not texto[index] in "0123456789": continue
            if index in [1]:
                novo_texto += texto[index] + ":"
            elif index == 4:
                novo_texto += texto[index] + ":00"
            else:
                novo_texto += texto[index]

        self.cx_temp_devolucao.delete(0, "end")
        self.cx_temp_devolucao.insert(0, novo_texto)

    def validar_tempo(self, dataretirada, tempretirada, datadevolucao,tempdevolucao, tempolimite):
        print(dataretirada)#20/08/2022
        print(tempretirada)#11:00:00
        print(datadevolucao)#24/08/2022
        print(tempdevolucao)#12:00:00
        #x = dataretirada.split("/")
        #print(x)
        #d2 = datetime.date(x[2], int(x[1]), int(x[0]))
        #print(d2)
        #y = dataretirada.split("/")
        #print(y)
        #d1 = datetime.date(y[2], int(y[1]), int(y[0]))
        #print(d1)
        #quantidade_dias = abs((d2 - d1).days) - 1
        #print(quantidade_dias)


        tempopedido = 1
        if tempopedido < tempolimite:
            return True
        else:
            return False

    def cadastrar(self):
        x = 10
        resultado = self.validar_tempo(self.cx_dataretirada.get(), self.cx_temp_retirada.get(),self.cx_datadevol.get(), self.cx_temp_devolucao.get(),x)
        tecnico = self.texto_lb_tecnico.split(' > ')
        ferramenta = self.texto_lb_ferramenta.split(' > ')
        if resultado == True:
            if (tecnico and ferramenta and self.cx_dataretirada.get() and self.cx_temp_retirada.get() and self.cx_datadevol.get() and self.cx_temp_devolucao.get() and self.cx_descricao.get()) == '':
                tkinter.messagebox.showerror("Validação de campos",
                                             "Um ou mais campos estão em branco. Verifique os campos e tente novamente.",
                                             parent=self.principal)
            else:
                nova_reserva = Reserva(tecnico[0],
                                            tecnico[1],
                                            ferramenta[0],
                                            ferramenta[1],
                                            self.cx_dataretirada.get(),
                                            self.cx_temp_retirada.get(),
                                            self.cx_datadevol.get(),
                                            self.cx_temp_devolucao.get(),
                                            self.cx_descricao.get())

                if nova_reserva.reservar_ferramenta():
                    tkinter.messagebox.showinfo("Cadastro de Reserva", "Reserva cadastrada com sucesso!",
                                                parent=self.principal)

                    mensagem = f"Nova reserva: CPF: {tecnico[0]} / Tecnico: {tecnico[1]} / Ferramenta: {ferramenta[1]} / " \
                               f"Retirada: {self.cx_dataretirada.get()} - {self.cx_temp_retirada.get()} / Devolução: {self.cx_datadevol.get()} - {self.cx_temp_devolucao.get()} / " \
                               f"Descrição: {self.cx_descricao.get()}"
                    email = Email()
                    email.enviar_mensagem(mensagem=mensagem)

                    if email:
                        tkinter.messagebox.showinfo("Envio de mensagem", f"Uma mensagem foi enviada para: {email.get_email_destinatario()}", parent=self.principal)
                    self.principal.destroy()
                else:
                    tkinter.messagebox.showerror("Falha ao cadastrar",
                                                 "Ocorreu um erro ao cadastrar a reserva, por favor, verifique os campos e tente novamente!",
                                                 parent=self.principal)
                    self.principal.lift()
        else:
            tkinter.messagebox.showerror("Falha ao cadastrar",
                                         "Tempo de reserva não permitido, insira outro!",
                                         parent=self.principal)


    def editar(self):
        x = 10
        resultado = self.validar_tempo(self.cx_dataretirada.get(), self.cx_temp_retirada.get(), self.cx_datadevol.get(),self.cx_temp_devolucao.get(), x)
        tecnico = self.texto_lb_tecnico.split(' > ')
        ferramenta = self.texto_lb_ferramenta.split(' > ')
        if resultado == True:
            if (
                    tecnico and ferramenta and self.cx_dataretirada.get() and self.cx_temp_retirada.get() and self.cx_datadevol.get() and self.cx_temp_devolucao.get() and self.cx_descricao.get()) == '':
                tkinter.messagebox.showerror("Validação de campos",
                                             "Um ou mais campos estão em branco. Verifique os campos e tente novamente",
                                             parent=self.principal)
            else:
                self.atualiza = Reserva().atualiza_banco(set=(f"cpf_tecnico = '{tecnico[0]}',"
                                                              f"nome_tecnico = '{tecnico[1]}',"
                                                              f"cod_ferramenta = '{ferramenta[0]}',"
                                                              f"nome_ferramenta = '{ferramenta[1]}',"
                                                              f"data_retirada = '{self.cx_dataretirada.get()}',"
                                                              f"hora_retirada = '{self.cx_temp_retirada.get()}',"
                                                              f"data_devolucao = '{self.cx_datadevol.get()}',"
                                                              f"hora_devolucao = '{self.cx_temp_devolucao.get()}',"
                                                              f"descricao = '{self.cx_descricao.get()}'"),
                                                         where=f"id = '{self.codigo}'")
                if self.atualiza:
                    tkinter.messagebox.showinfo("Editar reserva", "Reserva editada com sucesso!", parent=self.principal)
                    self.principal.destroy()
                else:
                    tkinter.messagebox.showerror("Falha ao editar",
                                                 "Não foi possível editar a reserva. Por favor, tente novamente.",
                                                 parent=self.principal)
                    self.principal.lift()
        else:
            tkinter.messagebox.showerror("Falha ao editar",
                                         "Tempo de reserva não permitido, insira outro!",
                                         parent=self.principal)