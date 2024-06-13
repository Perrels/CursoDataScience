import numpy as np

notas = []
for i in range(3):
    while True:
        try:
            valor = float(input(f'Insira a nota do aluno {i}\n'))
            notas.append(valor)
            break
        except KeyError:
            print('Inserção de dados incorreta. Tente somente com números do tipo float/inteiros')

print(f"Lista de notas -> {notas}")

arrayNotas = np.array(notas)
reprovados  = arrayNotas <= 6
print(reprovados)
print(f"Lista das notas reprovadas{arrayNotas[reprovados]}")        