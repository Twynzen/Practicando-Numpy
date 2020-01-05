import numpy as np

#matriz de unos
unos = np.ones((3,4))

#matriz de ceros

ceros = np.zeros((3,4))

#matriz aleaoria
aleatiorios =  np.random.random((4,4))

#matriz con  todos los valores que se decida
#Numero de la matriz
n=5
full = np.full((2,2),n)

#Para crear una matriz con valores espaciados uniformemente
espacio1 = np.arange(0,30,5)
espacio2 = np.linspace(0,2,5)

#matriz de identidad en que las diagonales son 1 y los demás ceros
identidad1 = np.eye(4,4)
identidad2 = np.identity(4)

#conocer el tipo de datos
a = np.array([(1,2,3)])
#se utiliza print(a.dtype)

#Para conocer el tamaño y  forma de la matriz
b= np.array([(1,2,3,4,5,6)])
#se tuliza print(a.size) y print(a.shape)

#cambiando el numero de filas y columndas de las matrices
c1 = np.array([(8,9,10),(11,12,13)])
#con volteamos la matriz
c2 = c1.reshape(3,2)

#seleccionar un solo lemento de matriz
d= np.array([(1,2,3,4),(3,4,5,6)])
#seleccionamos el valor que queremos print(d[0:,2])

#podemos encontrar el valor minimo maximo
e = np.array=([2,4,8])
#valor.min, vamor.max, valor.sum No sirven por razones que no comprendo

#Resultado
print(e.max())
