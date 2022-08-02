class Ferramenta:
    def __init__(self, cod_ferramenta, descricao, fabricante, voltagem, part_number,
                 tamanho, und_medida, tipo_ferramenta, material_ferramenta, tempo_max_reserva):

        self._cod_ferramenta = cod_ferramenta
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
    def cod_ferramenta(self):
        return self._cod_ferramenta

    @property
    def tempo_max_reserva(self):
        return self._tempo_max_reserva

    def __str__(self):
        return f'Cod: {self._cod_ferramenta} - {self._descricao} / {self._fabricante} - ' \
               f'{self._voltagem} - Tempo Máximo de Reserva: {self._tempo_max_reserva} horas'


## Somente será usado para testar a classe isoladamente,
# sem vinculo com o restante do sistema
if __name__ == "__main__":
    print(Ferramenta('001','Furadeira', 'Bosh', '220V', '0809221431', 35, 'cm', 'Eletrica', 'Plastico ABS', 48))