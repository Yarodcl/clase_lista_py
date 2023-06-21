import numpy as np

arr = np.random.randint(1,10, size=(3,2)) #Array aleatorio en un rango de 1 a 10 con un tamaño de 3 x 2

print(arr)
print(arr.shape) #Dice la forma original del array
print(arr.reshape(1,6)) #Cambia la forma del array

np.reshape(arr,(2,3), "C") #Ordenamiento según C
np.reshape(arr,(2,3), "F") #Ordenamiento según Fortran
np.reshape(arr,(2,3), "A") #Ordenamiento según mi sistema, puece ser cualquiera de los dos
#reshape tiene que respetar la forma original, siempre respetando la cantidad de valores original
print(arr.reshape(1,9)) #Error