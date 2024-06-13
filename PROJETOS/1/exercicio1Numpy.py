import numpy as np

lista = []
for i in range(1, 4):
    while True:
        try:
            x = input(f"insira o {i} número \n")
            lista.append(x)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido")
            
            
# transformando a lista num npArray
numPyArray = np.array(lista)

#
