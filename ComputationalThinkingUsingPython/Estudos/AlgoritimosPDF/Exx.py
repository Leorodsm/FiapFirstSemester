repeticao = 'sim'

while repeticao == 'sim':

    carros = []
    consumo = []

    contador = 0
    soma_combustiveis = 0

    # Preenchendo as listas usando while
    while contador < 5:
        nome_carro = input(f"\nDigite o nome do {contador + 1}º carro: ")
        carros.append(nome_carro)

        consumo_carro = float(input(f"Digite o consumo do {contador + 1}º carro (Km/l): "))
        consumo.append(consumo_carro)

        soma_combustiveis += consumo_carro

        contador += 1

    media_combustiveis = soma_combustiveis / 5

    consumo_definido = []
    gasto_definido = []

    menor_gasto = 0
    veiculo_economico = ''

    contador = 0

    # Calculando consumo para 1000km e gasto (R$ 6.89 por litro)
    while contador < 5:
        litros = 1000 / consumo[contador]
        gasto = litros * 6.89

        consumo_definido.append(litros)
        gasto_definido.append(gasto)

        if (menor_gasto is None) or (gasto < menor_gasto):
            menor_gasto = gasto
            veiculo_economico = carros[contador]

        contador += 1

    # Impressão dos dados dos veículos
    print('\n\nComparativo de Consumo de Combustível\n\n')

    contador = 0
    while contador < 5:
        print(f'- Veículo {contador + 1}:')
        print(f'Nome: {carros[contador]}, {consumo[contador]} Km/l\n')
        contador += 1

    print('Relatório Final, comparando uma distância:\n')

    contador = 0
    while contador < 5:
        print(f'{contador + 1} - {carros[contador]}')
        print(f'- Consumo: {consumo[contador]:.2f} Km/l')
        print(f'- Para 1000 km faz {consumo_definido[contador]:.2f} litros')
        print(f'- Gasto: R${gasto_definido[contador]:.2f}\n')
        contador += 1

    print(f'\nO menor gasto é com o veículo: {veiculo_economico}.\n')

    repeticao = input('Deseja continuar? Digite (Sim) ou (Não): ').lower()
