class Bomb:
    def __init__(self, nome='Bomba 1', combustivel='Gasolina', capacidade_combustivel=500, quantidade_combustivel=500, mangueiras=1):
        if capacidade_combustivel >= quantidade_combustivel:
            self.combustivel = combustivel
            self.capacidade_combustivel = capacidade_combustivel
            self.quantidade_combustivel = quantidade_combustivel
            self.mangueiras = mangueiras
            self.nome = nome
        else:
            print('Erro na configuração da bomba.\nQuantidade de combustível superior à capacidade máxima')

    def encher(self, carro, quantidade):
        self.mangueiras -= 1
        carro.tanque_combustivel += quantidade
        self.quantidade_combustivel -= quantidade