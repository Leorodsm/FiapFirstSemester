carros = ['Jeep Compass','Pegout 208','Hyundai Creta', 'Fiat Uno', 'Honda Civic']
consumo = [16, 5, 12, 10, 14]

contador = 0
soma_combustiveis = 0

for posicao in consumo:
    soma_combustiveis = soma_combustiveis + posicao

media_combustiveis = soma_combustiveis / 5

consumo_definido = []
gasto_definido = []

menor_gasto = 0
veiculo_economico = ''


for litros in consumo:
    quilometragem = (1000 / litros)
    gasto = quilometragem * 6.89 

    consumo_definido.append(quilometragem)
    gasto_definido.append(gasto)

    for valor in consumo:
        if gasto > menor_gasto:
            menor_gasto = gasto
            break

    for veiculo in carros:
        if gasto < menor_gasto:
            veiculo_economico = veiculo
            break
            

print('\n\nComparativo de Consumo de Combustível\n\n')
print(f'- Veículo 1:\nNome: {carros[0]}, {consumo[0]} Km/l\n')
print(f'- Veículo 2:\nNome: {carros[1]}, {consumo[1]} Km/l\n')
print(f'- Veículo 3:\nNome: {carros[2]}, {consumo[2]} Km/l\n')
print(f'- Veículo 4:\nNome: {carros[3]}, {consumo[3]} Km/l\n')
print(f'- Veículo 4:\nNome: {carros[4]}, {consumo[4]} Km/l\n')

print('Relatório Final, comparando uma distância: \n')
print(f'1 - {carros[0]}     \n- {consumo[0]:.2f}Km/l  - 1000km Faz {consumo_definido[0]:.2f} L , gastando R${gasto_definido[0]:.2f}\n')
print(f'2 - {carros[1]}     \n- {consumo[1]:.2f}Km/l  - 1000km Faz {consumo_definido[1]:.2f} L , gastando R${gasto_definido[1]:.2f}\n')
print(f'3 - {carros[2]}     \n- {consumo[2]:.2f}Km/l  - 1000km Faz {consumo_definido[2]:.2f} L , gastando R${gasto_definido[2]:.2f}\n')
print(f'4 - {carros[3]}     \n- {consumo[3]:.2f}Km/l  - 1000km Faz {consumo_definido[3]:.2f} L , gastando R${gasto_definido[3]:.2f}\n')
print(f'5 - {carros[4]}     \n- {consumo[4]:.2f}Km/l  - 1000km Faz {consumo_definido[4]:.2f} L , gastando R${gasto_definido[4]:.2f}\n')

print(f'\nO menor gasto é {veiculo}.\n')