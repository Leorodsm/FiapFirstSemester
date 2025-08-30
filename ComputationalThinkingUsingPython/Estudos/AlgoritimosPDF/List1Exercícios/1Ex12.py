"""
Fazer um algoritmo que leia dois números L e R. O programa deve verificar a maior área entre um quadrado
de lado L e um círculo de raio R. Imprimir na tela qual o maior: "Quadrado" ou "Círculo"

"""

print('\nAlgotrítmo: L e R\n')

# Entrada
lado = float(input('Digite o valor do lado: '))
raio = float(input('Digite o valor do raio: '))

# Processamento
quadrado = lado * lado
circulo = 3.14 * raio ** 2

# Saída
if quadrado > raio:
    print(f'\nA área maior é a do quadrado: {quadrado}\n')
else:
    print(f'\nA área maior é a do circulo: {circulo}\n')