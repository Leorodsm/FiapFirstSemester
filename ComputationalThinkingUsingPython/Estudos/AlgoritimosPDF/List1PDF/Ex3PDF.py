""" ___________________________________________________________________________________________________________________________________
3 - Um algoritmo capaz de calcular o exponencial de um número por outro  

(Entrada)
- Exponencial, é exponenciação. Um número elevado a tantas vezes, 2 elevado a 3: 2x2x2 = 8.
  No computador, usamos o chápeu para representar essa operação: 2^3 = 8
  Mas para fazer mesmo a exponenciação, se usa três asteristicos: 2**3 = 8

- Assim, pegamos a base (o número que vai ser elevado), pegamos o expoente (o número que vai elevar) e colocamos um em cada variável.

(Processamento)
- E criamos o algorítimo da exponenciação, base elevado pelo expoente: base ** expoente

(Saída)
- E exibimos o resultado.2

"""

print('\nAlgorítimo: Exponenciação\n')

b = float(input('Digite uma base: '))
e = int(input('Digite um expoente: '))

ex = b ** e

print(f'\n- {b} ^ {e} é: {ex:.2f}\n')






















"""
# Entrada
print('\nAlgorítimo: Exponenciação\n')

base = int(input('Digite a número da base: '))
expoente = int(input('Digite o número do expoente: '))

# Processamento
potencia = base**expoente

# Saída
print(f'\nO resultado de {base} ^ {expoente} = {potencia}\n')
"""