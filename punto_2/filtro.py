import numpy as np
import matplotlib.pylab as plt 
from PIL import Image, ImageOps 

#subir la imagen como una matriz (se debe poner entre comillas la ubicacion de la imagen)
def sube_imagen(dire):
	return Image.open(str(dire))

color = sube_imagen('jhh.png')

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
	for i in range(M):
		for j in range(N):
			tran_act = 0.0
			for m in range(M):
				for n in range (N):
					a = i*(float(n)/float(N))
					b = j*(float(m)/float(M))
					expo = (-1j)*(2.0)*(3.1416)*(float(a+b))
					tran_act += mtz[m,n]*np.exp(expo)
			
			mtrans[i,j] = tran_act
	return mtrans

transima = transformada(byne)

#Filtros que se les pasa por parametro la matriz transformada de la imagen 

#Filtro pasa bajos
def bajos(mtz):
	(Mt,Nt) = np.shape(mtz) 
	for n in range(Nt):
		for m in range(Mt):
			actual = mtz[n,m]
			if(actual>):
				actual = 0.0
	return mtz

#Filtro pasa altos 				
def altos(mtz):
	(Mt,Nt) = np.shape(mtz)
	for n in range(Nt):
		for m in range(Mt):
			actual = transima[n,m]
			if(actual<):
				actual = 0.0
	return mtz	
		
ba = bajos(transima)

print ba

#Gaussiana en dos dimensiones generada a partir de la matriz de la imagen que entra como parametro
def gaussiana(mtz):

	#Dimensiones de la matriz de la imagen 
	(M,N) = np.shape(mtz)

	#Matriz donde se guarda la gaussiana
	mgauss = np.zeros((M,N), dtype = complex)
	
	#Da los centros de la imagen que utilizare en la gaussiana y los guarda en variables globales
	yO = 0.0
	xO = 0.0

	if(M%2 == 0):
		yO = M/2
	else: 
		yO = (M/2)+1
 	
	if(N%2 == 0):
		xO = N/2

	else: 
		xO = (N/2)+1
 	
	#ancho de la gaussiana 
	sigma = 0.3
	
	A = 1.0 / (np.sqrt(2.0*3.1416*sigma*sigma))
	for y in range(M):
		for x in range(N):
			gx = float((x-xO)**2)/2.0*sigma*sigma
			gy = float((y-yO)**2)/2.0*sigma*sigma
			mgauss[y,x] = A*(np.exp(-(gx+gy)))
	return mgauss

ga = gaussiana(byne)

#Aplicacion de la transformada a la gaussiana 
transgau= transformada(ga)

#Convolucion entre las transformadas (gaussiana e imagen)
con= transgau*transim

#Funcion que retorna la inversa de la transformada de Fourier
def invtra(mtz):
	#Dimensiones de la matriz de la imagen 
	(M,N) = np.shape(mtz)
	
	#Matriz donde se guarda la transformada 
	mtrans = np.zeros((M,N), dtype = float) 
	for m in range(M):
		for n in range(N):
			tran_act = 0.0
			for i in range(M):
				for j in range (N):
					a = i*(float(n)/float(N))
					b = j*(float(m)/float(M))
					expo = (1j)*(2.0)*(3.1416)*(float(a+b))
					tran_act += mtz[m,n]*np.exp(expo)
			
			mtrans[m,n] = tran_act
	return mtrans

#Aplicacion de la transformada inversa al resultado de lo anterior entra como parametro la matriz de la convoluncion anteriormente realizada 

rta = invtra(con)

#plt.figure()
#plt.imread(rta)
#plt.show()
#plt.save("suave.png")
