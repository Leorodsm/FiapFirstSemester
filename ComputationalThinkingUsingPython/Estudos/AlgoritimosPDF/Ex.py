# repetição = 'sim'

# while repetição == 'sim':

#     saltos = []
#     maior_salto = 0
#     soma_saltos = 0
#     contador = 0

#     nome = input("\nDigite seu nome: \n")

#     while contador < 5:
#         salto_atual = float(input("Digite qual a distância que saltou: "))
#         saltos.append(salto_atual)

#         contador = contador + 1
#         soma_saltos = soma_saltos + salto_atual

#         if salto_atual > maior_salto:
#             maior_salto = salto_atual

#     media = soma_saltos / 5

#     print(f"\nAtleta: {nome}\n")

#     print(f"Primeiro Salto: {saltos[0]}m")
#     print(f"Segundo Salto: {saltos[1]}m")
#     print(f"Terceiro Salto: {saltos[2]}m")
#     print(f"Quarto Salto: {saltos[3]}m")
#     print(f"Quinto Salto: {saltos[4]}m")

#     print(f"\nResultado final:\n- Atleta: {nome}\n- Saltos: {saltos[0]}m, {saltos[1]}m, {saltos[2]}m, {saltos[3]}m, {saltos[4]}m\n- Maior salto: {maior_salto}\n- Média: {media}m\n")
    
#     repetição = str(input('Deseja continuar? Digite (Sim) ou (Não): ')).lower()

# ////////////// Criando as Funções //////////////

def coletar_saltos():

    saltos = []
    maior_salto = 0
    soma_saltos = 0
    contador = 0

    while contador < 5:
        salto_atual = float(input(f"Digite a distância do {contador + 1}º salto (em metros): "))
        saltos.append(salto_atual)

        contador = contador + 1
        soma_saltos = soma_saltos + salto_atual

        if salto_atual > maior_salto:
            maior_salto = salto_atual

    media = soma_saltos / 5

    return saltos, maior_salto, media


def exibir_resultado(nome, saltos, maior_salto, media):

    print(f"\nAtleta: {nome}\n")

    print(f"Primeiro Salto: {saltos[0]}m")
    print(f"Segundo Salto: {saltos[1]}m")
    print(f"Terceiro Salto: {saltos[2]}m")
    print(f"Quarto Salto: {saltos[3]}m")
    print(f"Quinto Salto: {saltos[4]}m")

    print("\nResultado final:")
    print(f"- Atleta: {nome}")
    print(f"- Saltos: {saltos[0]}m, {saltos[1]}m, {saltos[2]}m, {saltos[3]}m, {saltos[4]}m")
    print(f"- Maior salto: {maior_salto}m")
    print(f"- Média dos saltos: {media}m\n")

# ////////////// Programa Principal //////////////

repeticao = 'sim'

while repeticao.lower() == 'sim':
    nome = input("\nDigite seu nome: ")

    # Chamada da função e separação dos dados (forma destrinchada)
    dados_dos_saltos = coletar_saltos()

    saltos = dados_dos_saltos[0]
    maior_salto = dados_dos_saltos[1]
    media = dados_dos_saltos[2]

    # Exibir resultado
    exibir_resultado(nome, saltos, maior_salto, media)

    # Verificar se quer continuar
    repeticao = input('Deseja continuar? (Sim ou Não): ').lower()
