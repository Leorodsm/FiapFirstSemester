""" ___________________________________________________________________________________________________________________________________
13 - Escreva um algoritmo que leia a cotação do dólar e a quantidade de dólares a ser comprada. Converta o valor para real e mostre o resultado

(Entrada)
- 

(Processamento)
- 

6dol

200dol

1200reais


(Saída)
- 


"""

print('\nAlgorítimo: Conversão Dóllars para Reais\n')

vld= float(input('Digite a cotação do dóllar: '))
d = float(input('E quantos dóllars você deseja comprar? : '))

r = vld * d

print(f'\n- É preciso R${r:.2f} para comprar ${d:.2f} \n')





























"""
# Entrada
print('\nAlgorítimo: Valor em dólares\n')

cotacao = float(input('Digite a cotação do dólar: '))
qt = float(input('Digite quantos dólares você quer comprar: '))

# Processamento
realdolar = qt*cotacao

# Saída
print(f'\n${qt:.2f} são R${realdolar:.2f} na cotação atual de {cotacao}%\n')
"""
