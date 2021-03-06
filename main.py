from random import random
from assets import cars, bombs
from time import sleep

bombas = []
abastecimento = []
fila = []

bomba1 = bombs.Bomb(capacidade_combustivel=1000, quantidade_combustivel=1000, mangueiras=2)
bomba2 = bombs.Bomb(nome='Bomba 2', combustivel='Etanol', mangueiras=1)
bomba3 = bombs.Bomb(nome='Bomba 3', combustivel='GNV', mangueiras=4)
bomba4 = bombs.Bomb(nome='Bomba 4', combustivel='Diesel', mangueiras=2)
bombas.append(bomba1)
bombas.append(bomba2)
bombas.append(bomba3)
bombas.append(bomba4)

index_carro = 0
while True:
    if random() >= 0.5:
        index_carro += 1
        carro = cars.Car(index_carro)
        
        if carro.requisicao:
            carro.fila = True
            fila.append(carro)
        for carro_objeto in fila:
            for index, i in enumerate(bombas):
                if i.combustivel == carro_objeto.combustivel:
                    if i.quantidade_combustivel > carro_objeto.capacidade_tanque_combustivel - carro_objeto.capacidade_tanque_combustivel and i.mangueiras >= 1:
                        print(f'O veículo {carro_objeto.index_carro} {carro_objeto.tipo} {carro_objeto.marca} está sendo abastecido na {i.nome}\n')
                        tempo_encher = (carro_objeto.capacidade_tanque_combustivel - carro_objeto.tanque_combustivel) // 2
                        abastecimento.append([carro_objeto, index_carro, tempo_encher])
                        carro_objeto.index_bomba = index
                        i.encher(carro_objeto, carro_objeto.capacidade_tanque_combustivel - carro_objeto.tanque_combustivel)
                        fila.remove(carro_objeto)
                        break
                    elif index+1 == len(bombas):
                        print(f'O veículo {carro_objeto.index_carro} {carro_objeto.tipo} {carro_objeto.marca} não encontrou uma bomba disponível, ele está aguardando na fila.\n')
                        break
                elif index+1 == len(bombas):
                    print(f'O veículo {carro_objeto.index_carro} {carro_objeto.tipo} {carro_objeto.marca} não encontrou uma bomba com o tipo de combustível {carro_objeto.combustivel}, e foi embora.\n')
                    fila.remove(carro_objeto)
                    
    for index, veiculo in enumerate(abastecimento):
        if veiculo[1] + veiculo[2] <= index_carro:
            abastecimento.pop(index)
            print(f'O veículo {veiculo[0].index_carro} {veiculo[0].tipo} {veiculo[0].marca} foi abastecido e saiu do posto!\n')
            print(f'Uma mangueira da {bombas[veiculo[0].index_bomba].nome} foi livrada!\n')
            bombas[veiculo[0].index_bomba].mangueiras = +1

    
    if index_carro >= 10 and len(fila) == 0:
        print('O posto fechou e todos os veículos foram abastecidos')
        break
    elif index_carro > 100:
        print('O posto fechou por exesso de veículos')
        break
    sleep(1.5)

print('*'*20)
print('Debug')
print('*'*20)
print(f'Carros na fila: {len(fila)}')