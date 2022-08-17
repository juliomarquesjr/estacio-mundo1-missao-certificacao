class Validadores:
    def __init__(self,validadores2):
        self.validadores_entry()
    def validadores_entry(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100

    #Técnicos
#Nome - Texto Livre, não aceite números (40 caracteres);
#CPF - Já vem configurado do cadastro com pontos e traço (14 caracteres);
#Telefone - Já vem do cadastro configurado como telefone celular, com parenteses e traço (14 caracteres);
#Equipe - Texto Livre (30 caracteres);
#Turno - Manhã, Tarde ou Noite(5 caracteres).

    #Ferramentas
#Código - (x caracteres);
#Fabricante - Texto Livre (30 caracteres);
#Part Number - Apenas aceitar números (25 caracteres);
#Material - Palavra Livre (15 caracteres);
#Voltagem - Texto Livre (15 caracteres);
#Tamanho - Informação em Número (20 caracteres);
#Unidade - Palavra Livre (15 caracteres);
#Tipo - Palavra Livre (15 caracteres);
#Tempo Limite - Já vem do cadastro configurado como tempo, com horas, minutos e segundos, juntamente com dois pontos (8 caracteres);
#Descrição - Texto Livre (60 caracteres).

    #Reservas
#Nome do Técnico - Texto Livre, não aceite números (40 caracteres)
#Código da Ferramenta - (x caracteres);
#Data e hora da Retirada - Data vem configurada (x caracteres) e a hora como tempo, com horas, minutos e segundos, juntamente com dois pontos (8 caracteres);
#Data e hora da Devolução - Data vem configurada (x caracteres) e a hora como tempo, com horas, minutos e segundos, juntamente com dois pontos (8 caracteres);
#Descrição - Texto Livre (60 caracteres).
