import numpy as np
#Scalar: Un unico dato
#Vector: Un array de una unica dimension
#Matriz: Filas y columnas, dos dimensiones. Puede ser una hoja de calculo excel
#Tensor 3D: Tres dimensiones, tienen caracteristicas, series de tiempo y sus ejemplos.
#Tensor 4D: Cuatro dimensiones, tiene alto, ancho, ejemplos y canales.


scalar = np.array(42)
print(scalar)
print(scalar.ndim) #numero de dimensiones

vector = np.array([1,2,3,4,5])
print(vector)
print(vector.ndim) #numero de dimensiones

matriz = np.array([[1,2,3], [5,6,7], [8,9,10],[14,27,36], [54,67,70], [84,98,10]])
print(matriz)
print(matriz.ndim) #numero de dimensiones

tensor = np.array([[[1,2,3], [5,6,7], [8,9,10],[14,27,36], [54,67,70], [84,98,10]],[[1,2,3], [5,6,7], [8,9,10],[14,27,36], [54,67,70], [84,98,10]]])
print(tensor)
print(tensor.ndim) #numero de dimensiones
