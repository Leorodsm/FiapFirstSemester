letra = ""
contador = 0

# Diferente

while letra != "x":
    letra = str(input("Digite mais uma letra:"))

    contador = contador + 1

print(f'Foram digitadas {contador} letras')