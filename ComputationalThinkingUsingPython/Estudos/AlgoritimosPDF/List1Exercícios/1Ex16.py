"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode
começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. Veja
abaixo alguns exemplos. Não fixe esses valores no código. Você pode usá-los para TESTAR seu algoritmo:

Hora inicial    Hora final            Resultado
    16              2           O JOGO DUROU 10 HORA(S)
    0               0           O JOGO DUROU 24 HORA(S)
    2               16          O JOGO DUROU 14 HORA(S)

"""

# Leitura das horas
hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))

# Cálculo da duração
if hora_inicial == hora_final:
    duracao = 24
elif hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final

# Exibição do resultado
print(f"O JOGO DUROU {duracao} HORA(S)")