# Definindo os números decimais
a = 3.5
b = 1.2
c = 4.7

# Ordenando com if
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b


# Exibindo os números ordenados
print(a, b, c)