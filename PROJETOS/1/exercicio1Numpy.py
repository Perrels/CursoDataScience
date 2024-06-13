import numpy as np

lista = []
for i in range(1, 4):
    while True:
        try:
            # passando valores com parse para float senão da problema
            x = float(input(f"insira o {i} número \n"))
            lista.append(x)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido")


# transformando a lista num npArray
numPyArray = np.array(lista)
print(f'Lista do array do numPy{numPyArray}')
print("----------------------------------------\n")
# crie maximo, minimo, menor posicao, desvio padrao e media
print("Máx", numPyArray.max())
print("Min", numPyArray.min())
print("Menor posicao", numPyArray.argmax())
print("Desvio padrão", numPyArray.std())
print("Média", numPyArray.mean())
