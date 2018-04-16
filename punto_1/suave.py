import numpy as np
import matplotlib.pylab as plt 
import sys 
from PIL import Image, ImageOps 
import cmath

#sigma(ancho de la gaussiana) y nombre de la imagen a la que se le quiere aplicar ingresada por el usuario
sig = sys.argv[2]
nombre = sys.argv[1]

#subir la imagen como una matriz blanco y negro (se debe poner entre comillas la ubicacion de la imagen)
def sube_imagen(dire):
	cargo = Image.open(dire)
	b_n = cargo.convert('L')
	b_n.save('ima.png')
	#Subo nueva imagen a blanco y negro para obtener el array
	imab_n = plt.imread('ima.png')
	return imab_n

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
			
			mtrans[i,j] = tran_act/N/M
	return mtrans
	
	
#Gaussiana en dos dimensiones generada a partir de la matriz de la imagen que entra como parametro
def gaussiana(mtz, sigma):

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
 		
	A = 1.0 / (np.sqrt(2.0*3.1416*float(sigma)**2))
	for y in range(M):
		for x in range(N):
			gx = float((x-xO)**2)/(2.0*float(sigma)**2)
			gy = float((y-yO)**2)/(2.0*float(sigma)**2)
			mgauss[y,x] = A*(np.exp(-(gx+gy)))
	return mgauss

#Funcion que retorna la inversa de la transformada de Fourier
def invtra(mtz):
	#Dimensiones de la matriz de la imagen 
	(M,N) = np.shape(mtz)

	mtrans = np.zeros((M,N), dtype= float)
	for m in range(M):
		for n in range(N):
			tran_act = 0.0
			for i in range(M):
				for j in range(N):
					a = float(i*m)/float(M) 
					b = float(j*n)/float(N)
					expo = 1j*2.0*3.1416*(a+b)
					tran_act += mtz[j][i] * np.exp(expo)
			mtrans[m,n]=(tran_act.real)
	return (mtrans)


#Sube imagen que ingreso el usuario 
byne = sube_imagen(nombre)

#Aplicacion de la transformada a la imagen 
transim = transformada(byne)

#Aplicacion de la gaussiana a la matriz de la imagen 
ga = gaussiana(byne,sig)

#Aplicacion de la transformada a la gaussiana 
transgau= transformada(ga)

#Convolucion entre las transformadas (gaussiana e imagen)
con= transgau*transim

#Aplicacion de la transformada inversa al resultado de lo anterior entra como parametro la matriz de la convoluncion anteriormente realizada 

rta = invtra(con)

plt.figure()
plt.imshow(rta, cmap="gray")
plt.save("suave.png")

