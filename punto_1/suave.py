import numpy as np
import matplotlib.pylab as plt 
from PIL import Image, ImageOps

#subir la imagen como una matriz (se debe poner entre comillas la ubicacion de la imagen)
def sube_imagen(dire):
	return Image.open(str(dire))


color = sube_imagen('ult.png')

#Cambio de matriz de 3d (color) a matriz 2d (blanco y negro) 
def byn(imag):
	b_n= ImageOps.grayscale(imag)
	b_n.save('ima.png')
	#Subo nueva imagen a blanco y negro para obtener el array
	imab_n = plt.imread('ima.png')

	return imab_n

byne = byn(color)


#Transformada de Fourier en dos dimensiones  
#Parametro m: matriz de la imagen en blanco y negro o matriz de la gaussiana 
def transformada(mtz):
	#Dimensiones de la matriz de la imagen 
	(M,N) = np.shape(mtz)
	
	#Matriz donde se guarda la transformada 
	mtrans = np.zeros((M,N), dtype = complex) 

	k = np.linspace(0.0, N-1, N)
	j = np.linspace(0.0, M-1, M)
	for m in range(M):
		for n in range (N):
			a = k*(float(n)/float(N))
			b = j*(float(m)/float(M))
			expo = (-1j)*(2.0)*(3.1416)*(float(a+b))
			tran_act = np.sum(mtz[m,n]*np.exp(expo))

		mtrans[m,n] = tran_act

	return mtrans

#Gaussiana en dos dimensiones
def transgaus(m):

	#Dimensiones de la matriz de la imagen 
	(M,N) = np.shape(m)

	#Da los centros de la imagen que utilizare en la gaussiana y los guarda en variables globales
	if(M%2 == 0):
		yO = M/2
	else: 
		yO = (M/2)+1
 
	if(N%2 == 0):
		xO = N/2

	else: 
		xO = (N/2)+1
 
	
#Aplicacion de la transformada a la gaussiana 

#Convolucion entre las transformadas (gaussiana e imagen)

#Aplicacion de la transformada inversa al resultado de lo anterior 



