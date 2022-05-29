from random import randint, choice

class Car:
    marca = ''
    modelo = ''
    tanque_combustivel = 0
    capacidade_tanque_combustivel = 0
    tipo = 'Sedã'
    combustivel = 'Gasolina'
    index_bomba = 0
    index_carro = 0
    fila = bool()
    requisicao = bool()
    
    def __init__(self, index):
        tipos = ['Sedã', 'SUV', 'Caminhão']
        marcas = [['Honda', 'Volkswagen', 'Fiat'], ['Jeep', 'Volkswagen', 'Chevrolet'], ['Man', 'Mercedes-benz']]
        tipos_combustivel = ['Gasolina', 'Diesel', 'Etanol', 'GNV']
        index_tipo_carro = randint(0, len(tipos) - 1)
        self.tipo = tipos[index_tipo_carro]
        self.marca = marcas[index_tipo_carro][randint(0, len(marcas[index_tipo_carro]) - 1)]
        if self.tipo == 'Caminhão':
            self.capacidade_tanque_combustivel = randint(100, 900)
            self.combustivel = tipos_combustivel[choice([1])]
        elif self.tipo == 'SUV':
            self.capacidade_tanque_combustivel = randint(80, 250)
            self.combustivel = tipos_combustivel[choice([0, 1, 2])]
        elif self.tipo == 'Sedã':
            self.capacidade_tanque_combustivel = randint(50, 80)
            self.combustivel = tipos_combustivel[choice([0, 2, 3])]

        self.index_carro = index
        self.tanque_combustivel = randint(int(self.capacidade_tanque_combustivel * 0.01), self.capacidade_tanque_combustivel)
        if self.tanque_combustivel > self.capacidade_tanque_combustivel * (randint(40, 100)/100):
            print(f'Um veículo {self.index_carro} {self.tipo} {self.marca} não quis abastecer e passou direto pelo seu posto.\n')
            self.requisicao = False
        else:
            print(f'O veículo {self.index_carro} {self.tipo} {self.marca} está indo ao seu posto.\n')
            self.requisicao = True
