import tkinter
from tkinter import Label, Entry, Button, messagebox, PhotoImage

from sistema.centraliza_janelas import center
from ferramenta import Ferramenta
from sistema.banco import Banco

class GraficoFerramenta:
    def __init__(self, codigo_ferramenta=False):
        self.principal = tkinter.Toplevel()   # Top Level pois ela é filha de graficomain.py

        ## Ajustar tamanho da janela e não permitir maximizar.
        self.principal.geometry("570x200")
        self.principal.resizable(width=False, height=False)

        self.cod_ferramenta = codigo_ferramenta
        self.principal.title('Ferramentas')
        center(self.principal)

        ## Icones
        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_sair = PhotoImage(file="assets/icones/icon_saida.png")

        ## Labels.
        self.lb_codigo = Label(self.principal, text="Código: ")
        self.lb_desc = Label(self.principal, text="Descrição: ")
        self.lb_fab = Label(self.principal, text="Fabricante: ")
        self.lb_volts = Label(self.principal, text="Voltagem: ")
        self.lb_ref = Label(self.principal, text="Part Number: ")
        self.lb_tamanho = Label(self.principal, text="Tamanho: ")
        self.lb_und = Label(self.principal, text="Unidade: ")
        self.lb_tipo = Label(self.principal, text="Tipo: ")
        self.lb_mat = Label(self.principal, text="Material: ")
        self.lb_temp = Label(self.principal, text="Tempo Limite: ")

        ## Caixas de texto.
        self.cx_codigo = Entry(self.principal, width=30)
        self.cx_desc = Entry(self.principal, width=76)
        self.cx_fab = Entry(self.principal, width=30)
        self.cx_volts = Entry(self.principal, width=30)
        self.cx_ref = Entry(self.principal, width=30)
        self.cx_tamanho = Entry(self.principal, width=30)
        self.cx_und = Entry(self.principal, width=15)
        self.cx_tipo = Entry(self.principal, width=15)
        self.cx_mat = Entry(self.principal, width=30)
        self.cx_temp = Entry(self.principal, width=15)

        ## Botões.
        self.btsalvar = Button(self.principal, image=self.icon_salvar, compound='left', height=22, padx=5,
                               text="Salvar", command=self.salvar)
        self.btfechar = Button(self.principal, image=self.icon_sair, compound='left', height=22, padx=5,
                               text="Fechar", command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_codigo.place(x=10, y=10)
        self.cx_codigo.place(x=95, y=10)
        self.lb_mat.place(x=300, y=10)
        self.cx_mat.place(x=370, y=10)
        self.lb_fab.place(x=10, y=40)
        self.cx_fab.place(x=95, y=40)
        self.lb_volts.place(x=300, y=40)
        self.cx_volts.place(x=370, y=40)
        self.lb_ref.place(x=10, y=70)
        self.cx_ref.place(x=95, y=70)
        self.lb_tamanho.place(x=300, y=70)
        self.cx_tamanho.place(x=370, y=70)
        self.lb_und.place(x=10, y=100)
        self.cx_und.place(x=95, y=100)
        self.lb_tipo.place(x=210, y=100)
        self.cx_tipo.place(x=250, y=100)
        self.lb_temp.place(x=370, y=100)
        self.cx_temp.place(x=460, y=100)
        self.lb_desc.place(x=10, y=130)
        self.cx_desc.place(x=95, y=130)

        self.btsalvar.place(x=407, y=160)
        self.btfechar.place(x=485, y=160)

        self.principal.focus_force()  # Mantem o focus na janela ativa
        self.principal.grab_set()  # Matem no top até ser fechada

        ## Se estiver o código da ferramenta, preenche os campos ativando o modo Edição
        if self.cod_ferramenta:
            self.preencher_campo()

        self.principal.focus_force()  # Mantem o focus na janela ativa
        self.principal.grab_set()  # Matem no top até ser fechada

        self.principal.mainloop()

    ## Função para verificar se está no modo edição para salvar ou atualizar no banco
    def salvar(self):
        if self.cod_ferramenta == False:
            self.cadastrar()
        else:
            self.editar()

    def cadastrar(self):
        self.nova_ferramenta = Ferramenta(self.cx_codigo.get(),
                                          self.cx_desc.get(),
                                          self.cx_fab.get(),
                                          self.cx_volts.get(),
                                          self.cx_ref.get(),
                                          self.cx_tamanho.get(),
                                          self.cx_und.get(),
                                          self.cx_tipo.get(),
                                          self.cx_mat.get(),
                                          self.cx_temp.get())

        if self.nova_ferramenta.cadastra_banco():
            tkinter.messagebox.showinfo("Cadastro de Ferramenta", "Cadastro realizado com sucesso!", parent=self.principal)
            self.principal.destroy()
        else:
            tkinter.messagebox.showerror("Falha ao cadastrar", "Erro ao salvar os dados. Por favor, verifique os campos novamente!", parent=self.principal)
            self.principal.lift()

    def editar(self):
        self.atualiza = Banco().atualizar_dados('ferramenta', set= f"descricao_ferramenta = '{self.cx_desc.get()}',"
                                                                f"fabricante = '{self.cx_fab.get()}',"
                                                                f"voltagem = '{self.cx_volts.get()}',"
                                                                f"part_number = '{self.cx_ref.get()}',"
                                                                f"tamanho = '{self.cx_tamanho.get()}',"
                                                                f"und_medida = '{self.cx_und.get()}',"
                                                                f"tipo_ferramenta = '{self.cx_tipo.get()}',"
                                                                f"material_ferramenta = '{self.cx_mat.get()}',"
                                                                f"tempo_max_reserva = '{self.cx_temp.get()}'",where=f"cod_ferramenta = '{self.cx_codigo.get()}'")

        if self.atualiza:
            tkinter.messagebox.showinfo("Editar ferramenta", "Ferramenta Editada com Sucesso!", parent=self.principal)
            self.principal.destroy()
        else:
            tkinter.messagebox.showerror("Falha ao editar", "Não foi possível editar a ferramenta. Por favor, tente novamente.", parent=self.principal)
            self.principal.lift()

    def preencher_campo(self):
        self.dados = Banco().consultar_dados(tabela='ferramenta',
                                                where=f"cod_ferramenta = {self.cod_ferramenta}")
        self.cx_codigo.insert(0, self.dados[0][0])
        self.cx_codigo.config(state='disabled')
        self.cx_desc.insert(0, self.dados[0][1])
        self.cx_fab.insert(0, self.dados[0][2])
        self.cx_volts.insert(0, self.dados[0][3])
        self.cx_ref.insert(0, self.dados[0][4])
        self.cx_tamanho.insert(0, self.dados[0][5])
        self.cx_und.insert(0, self.dados[0][6])
        self.cx_tipo.insert(0, self.dados[0][7])
        self.cx_mat.insert(0, self.dados[0][8])
        self.cx_temp.insert(0, self.dados[0][9])