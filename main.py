from datetime import datetime
from random import randint, random
from assets import cars, bombs
from time import sleep

carros = []
bombas = []
fila = []
abastecimento = []

bomba1 = bombs.Bomb(capacidade_combustivel=1000, quantidade_combustivel=1000, mangueiras=2)
bomba2 = bombs.Bomb(nome='Bomba 2', combustivel='Etanol')
bomba3 = bombs.Bomb(nome='Bomba 3', combustivel='GNV', mangueiras=4)
bomba4 = bombs.Bomb(nome='Bomba 4', combustivel='Diesel', mangueiras=2)
bombas.append(bomba1)
bombas.append(bomba2)
bombas.append(bomba3)
bombas.append(bomba4)


for c in range(0, 10):
    
    if random() >= 0.5:
        carro_objeto = cars.Car
        carro = cars.Car.gerar_carro(carro_objeto)
        carro_objeto.index_carro = c
        
        if type(carro) == list:
            carros.append(carro)
            for index, i in enumerate(bombas):
                if i.combustivel == carro_objeto.combustivel:
                    if i.quantidade_combustivel > carro_objeto.capacidade_tanque_combustivel - carro_objeto.capacidade_tanque_combustivel and i.mangueiras >= 1:
                        print(f'O veículo {carro_objeto.index_carro} {carro_objeto.tipo} {carro_objeto.marca} está sendo abastecido na {i.nome}')
                        tempo_encher = (carro_objeto.capacidade_tanque_combustivel - carro_objeto.tanque_combustivel) // 2
                        abastecimento.append([carro_objeto, c, tempo_encher])
                        carro_objeto.index_bomba = index
                        i.encher(carro_objeto, carro_objeto.capacidade_tanque_combustivel - carro_objeto.tanque_combustivel)
                        break
                    elif index+1 == len(bombas):
                        print(f'O veículo {carro_objeto.index_carro} {carro_objeto.tipo} {carro_objeto.marca} não encontrou uma bomba disponível, ele está aguardando na fila.')
                        fila.append(carro_objeto)
                        break
                elif index+1 == len(bombas):
                    print(f'O veículo {carro_objeto.index_carro} {carro_objeto.tipo} {carro_objeto.marca} não encontrou uma bomba com o tipo de combustível {carro_objeto.combustivel}, e foi embora')
                    carros.pop()
                    
    for index, veiculo in enumerate(abastecimento):
        if veiculo[1] + veiculo[2] <= c:
            print(veiculo[1], veiculo[2],veiculo[1] + veiculo[2], c)
            abastecimento.pop(index)
            print(f'O veículo {veiculo[0].index_carro} {veiculo[0].tipo} {veiculo[0].marca} foi abastecido e saiu do posto')
            bombas[veiculo[0].index_bomba].mangueiras = +1


    sleep(1.5)

print(f'\nDebug\nCarros\t{carros}\nFila\t{fila}\nAbastecimento\t{abastecimento}')

