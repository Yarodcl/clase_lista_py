import numpy as np

arr = np.array[1,2,3,4], dtype='float64' #Al escribir esto, el array cambia a tipo decimal.
arr.dtype #Esto nos ayuda a ver de que tipo es un array 


arr1 = np.array[1,2,3,4]
arr1 = arr1.astype(np.float64) #Tambien podemos cambiar el tipo de dato directamente desde numpy, podemos hacerlo tanto con float, enteros, booleanos, string
#int8 para enteros
#string_ para strings
#bool_ para booleanos