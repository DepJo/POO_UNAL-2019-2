""" Reproductor de Contenido Multimedia """

"""
Integrantes:
	Juan Esteban Ochoa
	Delwin Jose Padillas
	Juan Camilo Reyes
	Leonardo Daniel Talledos 
"""

import cv2 #Librería que permite la captura de Fotos y Videos
#import pygame #Libreria utilizada para reproducir Audio
import os #Libreria utilizada para el control y administracion de archivos
from os import scandir, getcwd, rename, remove, system
import time #Libreria utilizada para el control del tiempo

		
class General:

	def __init__(self, seccion):
		pass

	def print_menu(self, menu):
		#Se define la Variable menu
		self.__menu = menu

		#Dependendo del valor de la seccion del objeto se podran imprimir los siguientes Menus
		if (self.seccion == 1): # ----- Canciones -----
			if self.__menu == 'canciones': #Menu principal de las Canciones
				print('{:37}{:37}{:37}\n{:37}{:37}{:37}'.format('[1] Reproducir Cancion','[2] Agregar Cancion','[3] Borrar Cancion','[4] Listas de Reproduccion','[5] Ordenar','[6] Salir'))
			elif self.__menu == 'ordenar': #Menu para reordenar Canciones
				print('{:37}{:37}{:37}\n{:37}{:37}{:37}'.format('[1] Nombre','[2] Autor','[3] Album','[4] Genero','[5] Año','[6] Salir'))
		elif (self.seccion == 11): # ----- Listas de Reproduccion -----
			if self.__menu == 'listas de reproduccion': #Menu principal de las listas de reproduccion
				print('{:37}{:37}{:37}\n{:^90}'.format('[1] Seleccionar Lista','[2] Agregar Lista','[3] Borrar Lista','[6] Salir'))
			elif self.__menu == 'modificar lista': #Menu de Modificacion de Lista
				print('{:27}{:37}{:37}\n{:^90}'.format('[1] Renombrar Lista','[2] Agregar Cancion al la Lista','[3] Borrar Cancion de la Lista ','[6] Salir'))
			elif self.__menu == 'ver lista': #Menu de Reproduccion de Listas
				print('{:37}{:37}{:37}'.format('[1] Reproducir','[2] Ordenar','[6] Salir'))
			elif self.__menu == 'ordenar': #Menu para reordenar Listas
				print('{:37}{:37}{:37}'.format('[1] Nombre','[2] Numero de Canciones','[6] Salir'))				
		elif (self.seccion == 2): # ----- Fotos -----
			if self.__menu == 'fotos': #Menu principal de las Fotos
				print('{:30}{:30}\n{:30}{:30}\n{:30}'.format('[1]Ver Foto','[2] Agregar Foto','[3] Borrar Foto','[4]Ordenar','[5] Salir'))
			elif self.__menu == 'ordenar': #Menu para reordenar Fotos
				print('{:37}{:37}\n{:37}{:37}\n{:37}'.format('[1] Nombre','[2] Autor','[3] Album','[4] Año','[5] Salir'))
		elif (self.seccion == 3): # ----- Videos -----
			if self.__menu == 'videos': #Menu principal de los Videos
				print('{:30}{:30}{:30}{:30}'.format('[1] Agregar Video','[2] Borrar Video','[3] Ordenar','[4]Salir'))
			elif self.__menu== 'ordenar': #Menu para reordenar Videos
			    print('{:37}{:37}\n{:37}{:37}\n{:37}'.format('[1] Nombre','[2] Autor','[3] Album','[4] Año','[5] Salir'))

	def add_media(self):
		#Dependiendo del valor de la seccion del objeto el proceso de agregar un elemento sera diferente
		if (self.seccion == 1): # ----- Canciones -----
			#Abre archivo con base de datos de las Canciones
			self.__datos = open("Datos/Info_canciones.txt","r")
			self.__canciones = self.__datos.read()
			self.__datos.close()
			system('cls')

			#Pide los datos de la Nueva Cancion al Usuario
			print('\n\nUsted eligio agregar una cancion a la lista de canciones \nAsegurese de copiar la cancion que desea agregar en la carpeta "Nueva Musica"\n')
			self.__nombre = input('- Ingrese el nombre de la cancion que desea agregar:\n')
			self.__autor = input('\n- Ingrese el autor de "{}":\n'.format(self.__nombre))
			self.__album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(self.__nombre,self.__autor))
			self.__genero = input('\n- Ingrese el genero de "{}" de "{}":\n'.format(self.__nombre,self.__autor))
			self.__año = input('\n- Ingrese el año de publicacion de "{}" de "{}":\n'.format(self.__nombre,self.__autor))
			
			#Busca la cancion en la carpeta, la renombra y la reubica
			self.__archivos = []
			for self.__archivo in scandir('Nueva Musica'):
				rename(self.__archivo,'Datos/Musica/'+self.__nombre+'.mp3')

			#Organizar la informacion como una cadena
			self.__cancionNueva = [self.__nombre, self.__autor, self.__album, self.__genero, self.__año,'\n']
			self.__cancionNueva = '<>'.join(self.__cancionNueva)
			#Agregar Nueva Cancion a la base de datos
			self.__datos = open("Datos/Info_canciones.txt","w")
			self.__datos.write(self.__canciones+self.__cancionNueva)
			self.__datos.close()
			self.ordenar_all('Nombre',0) #Ordena la lista
			print('Cancion Agregada Con Exito')
			time.sleep(2)
		elif (self.seccion == 2):# ----- Fotos -----
			#Abre archivo con base de datos de las Fotos
			self.__datos = open("Datos/Info_fotos.txt","r")
			self.__fotos = self.__datos.read()
			self.__datos.close()
			system('cls')

			#Mensaje Informativo para el Usuario
			print('\n\nUsted eligio agregar una foto a la lista de fotos\n')
			
			#Inicio de un ciclo de decicion para agregar la Nueva Foto
			self.__bandera = True
			while (self.__bandera):
				print("Elige una de las siguientes opciones:\n", "[T]omar foto\n", "[A]gregar informacion de una foto\n", "[S]alir\n")
				self.__opcion = input(">>")
				system('cls')
				
				if (self.__opcion == "t" or self.__opcion == "T"): # ----- Tomar una Foto con la Camara -----
					#Mensaje de Aviso 
					print("¿Listo para la Foto?\n","\nEn 3...\n")
					time.sleep(1)
					print("2...\n")
					time.sleep(1)
					print("1...\n")
					time.sleep(1)
					print("Ya\n")

					#Usar la Camara para tomar la Foto
					self.__cap=cv2.VideoCapture(0) #Activar camara
					self.__leido,self.__frames = self.__cap.read() #Asegurarse de que este activa
					self.__cap.release() #Desactivar camara
					system('cls')

					#Agregar Informacion de la Foto Tomada
					if (self.__leido==True):
						time.sleep(1)	
						self.__nombre = input('- Ingrese el nombre de la foto que desea agregar:\n')
						self.__autor = input('\n- Ingrese el autor de "{}":\n'.format(self.__nombre))
						self.__album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(self.__nombre,self.__autor))
						self.__genero = "None"
						self.__año = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(self.__nombre,self.__autor))
						
						#Busca la Foto la renombra y la reubica
						self.__path="Datos/Fotos" #Carpeta de almacenamiento
						cv2.imwrite(os.path.join(self.__path, self.__nombre+".jpg"),self.__frames)

						#Organizar la informacion como una cadena
						self.__fotoNueva = [self.__nombre, self.__autor, self.__album, self.__genero, self.__año,"\n"]
						self.__fotoNueva = '<>'.join(self.__fotoNueva)
						#Agregar Nueva Foto a la base de datos
						self.__datos = open("Datos/Info_fotos.txt","w")
						self.__datos.write(self.__fotos+self.__fotoNueva)
						self.__datos.close()
						system('cls')
						self.ordenar_all('Nombre',0) #Ordena la lista			
						print('Foto Agregada Con Exito')
						time.sleep(2)
						self.__bandera=False
					else: #Mensaje de Error si la Foto no es Tomada
						print("Error")
				elif (self.__opcion == "a" or self.__opcion == "A"): # ----- Agregar Informacion de una Foto -----
					#Pide los datos de la Nueva Foto al Usuario
					print('\n\nUsted eligio agregar información de una foto \nAsegurese de copiar la Foto que desea agregar en la carpeta "Nueva Foto"\n')
					self.__nombre = input('- Ingrese el nombre de la foto que desea agregar:\n')
					self.__autor = input('\n- Ingrese el autor de "{}":\n'.format(self.__nombre))
					self.__album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(self.__nombre,self.__autor))
					self.__genero = "None"
					self.__año = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(self.__nombre,self.__autor))

					#Busca la foto en la carpeta, la renombra y la reubica
					for self.__archivo in scandir ('Nueva Foto'):
						rename(self.__archivo,'Datos/Fotos/'+self.__nombre+'.jpg')

					#Organizar la informacion como una cadena
					self.__fotoNueva = [self.__nombre, self.__autor, self.__album, self.__genero, self.__año,"\n"]
					self.__fotoNueva= '<>'.join(self.__fotoNueva)
					#Agregar Nueva Foto a la base de datos
					self.__datos = open("Datos/Info_fotos.txt","w")
					self.__datos.write(self.__fotos+self.__fotoNueva)
					self.__datos.close()
					system('cls')
					self.ordenar_all('Nombre',0) #Ordena la lista
					print('Foto Agregada Con Exito')
					time.sleep(2)
					self.__bandera=False
				elif (self.__opcion== "S" or self.__opcion=="s"): # ----- Salir del ciclo -----
					self.__bandera=False
				else: # ----- Mensaje de error por entrada Incorrecta -----
					print("opcion invalida, vuelva a ingresar\n")
		elif (self.seccion == 3):# ----- Videos -----
			#Abre archivo con base de datos de los Videos
			self.__datos = open("Datos/Info_videos.txt","r")
			self.__videos = self.__datos.read()
			self.__datos.close()
			system('cls')

			#Mensaje Informativo para el Usuario
			print('\n\nUsted eligio agregar un video a la lista de videos\n')

			#Inicio de un ciclo de decicion para agregar el Nuevo Video
			self.__bandera = True
			while (self.__bandera):
				print("Elige una de las siguientes opciones:\n", "[C]apturar video\n", "[A]gregar informacion de un video\n","[S]alir\n")
				self.__option=input(">>") 
				system('cls')

				if (self.__option == "c" or self.__option == "C"): # ------ Grabar un Video con la Camara -----
					#Agregar Informacion del Video Grabado
					self.__nombre = input('- Ingrese el nombre del video que desea agregar:\n')
					self.__autor = input('\n- Ingrese el autor de "{}":\n'.format(self.__nombre))
					self.__album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(self.__nombre,self.__autor))
					self.__genero = "None"
					self.__anio = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(self.__nombre,self.__autor))

					#Organizar la informacion como una cadena
					self.__videoNuevo= [self.__nombre, self.__autor, self.__album, self.__genero, self.__anio,"\n"]
					self.__videoNuevo = '<>'.join(self.__videoNuevo)
					#Agregar Nuevo Video a la base de datos
					self.__datos = open("Datos/Info_videos.txt","w")
					self.__datos.write(self.__videos+self.__videoNuevo)
					self.__datos.close()
					
					#Mensaje de Aviso 				
					print("¿Listo para el Video?\n","En 3...\n")
					time.sleep(1)
					print("2...\n")
					time.sleep(1)
					print("1...\n")
					time.sleep(1)
					print("Ya\n")

					#Usar la Camara para grabar el Video
					self.__vid=cv2.VideoCapture(0) #Activar camara
					self.__frame_width=int(self.__vid.get(3))
					self.__frame_height= int(self.__vid.get(4))

					#Busca el Video lo renombra y lo reubica
					self.__path="Datos/Videos" #Carpeta de almacenamiento	
					self.__out = cv2.VideoWriter(os.path.join(self.__path,self.__nombre+".avi"),cv2.VideoWriter_fourcc('M','J','P','G'), 15, (self.__frame_width,self.__frame_height))
					
					#Ciclo para grabar el Video
					while (True):
						self.__ret,self.__frame = self.__vid.read() #Asegurarse de que este activa
						
						if (self.__ret == True):

							self.__out.write(self.__frame)

							cv2.imshow("Imagen",self.__frame)

						self.__exit=cv2.waitKey(1) & 0xFF
						if (self.__exit==27):
							break
					else:
						break
					#Finalizar proceso de Grabado
					self.__vid.release()
					self.__out.release() #Desactivar camara
					cv2.destroyAllWindows()
					system('cls')
					self.ordenar_all('Nombre',0) #Ordena la lista
					print('Video Agregado Con Exito')
					time.sleep(2)
					self.__bandera = False

				elif (self.__option == "a" or self.__option == "A"): # ----- Agregar Informacion de un Video -----
					#Pide los datos del Nueva Video al Usuario
					print('\n\nUsted eligio agregar la informacion de un video \nAsegurese de copiar el video que desea agregar en la carpeta "Nuevo Video"\n')
					self.__nombre = input('- Ingrese el nombre del video que desea agregar:\n')
					self.__autor = input('\n- Ingrese el autor de "{}":\n'.format(self.__nombre))
					self.__album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(self.__nombre,self.__autor))
					self.__genero = "None"
					self.__año = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(self.__nombre,self.__autor))
					
					#Busca el viedo en la carpeta, lo renombra y lo reubica
					self.__path="Datos/Videos"
					for archivo in scandir ('Nuevo Video'):
						rename(archivo,os.path.join(self.__path, self.__nombre+".avi"))

					#Organizar la informacion como una cadena
					self.__videoNuevo = [self.__nombre, self.__autor, self.__album, self.__genero, self.__año,"\n"]
					self.__videoNuevo = '<>'.join(self.__videoNuevo)
					#Agregar Nuevo Viedo a la base de datos
					self.__datos = open("Datos/Info_videos.txt","w")
					self.__datos.write(self.__videos+self.__videoNuevo)
					self.__datos.close()
					system('cls')
					self.ordenar_all('Nombre',0) #Ordena la lista
					print('Video Agregado Con Exito')
					time.sleep(2)
					self.__bandera=False
				
				elif (self.__option== "S" or self.__option=="s"): # ----- Salir del ciclo -----
					self.__bandera=False
				
				else: #Mensaje de error por entrada Incorrecta
					print("Opcion invalida, vuelva a ingresar\n")

	def all_tabla(self):
		#Dependiendo del valor de la seccion del objeto se usara la lista de la base de datos correspondiente y un titulo para esta
		if (self.seccion == 1 or self.seccion == 11): # ----- Canciones -----
			self.__lista = "Datos/Info_canciones.txt"
			self.__titulo = "Canciones"
		elif (self.seccion == 2): # ----- Fotos -----
			self.__lista = "Datos/Info_fotos.txt"
			self.__titulo = "Fotos"
		elif (self.seccion == 3): # ----- Videos -----
			self.__lista = "Datos/Info_videos.txt"
			self.__titulo = "Videos"

		#Abre archivo con base de datos respectiva
		self.__datos = open(self.__lista,"r")
		self.__lista = self.__datos.readlines()
		self.__datos.close()
		system('cls')
		#Imprime el titulo y las tablas
		print('{:^90}'.format('Todas las {}'.format(self.__titulo)))
		self.print_tabla(self.__lista)

	def print_tabla(self, lista):
		#Define Variables
		self.__lista = lista
		self.__encabezado = '\n\n{:^10}{:20}{:20}{:20}{:20}{:20}'.format('Num','Nombre','Autor','Album','Genero','Año')
		self.__linea = '-'*95
		self.__cont = 0

		#Imprime toda la tabla
		print(self.__encabezado)
		print(self.__linea+'\n')
		for self.__i in self.__lista:
			self.__cont += 1
			self.__media = self.__i.split('<>')
			self.__tabla = '{:^10}{:20}{:20}{:20}{:20}{:20}{}'.format(self.__cont,self.__media[0],self.__media[1],self.__media[2],self.__media[3],self.__media[4],self.__media[5])
			print(self.__tabla)

	def search_media(self, lista):
		#Dependiendo del valor de la seccion del objeto se usara un lista de busqueda
		self.__lista = lista
		if self.__lista == 0:
			if (self.seccion == 1 or self.seccion == 11): # ----- Canciones -----
				self.__lista = "Datos/Info_canciones.txt"
			elif (self.seccion == 2): # ----- Fotos -----
				self.__lista = "Datos/Info_fotos.txt"
			elif (self.seccion == 3): # ----- Videos -----
				self.__lista = "Datos/Info_videos.txt"

		#Abre el archivo con la base de datos
		self.__datos = open(self.__lista,"r")
		self.__lista = self.__datos.readlines()
		self.__datos.close()
		#Resive el valor de busqueda
		self.__busqueda = str(input('\nIngrese el Nombre del archivo, una palabra o frase clave:\n'))
		self.__resultadosBusqueda = [] #Lista de resultados

		#Proceso de busqueda por medio de comparacion del valor de busqueda y los atributos de la media
		for self.__i in self.__lista:
		    self.__media = self.__i.split('<>')
		    for self.__atributo in self.__media:
		        if (self.__atributo == self.__busqueda):
		        	self.__resultadosBusqueda.append(self.__i)

		#Mensaje de busqueda sin resutados
		if self.__resultadosBusqueda == []:
		    print('\nNo se han encontrado resultados con "{}":'.format(self.__busqueda))
		    time.sleep(3)
		    return

		#Imprime la lista de resultados
		system('cls')
		print('\n\nLos resultados de la busqueda de "{}" son:'.format(self.__busqueda))
		self.print_tabla(self.__resultadosBusqueda)

		#Inicia ciclo de seleccion de resultados
		self.__seleccionar = True
		while self.__seleccionar:
			#Verifica que el numero seleccionado se encuentre dentro del rango de resultados
			self.__desicion = int(input('Ingrese el numero del archivo que desea seleccionar:\n'))
			if (self.__desicion > 0) and (self.__desicion <= len(self.__resultadosBusqueda)):
				self.__seleccionar = False
			else:
				print('No existe ese numero de archivo')
				continue

		#Con el numero resivido la funcion retorna una cadena con la informacion de la cancion
		self.__resultado = self.__resultadosBusqueda[self.__desicion-1] 
		system('cls')
		return self.__resultado

	def delet_media(self, eliminar):
		#Dependiendo del valor de la seccion del objeto se usara una lista, una carpeta de ubicacion y una extencion para el archivo
		self.__eliminar = eliminar
		if (self.seccion == 1): # ----- Canciones -----
			self.__lista = "Datos/Info_canciones.txt"
			self.__carpeta = 'Datos/Musica/'
			self.__extension = '.mp3'
		elif (self.seccion == 2): # ----- Fotos -----
			self.__lista = "Datos/Info_fotos.txt"
			self.__carpeta = 'Datos/Fotos/'
			self.__extension = '.jpg'
		elif (self.seccion == 3): # ----- Videos -----
			self.__lista = "Datos/Info_videos.txt"
			self.__carpeta = 'Datos/Videos/'
			self.__extension = '.avi'

		#Abre el archivo con la base de datos
		self.__datos = open(self.__lista,"r")
		self.__elementos = self.__datos.readlines()
		self.__datos.close()

		#Compara los elementos con informacion a eliminar
		for self.__i in self.__elementos:
			if (self.__i == self.__eliminar):
				self.__elementos.remove(self.__i)
				self.__media = self.__i.split('<>')
				self.__nombre = self.__media[0]
				#Trata de eliminar el archivo vinculado a la informacion en caso que exista
				try:
					remove(self.__carpeta+self.__nombre+self.__extension)
				except FileNotFoundError: 
					pass

		#Reacomoda la informacion y la escribe en la base de datos
		self.__elementos = ''.join(self.__elementos)
		self.__datos = open(self.__lista,"w")
		self.__datos.write(self.__elementos)
		self.__datos.close()

	def ordenar_all(self,factor,lista):
		#Se definen varibles
		self.__factor = factor
		self.__lista = lista
		#Dependiendo del valor de la seccion del objeto se utilisa una lista respectivamente
		if (self.__lista == 0):
			if (self.seccion == 1): # ----- Canciones -----
				self.__lista = "Info_canciones"
			elif (self.seccion == 2): # ----- Fotos -----
				self.__lista = "Info_fotos"
			elif (self.seccion == 3): # ----- Videos -----
				self.__lista = "Info_videos"

		#Abre el archivo con la base de datos
		self.__datos = open("Datos/"+self.__lista+".txt","r")
		self.__elementos = self.__datos.readlines()
		self.__datos.close()

		#Redefine el valor de factor asignandole un valor numerico
		if self.__factor == 'Nombre':
			self.__factor = 0
		elif self.__factor == 'Autor':
			self.__factor = 1
		elif self.__factor == 'Album':
			self.__factor = 2
		elif self.__factor == 'Genero':
			self.__factor = 3
		elif self.__factor == 'Año':
			self.__factor = 4
		elif self.__factor == 'NombreLista':
			self.__factor = 0
		elif self.__factor == 'NumeroDeCanciones':
			self.__factor = 1

		#Guarda el atributo de elemento segun el factor dado
		self.__listaDeOrden = [] #Lista de los atributos
		for self.__i in self.__elementos:
			self.__media = self.__i.split('<>')
			self.__atributo = self.__media[self.__factor]
			if self.__atributo not in self.__listaDeOrden:
				self.__listaDeOrden.append(self.__atributo) #Agrega el atributo a lalista
		self.__listaDeOrden.sort(key = str.lower) #Ordena alfabeticamente los atributos sin tomar en cuenta las mayusculas

		#Agrega la informacion de la cancion con el orden de los atributos anteriores
		self.__listaOrdenada = [] #Lista de los elementos ordenados
		for self.__i in self.__listaDeOrden:
			for self.__j in self.__elementos:
				self.__media = self.__j.split('<>')
				for self.__atributo in self.__media:
					if self.__atributo == self.__i:
						self.__listaOrdenada.append(self.__j) #Agrega un elemento a la lista conforme el orden establecido

		#Organiza la informacion y la escribe en la base de datos
		self.__listaOrdenada = ''.join(self.__listaOrdenada)
		self.__datos = open("Datos/"+self.__lista+".txt","w") #guarda los datos pero ahora ordenados
		self.__datos.write(self.__listaOrdenada)
		self.__datos.close()


class Canciones(General):

	def __init__(self):
		self.seccion = 1

	def play_media(self, reproducir, lista):
		#Se definen variables
		self.__reproducir = reproducir
		self.__lista = lista
		if self.__lista == 0:
			self.__lista = 'Info_canciones'
		self.__cancion = self.__reproducir.split('<>')
		self.__nombre = self.__cancion[0]
		self.__autor = self.__cancion[1]
		self.__album = self.__cancion[2]
		self.__file = 'Datos/Musica/'+self.__nombre+'.mp3'

		#Se carga y reproduce el archivo
		pygame.init()
		pygame.display.set_mode((200,100)) #Inicializa una ventana
		pygame.mixer.music.load(self.__file) #Carga el archivo de musica
		pygame.mixer.music.play(0) #Reproduce el archivo de musica
		system('cls')

		#Se inicia ciclo de reproduccion
		self.__play = True
		while pygame.mixer.music.get_busy(): #Mientras se este reproduciendo
			print('\n{:^30}-{:^30}-{:^30}\n'.format(self.__nombre, self.__autor, self.__album))
			self.__desicion = input("""\n[1] Anterior    [2] Play/Pause      [3] Siguiente
			
			[4] Regresar\n""")
			if self.__desicion == '1': # ----- Regresar Cancion ------
				#Abre la base de datos de la lista
				self.__datos = open("Datos/"+self.__lista+".txt","r")
				self.__canciones = self.__datos.readlines()
				self.__datos.close()

				#Encuentra el numero de la cancion en la lista y modifica el indice
				for self.__i in self.__canciones:
					if (self.__i == self.__reproducir):
						self.__numero = self.__canciones.index(self.__i)
				self.__numero -= 1 #Le resta uno al indice para reproducir la cancion anterior
				if (self.__numero < 0):
					self.__numero = (len(self.__canciones)) - 1
				pygame.mixer.music.stop() #Detiene la reproduccion de la cancion actual

				#Redefine variables
				self.__reproducir = self.__canciones[self.__numero]
				self.__cancion = self.__reproducir.split('<>')
				self.__nombre = self.__cancion[0]
				self.__autor = self.__cancion[1]
				self.__album = self.__cancion[2]
				self.__file = 'Datos/Musica/'+self.__nombre+'.mp3'
				#Reproduce la cancion con el nuevo indice
				pygame.mixer.music.load(self.__file)
				pygame.mixer.music.play(0) 
			elif self.__desicion == '2': # ----- Play o Pause a la Cancion -----
				if self.__play == True:
					self.__play = False
					pygame.mixer.music.pause() #detiene la reproduccion temporalmente
				else:
					self.__play = True
					pygame.mixer.music.unpause()
			elif self.__desicion == '3': # ----- Avanzar Cancion ----- 
				#Abre la base de datos de la lista
				self.__datos = open("Datos/"+self.__lista+".txt","r")
				self.__canciones = self.__datos.readlines()
				self.__datos.close()

				#Encuentra el numero de la cancion en la lista y modifica el indice
				for self.__i in self.__canciones:
					if (self.__i == self.__reproducir):
						self.__numero = self.__canciones.index(self.__i)
				self.__numero += 1 #Le suma uno al indice para reproducir la cancion siguiente
				if (self.__numero == len(self.__canciones)):
					self.__numero = 0
				pygame.mixer.music.stop() #Detiene la reproduccion actual
				
				#Redefine variables
				self.__reproducir = self.__canciones[self.__numero]
				self.__cancion = self.__reproducir.split('<>')
				self.__nombre = self.__cancion[0]
				self.__autor = self.__cancion[1]
				self.__album = self.__cancion[2]
				self.__file = 'Datos/Musica/'+self.__nombre+'.mp3'
				#Reproduce la cancion con el nuevo indice
				pygame.mixer.music.load(self.__file)
				pygame.mixer.music.play(0) 
			elif self.__desicion == '4': # ----- Salir -----
				pygame.mixer.music.stop()
				pygame.display.quit() #cierra la ventana de reproduccion
			else: # ----- Mensaje de opcion invalida -----
				print('Valor Erroneo')
			system('cls')

class Listas(Canciones):

	def __init__(self):
		self.seccion = 11

	def all(self):
		#Abre la bse de datos de las listas
		self.__datos = open("Datos/Info_listas.txt","r")
		self.__listas = self.__datos.readlines()
		self.__datos.close()
		system('cls')

		#Imprime el titulo y las listas
		print('{:^90}'.format('Todas las Listas'))
		self.print(self.__listas)

	def print(self, lista):
		#Difine variables
		self.__conjunto = lista
		self.__encabezado = '\n\n{:^10}{:50}{:20}'.format('Num','Nombre de la Lista de Reproduccion','Numero de canciones')
		self.__linea = '-'*95
		print(self.__encabezado)
		print(self.__linea+'\n')

		#Imprime toda la tabla
		self.__cont = 0
		for self.__i in self.__conjunto:
			self.__cont += 1
			self.__lista = self.__i.split('<>')
			self.__tabla = '{:^10}{:50}{:^20}{}'.format(self.__cont, self.__lista[0], self.__lista[1], self.__lista[2])
			print(self.__tabla) 

	def add_media(self, titulo):
		#Define Variables
		self.__titulo = titulo
		#Abre la base de datos
		self.__datos = open("Datos/"+self.__titulo+".txt","r")
		self.__canciones = self.__datos.read()
		self.__datos.close()
		system('cls')

		#Pide la informacion de la cancion
		self.all_tabla()
		print('\nIngrese las canciones que desea agregar a la lista de Reproduccion "{}"'.format(self.__titulo))
		self.__resultado = self.search_media(0)
		if self.__resultado != None: #La agrega si es posible
			self.__datos = open("Datos/"+self.__titulo+".txt","w")
			self.__datos.write(self.__canciones+self.__resultado)
			self.__datos.close()
			self.ordenar_all('Nombre', self.__titulo) #Ordena la lista
			print('Cancion Agregada Con Exito')
			time.sleep(2)
			return True
		else:
			return False

	def add(self):
		#Abre la base de datos
		self.__datos = open("Datos/Info_listas.txt","r")
		self.__listas = self.__datos.read()
		self.__datos.close()

		#Pide la informacion de la nueva lista
		system('cls')
		print('\n\nUsted eligio agregar una lista de Reproduccion\n')
		self.__titulo = input('- Ingrese el nombre de la lista de Reproduccion que desea agregar:\n')
		self.__listaNueva = open("Datos/"+self.__titulo+".txt","w")
		self.__listaNueva.close()

		#Agrega por lo menos una cancion
		self.__cant = 0
		self.__agregar = True
		while self.__agregar: #agrega canciones continuamente hasta que el usuario determine lo contrario
			self.__confirmacion = self.add_media(self.__titulo)
			if self.__confirmacion == True:
				self.__cant += 1
			elif self.__confirmacion == False:
				if (self.__cant == 0):
					continue
			#Decicion de agregar mas canciones
			self.__seguir = True
			while self.__seguir:
				system('cls')
				self.__choise = input('¿Desea agregar otra Cancion?\n   [1] Si     [6] No\n')
				if (self.__choise == '1'):
					self.__seguir = False
				if (self.__choise == '6'):
					self.__seguir = False
					self.__agregar = False

		#Ordena la Infomacion
		self.__listaNueva = [self.__titulo, str(self.__cant),'\n']
		self.__listaNueva = '<>'.join(self.__listaNueva)
		#Lo escribe en la base de datos
		self.__datos = open("Datos/Info_listas.txt","w")
		self.__datos.write(self.__listas+self.__listaNueva)
		self.__datos.close()

	def delet(self, eliminar):
		#Define Variables
		self.__eliminar = eliminar
		#Abre la base de datos
		self.__datos = open("Datos/Info_listas.txt","r")
		self.__listas = self.__datos.readlines()
		self.__datos.close()

		#Busca y elimina la lista
		for self.__i in self.__listas:
			if (self.__i == self.__eliminar):
				self.__listas.remove(self.__i)
				self.__lista = self.__i.split('<>')
				self.__nombre = self.__lista[0]
				remove('Datos/'+self.__nombre+'.txt')

		#Organiza la informacion y la escribe en la base de datos
		self.__listas = ''.join(self.__listas)
		self.__datos = open("Datos/Info_listas.txt","w")
		self.__datos.write(self.__listas)
		self.__datos.close()

	def search(self):
		#Abre la base de datos
		self.__datos = open("Datos/Info_listas.txt","r")
		self.__listas = self.__datos.readlines()
		self.__datos.close()
		#Pide el valor de busqueda
		self.__busqueda = str(input('\nIngrese el Nombre de la Lista de reproduccion, una palabra o frase clave:\n'))
		self.__resultadosBusqueda = []

		#Busca coincidencias entre las listas y la palabra clave
		for self.__i in self.__listas: 
			self.__lista = self.__i.split('<>')
			for self.__atributo in self.__lista:
				if (self.__atributo == self.__busqueda):
					self.__resultadosBusqueda.append(self.__i)

		system('cls')
		if self.__resultadosBusqueda == []:
			print('\nNo se han encontrado resultados con "{}":'.format(self.__busqueda))
			time.sleep(3)
			return
		#Muestra los resultados
		print('\n\nLos resultados de la busqueda de "{}" son:'.format(self.__busqueda))
		self.print(self.__resultadosBusqueda)

		#Pide el numero de la lista que se desea seleccionar
		self.__seleccionar = True
		while self.__seleccionar:
			self.__desicion = int(input('Ingrese el numero de la cancion que desea seleccionar:\n'))
			if (self.__desicion > 0) and (self.__desicion <= len(self.__resultadosBusqueda)): #se asegura que la cancion este dentro del rango
				self.__seleccionar = False
			else:
				print('No existe ese numero de cancion')
				continue

		#Acomoda la informacion y la retorna
		self.__resultado = self.__resultadosBusqueda[self.__desicion-1] 
		system('cls')

		return self.__resultado

class Fotos(General):
	
	def __init__(self):
		self.seccion = 2

	def show_media(self, mostrar):
		#Se definen variables
		self.__mostrar = mostrar
		#Se abre el archivo con la base de datos de las fotos
		self.__datos = open("Datos/Info_fotos.txt","r")
		self.__fotos = self.__datos.readlines()
		self.__datos.close()

		#Se busca la imagen y se muestra
		self.__cont = 0
		for self.__i in self.__fotos:
			if (self.__i == self.__mostrar):
				while(self.__mostrar[self.__cont] != "<"):
					self.__cont += 1
				self.__direccion = self.__i[:self.__cont]
				self.__nombre = self.__direccion[:]+".jpg"
				self.__path = "Datos/Fotos" #Carpeta de almacenamiento
				self.__img = cv2.imread(os.path.join(self.__path, self.__nombre),cv2.IMREAD_UNCHANGED) #Leer imagen
				cv2.imshow("foto", self.__img) #Mostrar imagen en ventana externa
				self.__key = cv2.waitKey(0) & 0xFF
				if (self.__key == 27):
					cv2.destroyAllWindows() #Cerrar las ventanas externas

class Videos(General):
	
	def __init__(self):
		self.seccion = 3



def main_canciones(): # --- Funcion que ejecuta la Seccion Canciones ---
	#Crea el objeto que controlara todas las funciones de la seccion Canciones
	music= Canciones()
	#Ciclo de ejecucion de la seccion Canciones
	while True:
		system('cls')
		music.all_tabla()
		music.print_menu('canciones')
		eleccion = input()
		if (eleccion == '1'): # --- Reproducir Cancion ---
			system('cls')
			music.all_tabla()
			resultado = music.search_media(0)
			if resultado == None:
				continue
			music.play_media(resultado, 0)
		elif (eleccion == '2'): # --- Agregar Cancion ---
			system('cls')
			music.add_media()
		elif (eleccion == '3'): # --- Eliminar Cancion ---
			system('cls')
			music.all_tabla()
			resultado = music.search_media(0)
			if resultado == None:
				continue
			music.delet_media(resultado)
		elif (eleccion == '4'):
			#Crea el objeto que controla todas las funciones de la seccion Listas
			lista = Listas()
			#Ciclo de ejecucion de la seccion Listas
			verListas = True
			while verListas:
				system('cls')
				lista.all()
				lista.print_menu('listas de reproduccion')
				eleccion = input()
				if (eleccion == '1'): # --- Reproducir una Lista ---
					system('cls')
					lista.all()
					resultado = lista.search()
					if resultado == None:
						continue
					resultado = resultado.split('<>')
					titulo = resultado[0]
					datos = open("Datos/"+titulo+".txt","r")
					canciones = datos.readlines()
					datos.close()
					system('cls')
					lista.print_tabla(canciones)
					resultado = lista.search_media("Datos/"+titulo+".txt")
					if resultado == None:
						continue
					lista.play_media(resultado, titulo)
				elif (eleccion == '2'): # --- Agregar Lista ---
					system('cls')
					lista.add()
				elif (eleccion == '3'): # --- Eliminar Lista ---
					system('cls')
					lista.all()
					resultado = lista.search()
					if resultado == None:
						continue
					lista.delet(resultado)
				elif (eleccion == '6'):
					verListas = False
		elif (eleccion == '5'): # --- Ordenar Canciones ---
			while True:
				system('cls')
				music.all_tabla()
				print('Como desea ordenar su Musica')
				music.print_menu('ordenar')
				parametro = input()
				if parametro == '1':
					music.ordenar_all('Nombre', 0)
				elif parametro == '2':
					music.ordenar_all('Autor', 0)
				elif parametro == '3':	
					music.ordenar_all('Album', 0)
				elif parametro == '4':	
					music.ordenar_all('Genero', 0)
				elif parametro == '5':	
					music.ordenar_all('Año', 0)
				elif parametro == '6':	
					break
				else:
					print("Ese parametro no existe")
					time.sleep(1)
		elif (eleccion == '6'): # --- Salir ---
			print("Salio exitosamente\n")
			time.sleep(1)
			break
		else: # --- Mensaje de opcion invalida ---
			print("Opcion invalida, intentelo otra vez")
			time.sleep(1)

def main_fotos(): # --- Funcion que ejecuta la Seccion Fotos ---
	#Crea el objeto que controlara todas las funciones de la seccion Fotos
	photo = Fotos()
	#Ciclo de ejecucion de la seccion Fotos
	while (True):
		system('cls')
		photo.all_tabla()
		photo.print_menu('fotos')
		eleccion = input(">> ")
		if (eleccion == "1"): # --- Ver Foto ---
			system('cls')
			photo.all_tabla()
			resultado = photo.search_media(0)
			if (resultado == None):
				continue
			photo.show_media(resultado)
		elif (eleccion == "2"): # --- Agregar Foto ---
			system('cls')
			photo.add_media()
		elif (eleccion == "3"): # --- Eliminar Foto ---
			system('cls')
			photo.all_tabla()
			resultado = photo.search_media(0)
			if (resultado == None):
				continue
			photo.delet_media(resultado)
		elif (eleccion == "4"): # --- Ordenar Fotos ---
			while True:
			    system('cls')
			    photo.all_tabla()
			    print('Como desea ordenar sus Fotos')
			    photo.print_menu('ordenar')
			    parametro = input()
			    if parametro == '1':
			    	photo.ordenar_all('Nombre', 0)
			    elif parametro == '2':
			    	photo.ordenar_all('Autor', 0)
			    elif parametro == '3':	
			    	photo.ordenar_all('Album', 0)
			    elif parametro == '4':	
			    	photo.ordenar_all('Año', 0)
			    elif parametro == '5':	
			    	break
			    else:
			    	print("Ese parametro no existe")
			    	time.sleep(1)
		elif (eleccion == "5"): # --- Salir ---
			print("Salio exitosamente\n")
			time.sleep(1)
			break
		else: # --- Mensaje de opcion invalida ---
			print("Opcion invalida, intentelo otra vez")
			time.sleep(1)

def main_videos(): # --- Funcion que ejecuta la Seccion Videos ---
	#Crea el objetos que controlara todas las funciones de la seccion Videos
	video = Videos()
	#Ciclo de ejecucion de la seccion Videos
	while (True):
		system('cls')
		video.all_tabla()
		video.print_menu('videos')
		eleccion = input(">> ")
		if (eleccion == "1"): # --- Agregar Video ---
			system('cls')
			video.add_media()
		elif (eleccion == "2"): # --- Eliminar Video ---
			system('cls')
			video.all_tabla()
			resultado = video.search_media(0)
			if (resultado == None):
				continue
			video.delet_media(resultado)
		elif (eleccion == '3'): # --- Ordenar Videos ---
			while True:
				video.all_tabla()
				print('Como desea ordenar sus Videos')
				video.print_menu('ordenar')
				parametro = input()
				if parametro == "1":
					video.ordenar_all('Nombre', 0)
				elif parametro == "2":
					video.ordenar_all('Autor', 0)
				elif parametro == "3":	
					video.ordenar_all('Album', 0)
				elif parametro == "4":	
					video.ordenar_all('Año', 0)
				elif parametro == "5":	
					break
				else:
					print("Ese parametro no existe")
					time.sleep(1)
		elif (eleccion == "4"): # --- Salir ---
			print("Salio exitosamente\n")
			time.sleep(1)
			break
		else: # --- Mensaje de opcion invalida ---
			print("Opcion invalida, intentelo otra vez")
			time.sleep(1)

def main(): # --- Funcion Principal del Programa ---
	#Funcion Principal que iniciara la ejecucion de cada seccion
	while(True):
		system('cls')
		print("BIENVENIDO A TU ORGANIZADOR MULTIMEDIA\n")
		print('{:30}{:30}\n{:30}{:30}'.format('[1] MUSICA','[2] FOTOS','[3] VIDEOS','[4]SALIR'))
		ver = input(">> ")
		if (ver == "1"): # --- Ejecutar Seccion Musica ---
			main_canciones()
		elif (ver == "2"): # --- Ejecutar Seccion Fotos---
			main_fotos()
		elif (ver == "3"): # --- Ejecutar Seccion Videos ---
			main_videos()
		elif (ver == "4"): # --- Salir ---
			print("Salio exitosamente\n")
			time.sleep(1)
			break
		else: # --- Mensaje de Opcion Invalida ---
			print("Opcion invalida, intentelo otra vez")
			time.sleep(1)


main()
