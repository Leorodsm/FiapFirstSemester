"""
Escreva um programa para ler a quantidade de alunos existentes em uma turma. Depois disso, o programa
deve ler as notas de cada um destes alunos, calcular e mostrar na tela a média aritmética destas notas.
Utilize o laço WHILE.

"""

qtd = int(input("Digite a quantidade de alunos: "))
contador = 1
total = 0

while contador <= qtd:
    nota = int(input("Digite a nota do aluno: "))
    total += nota

    contador += 1

media = total / qtd

print(f"A média total é: {media}")



