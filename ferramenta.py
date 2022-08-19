from sistema.banco import Banco

class Ferramenta:
    def __init__(self, descricao=False, fabricante=False, voltagem=False, part_number=False,
                 tamanho=False, und_medida=False, tipo_ferramenta=False, material_ferramenta=False, tempo_max_reserva=False):


        self._descricao = descricao
        self._fabricante = fabricante
        self._voltagem = voltagem
        self._part_number = part_number
        self._tamanho = tamanho
        self._und_medida = und_medida
        self._tipo_ferramenta = tipo_ferramenta
        self._material_ferramenta = material_ferramenta
        self._tempo_max_reserva = tempo_max_reserva

    @property
    def tempo_max_reserva(self):
        return self._tempo_max_reserva

    def cadastra_banco(self):
        self.resp = Banco().adicionar_dados(tabela='ferramenta', dados=(self._descricao,
                                                                        self._fabricante,
                                                                        self._voltagem,
                                                                        self._part_number,
                                                                        self._tamanho,
                                                                        self._und_medida,
                                                                        self._tipo_ferramenta,
                                                                        self._material_ferramenta,
                                                                        self._tempo_max_reserva))

        return self.resp

    def remover_banco(self, cod_ferramenta):
        self.resp = Banco().remover_dados(tabela='ferramenta',
                                          where=f"id = '{cod_ferramenta}'")

        return self.resp

    def __str__(self):
        return f'Cod: {self._cod_ferramenta} - {self._descricao} / {self._fabricante} - ' \
               f'{self._voltagem} - Tempo Máximo de Reserva: {self._tempo_max_reserva} horas'
