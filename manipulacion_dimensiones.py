import numpy as np
vector = np.array([1,2,3,4,5], ndmin=10) #Este ultimo parametro transforma las dimensiones de nuestro array según lo solicitado
print(vector)
print(vector.ndim) #numero de dimensiones

expand = np.expand_dims(np.array([1,2,3]), axis=0) #Podemos expandir dimensiones, el axis se refiere a que nivel queremos aumentar la dimension el "0" se refiere a filas el "1" es columnas
print(expand)
print(expand.ndim)

print(vector, vector.ndim)
vector_2 = np.squeeze(vector) #Squeeze elimina las dimensiones que no se esten utilizando, dejando solamente una en este caso
print(vector_2, vector_2.ndim)