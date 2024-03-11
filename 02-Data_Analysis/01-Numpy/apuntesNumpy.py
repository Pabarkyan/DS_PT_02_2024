# Apuntes Numpy, clase 04/3/2024

import numpy as np # np es el convenio para abreviar numpy

'''help(np) # para la ayuda
help(np.random) # Para una ayuda mas especifica
np.info(np.concatenate) # Para obtener la documentacion de concatenate
'''
array = np.array([1,2,3,4,5,6,7,8,9])
print(array* 10) # a diferencia de antes ahora podemos operar a la vez todos los numeros de un array

print(array.dtype) # nos da cuanto espacio ocupa y el dato en cada uno de los elementos de la matriz, RECORDATORIO: los elementos deben ser homogenos

array_multi = np.array([[1,2,3], [4,5,6], [7,8,9]])

array = np.arange(start=0, stop=10, step=2) 
array = np.arange(10) # array del 0 al 10
array = np.arange(0, 10, 0.5) # saltos de 0.5
array = np.arange(0, 10, 2, np.float64) # del 0 al 10 con saltos de 2 en float64


array = np.random.rand(10)
array = np.random.randint(5, size=(3,4)) # numeros aleatorios entre el 0 y el 5 creando una matriz 3x4
array = np.random.randint(5, 10, size=(10)) # aleatorios del 5 al 10 , matriz 1x10

array_10 = np.random.rand(10)
array = np.round(array_10, 4) # redondea todo el array en 4 decimales

#np.random.seed(12) # establece una semilla, el numero de dentro es indiferente

matriz_identidad = np.identity(3) # dimension 3
matriz_de_zeros = np.zeros((3,3)) # 3x3
matriz_de_unos = np.ones((3,3), np.int32) # 3x3 ocupando un int32
array = np.full((3,3), np.random.randint(12)) # llena una matriz 3x3 espacios por enteros aleatorios del 0 al 12


array_multi = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(array_multi.ndim) # numero de dimensiones, ejemplo: 3
print(array_multi.shape) # tamaño en cada una de las dimensiones, ejemplo: 5x2
print(array_multi.size) # cantidad total de elementos de un array, ejemplo: si es una matriz 3x3 pues devolvera 9

array = np.array([1,2,3,4,5])
print(array.itemsize) # tamaño de bytes de los items del array
print(array.nbytes) # tamaño en bytes de todo el array


array = np.array([[[1,10], [2, 20], [3, 30]],
                    [[4, 40], [5, 50], [6, 60]],
                    [[7, 70], [8, 80], [9, 90]]])

print(array[0][0] == array[0,0]) # compara 1 con 1
print(array[0, -1, -1]) #30


l = np.arange(10)
print("Del primer elemento al quinto", l[0:5])
print("Del primero al quinto con saltos de dos", l[0:5:2])
print("Desde el quinto", l[5::])
print("Desde el quinto", l[5:]) # equivalente
print("Desde el quinto hasta el penultimo", l[5:-1])
print("Desde el quinto, al primero", l[5::-1])
print("Sacar una copia", l[:])
print("Ultimos dos elementos",l[-2:])

array_multi = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
print("2 primeras filas y 3 primeras columnas\n", array_multi[:2, :3])
print("Todas las filas, cada dos columnas\n", array_multi[::, ::2])
print("Invertir las filas\n", array_multi[::-1])
print("Invertir columnas\n", array_multi[::,::-1])
print("Invertir filas y columnas\n", array_multi[::-1,::-1])


x = np.arange(9)
y =x.reshape((3,3)) # convertimos a otra dimension, siempre que sea posible
f = np.arange(30).reshape(2,3,5)


x_bools = np.array(x == 2)
print(x_bools, x)
print(x[x_bools]) # es una buena forma de imponer condiciones
print(x_bools[x_bools]) # esta haciendo comparaciones 1 por 1


x = np.array([1,2,3])
y = np.array([3,2,1])
np.concatenate((x,y)) # concatena

xy = np.array([[1,2,3],
              [4,5,6]])
np.vstack([xy,x]) # añadimos x a xy en la ultima fila


xy = np.array([[1,2,3],
              [4,5,6]])

x = np.array([[7], [8]])
np.hstack([xy,x]) # cuando queramos hacer un concatenado horizontal


xy = np.array([[1,2,3],
              [4,5,6]])
print(np.where(xy < 4, 10, 20)) # Para hacer sustituciones
print(np.where(xy < 4, 10, xy)) # primero ponemos la condicion y despues con lo que queremos sustituirlo
# el tercer elemento es lo que quierp que ponga cuando no se cumpla la condicion

copiaxy = xy.copy() 


x = np.array([1, 2, 3, 99, 99, 3, 2, 1])
x1= np.split(x, [3]) # hacemos un corte en el 3
x1, x2, x3 = np.split(x, [2, 5])
print(x1, x2, x3)


grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2]) # hacemos corte a la mitad horizcontal
left, right = np.hsplit(grid, [2]) # hacemos corte a la mitad de forma vertical

L = np.random.random(100)
np.sum(L) #suma de todos los elementos, equivalente a sum(L) pero es mas rapida
np.min(L) # equivalente a min(L), pero mas rapido
np.max(L) # idem

m = np.random.random((3,4))
print(m.sum(axis=0)) # aplicamos dicha operacion al primer eje, idem con min y max

#ALGEBRA

x = np.eye(2) # creando una matriz identidad 3x3
detx = np.linalg.det(x) # calculo de determinantes
x_inv = np.linalg.inv(x) # calculo de inversa
A = np.array([[4, 7],
              [2, 6]])
A_inv = np.linalg.inv(A) # calculo de inversa
A.dot(x) # AxI = A

A = np.array([[1, 2, 3],
              [2, 5, 2],
              [6, -3, 1]])
b = np.array([6, 4, 2])
variables = np.linalg.solve(A, b) # Resolver sistemas de ecuaciones


# ¿Como leer imagenes?
from skimage.io import imread
import matplotlib.pyplot as plt

imagen_a_leer = imread('02-Data_Analysis/01-Numpy/01-Teoria/img/numpy.png') # Ponemos la url de la imagen
plt.imshow(imagen_a_leer) # En ipynb se ve bien, en la terminal solo se ve el array de la imagen
