import tkinter
from tkinter import Label, PhotoImage, Button, messagebox
import tkinter as tk
import tkinter.font as tkFont

from graficoconfig import GraficoConfig
from graficoconsferramenta import GraficoConsultaFerramenta
from graficoconstecnico import GraficoConsultaTecnico
from graficoconsreserva import GraficoConsultaReserva

from sistema.centraliza_janelas import center

class GraficoMain:
    def __init__(self):
        self.principal = tkinter.Tk()

        ## Ajustar tamanho da janela e não permitir maximizar
        self.principal.geometry("397x180")
        self.principal.resizable(width=False, height=False)

        self.principal.title('Missão Certificação - Mundo 1')
        center(self.principal)

        ## Icones
        self.icon_reserva = PhotoImage(file="assets/icones/icon_reservas.png")
        self.icon_ferramenta = PhotoImage(file="assets/icones/icon_ferramenta.png")
        self.icon_tecnico = PhotoImage(file="assets/icones/icon_tecnico.png")
        self.icon_config = PhotoImage(file="assets/icones/icon_config.png")
        self.icon_sobre = PhotoImage(file="assets/icones/icon_about.png")
        self.icon_saida = PhotoImage(file="assets/icones/icon_saida.png")

        ## Labels
        self.lb_cabecalho = Label(self.principal, text="Conteúdo Audiovisual LTDA",font=tkFont.Font(size=12))

        ## Botões
        self.bt_tecnico = Button(self.principal, image=self.icon_tecnico, height=22, width=100, compound='left', padx=5, text="Técnicos", command=GraficoConsultaTecnico)
        self.bt_ferramenta = Button(self.principal, image=self.icon_ferramenta, height=22, width=100, compound='left', padx=5, text="Ferramentas", command=GraficoConsultaFerramenta)
        self.bt_reservar = Button(self.principal, image=self.icon_reserva, height=22, width=100, compound='left', padx=5, text="Reservas",command=GraficoConsultaReserva)
        self.bt_config = Button(self.principal, text="Config Email", image=self.icon_config, height=22, width=100, padx=5, compound='left', command=GraficoConfig)
        self.bt_sobre = Button(self.principal, text="Sobre", image=self.icon_sobre, height=22, width=100, padx=5, compound='left', command=self.sobre)
        self.bt_sair = Button(self.principal, text="Sair", image=self.icon_saida, compound='left', height=22, width=100, padx=5, command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_cabecalho.place(x=90,y=10)
        self.bt_tecnico.place(x=10,y=50)
        self.bt_ferramenta.place(x=140,y=50)
        self.bt_reservar.place(x=270,y=50)
        self.bt_config.place(x=75,y=90)
        self.bt_sobre.place(x=205, y=90)
        self.bt_sair.place(x=140,y=130)

        self.principal.mainloop() ## Abre a janela no momento que a classe é chamada ou estanciada!

    def sobre(self):
        tk.messagebox.showinfo('Criadores', 'Desenvolvido por:\nDiego Gomes;\nJulio Marques;\nKauã Marques;\nValéria Souza.')

if __name__ == "__main__":
    GraficoMain()
