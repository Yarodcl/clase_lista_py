import numpy as np

arr = np.linspace(1,10,10, dtype='int8')

cont_index = arr > 5 #Retorna una lista booleana con el array, especificando que valores cumplen o no la condicion

print(arr[cont_index]) #Solamete devuelve valores que cumplan la condicion
print(arr[(arr > 5) & (arr <9)]) 
values_changes = arr[arr > 5] = 100

