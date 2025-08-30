loop = 'S'

while loop == 'S':

    saltos = []
    maior_salto = 0
    soma_saltos = 0
    contador = 0

    print("\n")

    nome = input("\nDigite seu nome: ")


    while contador < 5:
        salto_atual = float(input("Digite qual a distância que saltou: "))
        saltos.append(salto_atual)

        contador = contador + 1
        soma_saltos = soma_saltos + salto_atual

        if salto_atual > maior_salto:
            maior_salto = salto_atual

    media = soma_saltos / 5

    print(f"\nAtleta: {nome}\n")

    print(f"Primeiro Salto: {saltos[0]}m")
    print(f"Segundo Salto: {saltos[1]}m")
    print(f"Terceiro Salto: {saltos[2]}m")
    print(f"Quarto Salto: {saltos[3]}m")
    print(f"Quinto Salto: {saltos[4]}m")

    print(f"\nResultado final:\n- Atleta: {nome}\n- Saltos: {saltos[0]}m, {saltos[1]}m, {saltos[2]}m, {saltos[3]}m, {saltos[4]}m\n- Maior salto: {maior_salto}\n- Média: {media}m\n")

    loop = input('Deseja realizar mais um calculo? (S - para "Sim", N - para "Não")')












    

