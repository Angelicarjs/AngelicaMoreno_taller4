import numpy as np
import matplotlib.pylab as plt 
from scipy.fftpack import fft,fftfreq

#subir la imagen como una matriz
imagenc = plt.imread('jh.png')
plt.figure(1, figsize=(9.5,9))
plt.imshow(imagenc)
#plt.show()

#Cambio de matriz de 3d (color) a matriz 2d (blanco y negro) 
imagenbyn = imagenc[:,:,0]
plt.imshow(imagenbyn)
plt.show()

#Transformada de Fourier en dos dimensiones aplicada a la matriz de la imagen 
def transformada(matriz):
	for n in range(0,N):	
		expo = (-1j)*(2.0)*(3.1416)*m*(float(n)/float(N))
		tran = np.sum(y*np.exp(expo))
		listaf.append(tran)
#Gaussiana en dos dimensiones

#Aplicación de la transformada a la gaussiana 

#Convolucion entre las transformadas (gaussiana e imagen)

#Aplicacion de la transformada inversa al resultado de lo anterior 






