import numpy as np

lista = list(range(0,10)) #Lista de Python
print(lista)

array = np.arange(0,10) #Array, objeto de numpy
print(array)

zeroArray = np.zeros((10,10)) #Nos sirve para crear arrays en 0, asi podemos hacer esquemas de dimensiones
print(zeroArray)

oneArray = np.ones((10,10)) #Lo mismo pero con unos

linsArray = np.linspace(0,10,10) #No comprendí muy bien para que sirve este metodo
print(linsArray)

eyeArray = np.eye(4)
print(eyeArray)

randomArray =  np.random.rand(4) #Me da un array con datos aleatorios entre 0 y 1
print(randomArray) 

randomArray2 = np.random.randint(1,100, (10,10)) #Con esto podemos crear arrays, matrices o tensores según el rango que necesitemos pero de forma completamente aleatoria
print(randomArray2)