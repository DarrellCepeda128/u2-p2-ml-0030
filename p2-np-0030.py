import numpy as np
# Cepeda Darrell Nc 0030
# Ejemplos de Numerical Python
print("-- Espaciado Linealmente en array -- 0030")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- Matrizidentidad en 2D array -- 0030")
matrix=np.eye(3)
print(matrix)
print("-- Genera numeros al azar(Aleatorios) en 2D array -- 0030")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("genera 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3)) # genera 12 numeros aleatorios
print(numale)
# como generar 9 numeros aleatorios comprendidos entre 1 y 20
# con numpy en un arreglo de 3 por 3
print("generar 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Cepeda Darrell NC 0030")
