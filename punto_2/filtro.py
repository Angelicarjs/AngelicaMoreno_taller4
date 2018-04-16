#subir la imagen como una matriz (se debe poner entre comillas la ubicacion de la imagen)
def sube_imagen(dire):
	return Image.open(str(dire))

color = sube_imagen('jhh.png')

#Cambio de matriz de 3d (color) a matriz 2d (blanco y negro) 
def byn(imag):
	b_n= ImageOps.grayscale(imag)
	b_n.save('ima.png')
	#Subo nueva imagen a blanco y negro para obtener el array
	
	return imab_n

byne = byn(color)

plt.figure()
plt.imshow(byne)
plt.show()

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


