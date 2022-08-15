import tkinter
from tkinter import Label, PhotoImage, Button, messagebox, Entry
from tkinter.ttk import Treeview
import tkinter as tk
import tkinter.font as tkFont

from graficoconfig import GraficoConfig
from graficoconsferramenta import GraficoConsultaFerramenta
from graficoconstecnico import GraficoConsultaTecnico
from graficoreserva import GraficoReserva

from sistema.centraliza_janelas import center

class GraficoMain:
    def __init__(self):
        self.principal = tkinter.Tk()

        ## Ajustar tamanho da janela e não permitir maximizar
        self.principal.geometry("800x440")
        self.principal.resizable(width=False, height=False)

        self.principal.title('Conteúdo Audiovisual LTDA')
        center(self.principal)

        ## Icones
        self.icon_config = PhotoImage(file="assets/icones/icon_config.png")
        self.icon_saida = PhotoImage(file="assets/icones/icon_saida.png")
        self.icon_reserva = PhotoImage(file="assets/icones/icon_reservas.png")
        self.icon_ferramenta = PhotoImage(file="assets/icones/icon_ferramenta.png")
        self.icon_tecnico = PhotoImage(file="assets/icones/icon_tecnico.png")
        self.icon_sobre = PhotoImage(file="assets/icones/icon_about.png")
        self.icon_cadastrar = PhotoImage(file="assets/icones/icon_cadastrar.png")
        self.icon_pesquisar = PhotoImage(file="assets/icones/icon_pesquisar.png")
        self.icon_limpar = PhotoImage(file="assets/icones/icon_limpar.png")
        self.icon_atualizar = PhotoImage(file="assets/icones/icon_atualizar.png")

        ## Labels
        self.lb_expira = Label(self.principal, text="Reservas",font=tkFont.Font(size=15))
        self.lb_buscar = Label(self.principal, text="Buscar:", font=tkFont.Font(size=10))

        ## Caixas de texto
        self.cx_pesquisa = Entry(self.principal, width=50, font=32)

        ## Botões
        self.bt_pesquisa = Button(self.principal, text="Pesquisar", image=self.icon_pesquisar, compound='left', padx=5, height=22)
        self.bt_atualizar = Button(self.principal, text="Atualizar", image=self.icon_atualizar, compound='left', padx=5,height=22)
        self.bt_limpar = Button(self.principal, text="Limpar", image=self.icon_limpar, compound='left', padx=5, height=22, command=self.limpar_pesquisa)
        self.bt_tecnico = Button(self.principal, image=self.icon_tecnico, height=22, compound='left', padx=5, text="Técnicos", command=GraficoConsultaTecnico)
        self.bt_ferramenta = Button(self.principal, image=self.icon_ferramenta, height=22, compound='left', padx=5, text="Ferramentas", command=GraficoConsultaFerramenta)
        self.bt_reservar = Button(self.principal, image=self.icon_reserva, height=22, compound='left', padx=5, text="Reservas",command=GraficoReserva)
        self.bt_config = Button(self.principal, text="Config Email", image=self.icon_config, height=22, padx=5, compound='left', command=GraficoConfig)
        self.bt_sobre = Button(self.principal, text="Sobre", image=self.icon_sobre, height=22, padx=5, compound='left', command=self.sobre)
        self.bt_sair = Button(self.principal, text="Sair", image=self.icon_saida, compound='left', height=22, padx=5, command=self.principal.destroy)

        ## Inicio da Lista de Reservas
        self.nomes_colunas = ('col1', 'col2', 'col3', 'col4', 'col5', 'col6')
        self.lista_reservas = Treeview(self.principal, columns=self.nomes_colunas, show='headings', height=14)
        self.lista_reservas.column('col1', width=55, stretch=False)
        self.lista_reservas.column('col2', width=150, stretch=False)
        self.lista_reservas.column('col3', width=150, stretch=False)
        self.lista_reservas.column('col4', width=90, stretch=False)
        self.lista_reservas.column('col5', width=90, stretch=False)
        self.lista_reservas.column('col6', width=245, stretch=False)

        self.lista_reservas.heading('col1', text='Código')
        self.lista_reservas.heading('col2', text='Ferramenta')
        self.lista_reservas.heading('col3', text='Técnico')
        self.lista_reservas.heading('col4', text="Data/Retirada")
        self.lista_reservas.heading('col5', text="Data/Entrega")
        self.lista_reservas.heading('col6', text="Descrição")

        ## Fim da lista de reserva

        ## Alinhamento dos componentes
        self.lb_expira.place(x=10,y=10)
        self.lb_buscar.place(x=10, y=45)
        self.cx_pesquisa.place(x=65,y=45)
        self.bt_pesquisa.place(x=533, y=40)
        self.bt_atualizar.place(x=628, y=40)
        self.bt_limpar.place(x=718, y=40)
        self.lista_reservas.place(x=10, y=80)
        self.bt_tecnico.place(x=10,y=400)
        self.bt_ferramenta.place(x=100,y=400)
        self.bt_reservar.place(x=210,y=400)
        self.bt_config.place(x=300,y=400)
        self.bt_sobre.place(x=412, y=400)
        self.bt_sair.place(x=735,y=400)

        self.principal.mainloop() ## Abre a janela no momento que a classe é chamada ou estanciada!

    def limpar_pesquisa(self):
        self.cx_pesquisa.delete(0, 'end')

    def sobre(self):
        tk.messagebox.showinfo('Criadores', 'Desenvolvido por:\nDiego Gomes;\nJulio Marques;\nKauã Marques;\nValéria Souza.')

if __name__ == "__main__":
    GraficoMain()
