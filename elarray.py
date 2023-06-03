import numpy as np

print("Lista")
lista = [1,2,3,4]
print(lista)

print("Array")
arr = np.array(lista) #numpy puede pasar objetos de lista a array que nos sirve para utilizar operaciones
print(arr) 

print("Matriz")
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)
print(matriz)

print("Indexación matriz")

matriz[0]
print(f"Nivel uno {matriz[0]}")

matriz[0,2]
print(f"Posiciones exactas, nivel uno, tercera posición: {matriz[0,2]}")

print("Slicing Array, para copiar o partir el array")
print(arr[1:4])
print(arr[:2])
print(arr[3:])
print(arr[:])
print(arr[::2])
print(arr[-1:])

print("Slicing Matriz, para copiar o partir de la matriz")
print(matriz[1:])
print(matriz[1:,0:2])