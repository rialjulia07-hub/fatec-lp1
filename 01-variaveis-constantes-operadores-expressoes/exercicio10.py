# Exercício 10
# Peça ao usuário três notas utilizando input() e float(). Calcule a
# média aritmética entre elas e exiba o resultado com print(). Em
# seguida, utilizando um operador relacional, exiba também se a média é
# maior ou igual a 6 (o resultado será um valor booleano, True ou False).

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

media = nota1 + nota2 + nota3 / 3
print(media)
print(media >= 6)