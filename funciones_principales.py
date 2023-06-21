import numpy as np

arr = np.random.randint(1,20,10)
print(arr)

matriz = arr.reshape(2,5)
print(matriz)


#Funcion max, para traer el número más grande del array

print(arr.max())
print(matriz.max(1)) #Podemos definir en que eje queremos sacar el maximo, puede ser tanto por el 0 (Columnas) o por el 1 (Filas)
print(arr.argmax()) #Argmax nos da el indice que contenga el valor más alto
print(matriz.argmax(1)) #Tambien podemos hacerlo por ejes


#Función min, para traer el número más pequeño del array
print(arr.min())
print(matriz.min(1)) #Podemos definir en que eje queremos sacar el maximo, puede ser tanto por el 0 (Columnas) o por el 1 (Filas)
print(arr.argmin()) #Argmax nos da el indice que contenga el valor más alto
print(matriz.argmin(1)) #Tambien podemos hacerlo por ejes


#Funcion ptp, muestra la distribución entre el número mayor y menor

print(arr.ptp())
print(matriz.ptp(1))


#Percentile, especifica en que percentile trabajamos

print(np.percentile(arr,(50)))


#Sort, para ordenar de menor a mayor nuestro arreglo

print(arr.sort())


#Mediana, para sacar la mediana

print(np.median(arr))


#std, poder sacar la desviación estandar

print(np.std(arr) ** 2)


#var, poder sacar la varianza

print(np.var(arr))


#media, poder sacar la media

print(np.mean(arr))


#Concatenar

a = np.array([[1,2],[3,4]])
b = np.array([5,6])

b = np.expand_dims(b,axis=0)

print(np.concatenate((a,b), axis=0))
print(np.concatenate((a,b.T), axis=1)) #La transpuesta de una matriz, cambia la forma del array para poder usar las dimensiones