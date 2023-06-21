import numpy as np

arr = np.arange(0,10)
arr2 = arr.copy()

#Operaciones

print(arr * 2)
print(1 / arr)
print(arr ** 2)
print(arr + arr2)

matriz = arr.reshape(2,5)
matriz2 = matriz.copy()
print(matriz + matriz2)

np.mamtul(matriz,matriz2.T)

matriz @ matriz2.T