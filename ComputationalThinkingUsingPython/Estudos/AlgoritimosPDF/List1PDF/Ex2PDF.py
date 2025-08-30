""" ___________________________________________________________________________________________________________________________________
2 - Um algoritmo para calcular a média aritmetica de 3 notas e apresentar o resultado  

(Entrada)
- A média aritimética é feita assim: A soma das notas dividido pelo número de avaliações, nesse caso, a soma de 3 notas dívidido por 3 avaliações.
- E fazemos o mesmo processo, pegamos os três números e colocamos um em cada variável.

(Processamento)
- Depois, criamos a operação da média aritimética. Como precisamos dividir os três números de uma vez depois de soma-los, 
colocamos a soma entre parênteses "()" e depois dividimos tudo dentro dos parênteses pelo número de avaliações.
Dessa maneira: (numero1 + numero2 + numero3) / 3

(Saída)
- E por fim, mostramos o resultado.

"""

print('\nAlgorítimo: Média de aritimética entre 3 notas: \n')

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

media = (n1 + n2 + n3) / 3

print(f'\n- A média é: {media:.2f}\n')

























"""
# Entrada
print('\nAlgorítimo: Média arítimetica semestral:\n')

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

# Processamento
media = (n1+n2+n3)/3

# Saída
print(f'\nA média das três provas é: {media:.1f}\n')
"""