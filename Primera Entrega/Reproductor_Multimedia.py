import cv2 #Librería que permite la captura de fotos y videos
import os
from os import scandir, getcwd, rename, remove, system
import time
#import pygame
import numpy as np

def ordenar_all(factor,lista):
	datos = open("Datos/"+lista+".txt","r")
	canciones = datos.readlines()
	datos.close()

	if factor == 'Nombre':
		factor = 0
	elif factor == 'Autor':
		factor = 1
	elif factor == 'Album':
		factor = 2
	elif factor == 'Año':
		factor = 4
	listaDeOrden = [] #Se inicializa una lista para que se guarden los atributos en orden

	for i in canciones:
		cancion = i.split('<>')
		atributo = cancion[factor]
		if atributo not in listaDeOrden:
			listaDeOrden.append(atributo) #agrega el atributo de todas las canciones a una lista
	listaDeOrden.sort(key = str.lower) #ordena alfabeticamente los nombres pertenecientes a dicho atributo

	listaOrdenada = []
	for i in listaDeOrden:
		for j in canciones:
			cancion = j.split('<>')
			for atributo in cancion:
				if atributo == i:
					listaOrdenada.append(j) #crea una lista de canciones teniendo en cuenta el orden anterior

	listaOrdenada = ''.join(listaOrdenada)
	datos = open("Datos/"+lista+".txt","w") #guarda los datos pero ahora ordenados
	datos.write(listaOrdenada)
	datos.close()



def PHOTOS():
	def print_menu_photos(estado):#menús principales
		if estado == 'FOTOS':
			print("\n")
			print('{:30}{:30}\n{:30}{:30}\n{:30}'.format('[1]Ver Foto','[2] Agregar Foto','[3] Borrar Foto','[4]Ordenar','[5] Salir'))
		elif estado == 'Ordenar':
			print('{:37}{:37}\n{:37}{:37}\n{:37}'.format('[1] Nombre','[2] Autor','[3] Album','[4] Año','[5] Salir'))

	def add_photos():
		datos = open("Datos/Info_fotos.txt","r")
		pho = datos.read()
		datos.close()

		print('\n\nUsted eligio agregar una Foto a la lista de Fotos\n')
		bandera=True
		while (bandera):
			print("Elige una de las siguientes opciones:\n", "[T]omar foto\n", "[A]gregar informacion de una foto\n","[S]alir\n")
			opcion=input(">>")
			if (opcion == "t" or opcion == "T"):
				print("¿listo para la foto\n?","\nEn 3..\n")
				time.sleep(1)
				print("2...\n")
				time.sleep(1)
				print("1...\n")
				time.sleep(1)
				print("0... Ya\n")
				cap=cv2.VideoCapture(0)#activar camara
				leido,frames = cap.read()#asegurarse de que este activa
				cap.release()#desactivar camara
				system('cls')
				if (leido==True):
					time.sleep(1)
					path="Datos/Fotos"#carpeta de almacenamiento	
					nombre = input('- Ingrese el nombre de la foto que desea agregar:\n')
					cv2.imwrite(os.path.join(path, nombre+".jpg"),frames)#guardar la imagen con el nombre y en la carpeta
					autor = input('\n- Ingrese el autor de "{}":\n'.format(nombre))
					album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(nombre,autor))
					genero = "None"
					anio = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(nombre,autor))

					newpho = [nombre, autor, album, genero, anio,"\n"]#datos de la nueva foto
					newpho = '<>'.join(newpho)

					datos = open("Datos/Info_fotos.txt","w")
					datos.write(pho+newpho)
					datos.close()
					print("FOTO AGREGADA CON EXITO\n")
				else:
					Print("Error")
				ordenar_all('Nombre','Info_fotos')
				bandera=False

			elif (opcion == "a" or opcion == "A"):
				print('\n\nUsted eligio agregar información de una foto \nAsegurese de copiar la cancion que desea agregar en la carpeta "Nueva Foto"\n')
				nombre = input('- Ingrese el nombre de la foto que desea agregar:\n')
				autor = input('\n- Ingrese el autor de "{}":\n'.format(nombre))
				album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(nombre,autor))
				genero = "None"
				anio = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(nombre,autor))

				for archivo in scandir ('Nueva Foto'):
					rename(archivo,'Datos/Fotos'+nombre+'.jpg')#toma la nueva foto, la renombra y la dirige a la carpeta Datos/Fotos
				newinfo = [nombre, autor, album, genero, anio,"\n"]
				newinfo= '<>'.join(newinfo)

				datos = open("Datos/Info_fotos.txt","w")
				datos.write(pho+newinfo)#guarda la nueva información
				datos.close()
				print("INFORMACION AGREGADA CON EXITO\n")
				ordenar_all('Nombre','Info_fotos')
				bandera=False
			elif (opcion== "S" or opcion=="s"):
				bandera=False
			else:
				print("Opcion invalida, vuelva a ingresar\n")

	def print_all_photos(lista):
		encabezado = '\n\n{:^10}{:20}{:20}{:20}{:20}{:20}'.format('Num','Nombre','Autor','Album','Genero','Año')
		linea = '-'*95
		print(encabezado)
		print(linea+'\n')
		cont = 0

		for i in lista:
			cont += 1
			cancion = i.split('<>')
			tabla = '{:^10}{:20}{:20}{:20}{:20}{:20}{}'.format(cont,cancion[0],cancion[1],cancion[2],cancion[3],cancion[4],cancion[5])
			print(tabla)#muestra una lista de todas las fotos y sus atributos

	def all_photos():
		datos = open("Datos/Info_fotos.txt","r")
		info = datos.readlines()
		datos.close()
		print_all_photos(info)
            
	def print_Music(cadena):
		encabezado = '\n\n{:^10}{:20}{:20}{:20}{:20}{:20}'.format('Num','Nombre','Autor','Album','Genero','Año')
		linea = '-'*95
		print(encabezado)
		print(linea+'\n')
		cont = 0

		for i in cadena:
			cont += 1
			cancion = i.split('<>')
			tabla = '{:^10}{:20}{:20}{:20}{:20}{:20}{}'.format(cont,cancion[0],cancion[1],cancion[2],cancion[3],cancion[4],cancion[5])
			print(tabla)
			    
	def search_photos():
		datos = open("Datos/Info_fotos.txt","r")
		Se_photo= datos.readlines()
		datos.close()

		busqueda = str(input('\nIngrese el Nombre de la Cancion, una palabra o frase clave:\n'))
		resultadosBusqueda = []

		for i in Se_photo:
		    Ser_photo = i.split('<>')
		    for atributo in Ser_photo:
		        if (atributo == busqueda): #compara nuestra palabra clave con los datos disponibles y agrega las coincidencias a nuestra lista de resultados
		        	resultadosBusqueda.append(i)

		system('cls')
		if resultadosBusqueda == []:
		    print('\nNo se han encontrado resultados con "{}":'.format(busqueda))
		    time.sleep(3)
		    return
		print('\n\nLos resultados de la busqueda de "{}" son:'.format(busqueda))
		print_Music(resultadosBusqueda) #se imprime la lista de coincidencias si las hay

		seleccionar = True
		while seleccionar: #rectificar que la foto seleccionada este dentro del rango
		        desicion = int(input('Ingrese el numero de la foto que desea seleccionar:\n'))
		        if (desicion > 0) and (desicion <= len(resultadosBusqueda)):
		        	seleccionar = False
		        else:
		            print('No existe ese numero de foto')
		            continue

		resultado = resultadosBusqueda[desicion-1] 
		system('cls')
		return resultado

	def Show_photos(photo): #muestra la imagen que se seleccione
		datos = open("Datos/Info_fotos.txt","r")
		fotos = datos.readlines()
		datos.close()
		cont=0
		for i in fotos:
			if (i == photo):
				while(photo[cont]!="<"):
					cont+=1
				direccion_foto=i[:cont]
				nombre=direccion_foto[:]+".jpg"
				path="Datos/Fotos"#carpeta de almacenamiento
				img=cv2.imread(os.path.join(path, nombre),cv2.IMREAD_UNCHANGED)#leer imagen
				cv2.imshow("foto",img)#mostrar imagen en ventana externa
				key=cv2.waitKey(0) & 0xFF
				if (key==27):
					cv2.destroyAllWindows()#cerrar las ventanas externas

	def delet_photos(eliminar):
		datos = open("Datos/Info_fotos.txt","r")
		info= datos.readlines()
		datos.close()
		contador=0
		path="Datos/Fotos"#carpeta de almacenamiento
		for i in info:
			if (i == eliminar):
				info.remove(i)
				while(eliminar[contador]!="<"):
					contador+=1
				eliminar_foto=i[:contador]+".jpg"
				os.remove(os.path.join(path,eliminar_foto))# elimina la foto de el directorio Datos/Fotos

		info = ''.join(info)
		datos = open("Datos/Info_fotos.txt","w") # reescribe los datos exceptuando la foto eliminada
		datos.write(info)
		datos.close()

	menu_photos= 'FOTOS'
	menu_photos1="Ordenar"

	while (True):
		system('cls')
		all_photos()
		print_menu_photos(menu_photos)
		eleccion=input(">>")
		if (eleccion=="1"):
			system('cls')
			all_photos
			resultado=search_photos()
			if (resultado==None):
				continue
			Show_photos(resultado)
		elif (eleccion=="2"):
			system('cls')
			add_photos()
		elif (eleccion=="3"):
			system('cls')
			all_photos
			resultado=search_photos()
			if (resultado==None):
				continue
			delet_photos(resultado)
		elif (eleccion=="4"):
			while True:
			    all_photos()
			    print('Como desea ordenar su Musica')
			    print_menu_photos(menu_photos1)
			    parametro = int (input()) #da a elegir por cual atributo ordenar la música
			    if parametro == 1:
			    	ordenar_all('Nombre','Info_fotos')
			    elif parametro == 2:
			    	ordenar_all('Autor','Info_fotos')
			    elif parametro == 3:	
			    	ordenar_all('Album','Info_fotos')
			    elif parametro == 4:	
			    	ordenar_all('Año','Info_fotos')
			    elif parametro == 5:	
			    	break
			    else:
			    	print("Ese parametro no existe")
			    	time.sleep(1)
		elif (eleccion=="5"):
			print("Salio exitosamente\n")
			time.sleep(1)
			break
		else:
			print("Opcion invalida, intentelo otra vez")
			time.sleep(1)

def VIDEOS():

	def print_menu_videos(estado):
		if estado == 'VIDEOS':
			print("\n") #muestra al usuario todas las posibles opciones del menú
			print('{:30}{:30}{:30}{:30}'.format('[1] Agregar Video','[2] Borrar Video','[3] Ordenar','[4]Salir'))
		elif estado == 'Ordenar': 
		    print('{:37}{:37}\n{:37}{:37}\n{:37}'.format('[1] Nombre','[2] Autor','[3] Album','[4] Año','[5] Salir')) #da opcion de elegir el criterio a utilizar para ordenar los videos

	def add_Videos():
		datos = open("Datos/Info_videos.txt","r")
		videos = datos.read()
		datos.close()

		print('\n\nUsted eligio agregar un video a la lista de videos\n')
		flag=True
		while (flag):
			print("Elige una de las siguientes opciones:\n", "[C]apturar video\n", "[A]gregar informacion de un video\n","[S]alir\n")
			option=input(">>") 
			if (option == "c" or option == "C"):
				nombre = input('- Ingrese el nombre del video que desea agregar:\n')
				autor = input('\n- Ingrese el autor de "{}":\n'.format(nombre))
				album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(nombre,autor))
				genero = "None"
				anio = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(nombre,autor))

				newvid= [nombre, autor, album, genero, anio,"\n"]
				newvid = '<>'.join(newvid)

				datos = open("Datos/Info_videos.txt","w")
				datos.write(videos+newvid)
				datos.close()
				print("¿listo para el video?\n","En 3..\n")
				time.sleep(1) #congela el mensaje en pantalla determinado tiempo
				print("2...\n")
				time.sleep(1)
				print("1...\n")
				time.sleep(1)
				print("0... Ya\n")
				vid=cv2.VideoCapture(0) #activar camara
				frame_width=int(vid.get(3))
				frame_height= int(vid.get(4))
				path="Datos/Videos" #carpeta de almacenamiento	
				out = cv2.VideoWriter(os.path.join(path,nombre+".avi"),cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame_width,frame_height))
				while (True):
					ret,frame = vid.read() #asegurarse de que este activa
					
					if (ret == True):

						out.write(frame)

						cv2.imshow("Imagen",frame)

					exit=cv2.waitKey(1) & 0xFF
					if (exit==27):
						break
				else:
					break
				vid.release()
				out.release() #desactivar camara
				cv2.destroyAllWindows()
				system('cls')
				print("VIDEO GUARDADO CON EXITO\n")
				ordenar_all('Nombre','Info_videos')
				flag=False


			elif (option == "a" or option == "A"):
				print('\n\nUsted eligio agregar un video a la lista de canciones \nAsegurese de copiar el video que desea agregar en la carpeta "Nuevo Video"\n')
				nombre = input('- Ingrese el nombre del video que desea agregar:\n')
				autor = input('\n- Ingrese el autor de "{}":\n'.format(nombre))
				album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(nombre,autor))
				genero = "None"
				anio = input('\n- Ingrese el año captura de "{}" de "{}":\n'.format(nombre,autor))
				path="Datos/Videos"
				for archivo in scandir ('Nuevo Video'):
					rename(archivo,os.path.join(path, nombre+".avi"))
				newvid = [nombre, autor, album, genero, anio,"\n"]
				newvid= '<>'.join(newvid)

				datos = open("Datos/Info_videos.txt","w")
				datos.write(videos+newvid)
				datos.close()
				print("INFORMACION AGREGADA CON EXITO\n")
				ordenar_all('Nombre','Info_videos')
				flag=False
			elif (option== "S" or option=="s"):
				flag=False #sale del programa
			else:
				print("Opcion invalida, vuelva a ingresar\n")

	def print_all_Videos(lista):
		encabezado = '\n\n{:^10}{:20}{:20}{:20}{:20}{:20}'.format('Num','Nombre','Autor','Album','Genero','Año')
		linea = '-'*95
		print(encabezado)
		print(linea+'\n')
		cont = 0

		for i in lista:
			cont += 1
			cancion = i.split('<>')
			tabla = '{:^10}{:20}{:20}{:20}{:20}{:20}{}'.format(cont,cancion[0],cancion[1],cancion[2],cancion[3],cancion[4],cancion[5])
			print(tabla)

	def all_Videos():
		datos = open("Datos/Info_videos.txt","r")
		info = datos.readlines()
		datos.close()
		print_all_Videos(info) #imprime la informacion guardada de todos los videos

	def search_Videos():
		datos = open("Datos/Info_videos.txt","r")
		Se_video= datos.readlines()
		datos.close()

		busqueda = str(input('\nIngrese una palabra o frase clave:\n'))
		resultadosBusqueda = [] #buscara una cadenas que se asemeje a la  requerida

		for i in Se_video:
			Ser_video = i.split('<>')
			for atributo in Ser_video:
				if (atributo == busqueda):
					resultadosBusqueda.append(i)

		system('cls')
		if resultadosBusqueda == []:
		  print('\nNo se han encontrado resultados con "{}":'.format(busqueda))
		  time.sleep(3)
		  return
		print('\n\nLos resultados de la busqueda de "{}" son:'.format(busqueda))
		print_all_Videos(resultadosBusqueda)

		seleccionar = True
		while seleccionar:
		  desicion = int(input('Ingrese el numero del video que desea seleccionar:\n'))
		  if (desicion > 0) and (desicion <= len(resultadosBusqueda)):
		    seleccionar = False
		  else:
		    print('No existe ese numero de Video')
		    continue

		resultado = resultadosBusqueda[desicion-1] 
		system('cls')

		return resultado

	def delet_Video(eliminar):
		datos = open("Datos/Info_videos.txt","r")
		info= datos.readlines()
		datos.close()
		contador=0
		path="Datos/Videos"#carpeta de almacenamiento
		for i in info:
			if (i == eliminar):
				info.remove(i)
				while(eliminar[contador]!="<"):
					contador+=1
				eliminar_foto=i[:contador]+".avi"
				os.remove(os.path.join(path,eliminar_foto))

		info = ''.join(info)
		datos = open("Datos/Info_videos.txt","w")
		datos.write(info)
		datos.close()

	menu_Videos= 'VIDEOS'
	menu_Videos1= "Ordenar"

	while (True):
		system('cls')
		all_Videos()
		print_menu_videos(menu_Videos)
		eleccion=input(">>")
		if (eleccion=="1"):
			system('cls')
			add_Videos()
		elif (eleccion=="2"):
			system('cls')
			all_Videos()
			resultado=search_Videos()
			if (resultado==None):
				continue
			delet_Video(resultado)
		elif (eleccion==3):
			while True:
			    all_Videos()
			    print('Como desea ordenar sus videos')
			    print_menu_videos(menu_Videos1)
			    parametro = input()
			    if parametro == "1":
			    	ordenar_all('Nombre','Info_videos')
			    elif parametro == "2":
			    	ordenar_all('Autor','Info_videos')
			    elif parametro == "3":	
			    	ordenar_all('Album','Info_videos')
			    elif parametro == "4":	
			    	ordenar_all('Año','Info_videos')
			    elif parametro == "5":	
			    	break
			    else:
			    	print("Ese parametro no existe")
			    	time.sleep(1)
		elif (eleccion=="4"):
			print("Salio exitosamente\n")
			time.sleep(1)
			break
		else:
			print("Opcion invalida, intentelo otra vez")
			time.sleep(1)

def MUSIC():
	def print_Menu(estado):#GENERAL
		if estado == 'canciones':
			print('{:37}{:37}{:37}\n{:37}{:37}{:37}'.format('[1] Reproducir Cancion','[2] Agregar Cancion','[3] Borrar Cancion','[4] Listas de Reproduccion','[5] Ordenar','[6] Salir'))
		elif estado == 'listas de reproduccion':
			print('{:37}{:37}{:37}\n{:37}{:37}{:37}'.format('[1] Seleccionar Lista','[2] Agregar Lista','[3] Borrar Lista','[4] Modificar Lista','[5] Ordenar','[6] Salir'))
		elif estado == 'modificar lista':
			print('{:27}{:37}{:37}\n{:^90}'.format('[1] Renombrar Lista','[2] Agregar Cancion al la Lista','[3] Borrar Cancion de la Lista ','[6] Salir'))
		elif estado == 'ver lista':
			print('{:37}{:37}{:37}'.format('[1] Reproducir','[2] Ordenar','[6] Salir'))
		elif estado == 'reordenar':
			print('{:37}{:37}{:37}\n{:37}{:37}{:37}'.format('[1] Nombre','[2] Autor','[3] Album','[4] Genero','[5] Año','[6] Salir'))
		elif estado == 'reordenar listas':
			print('{:37}{:37}{:37}'.format('[1] Nombre','[2] Numero de Canciones','[6] Salir'))


	def print_Music(canciones):#GENERAL
		encabezado = '\n\n{:^10}{:20}{:20}{:20}{:20}{:20}'.format('Num','Nombre','Autor','Album','Genero','Año')
		linea = '-'*95
		print(encabezado)
		print(linea+'\n')
		cont = 0

		for i in canciones:
			cont += 1
			cancion = i.split('<>')
			tabla = '{:^10}{:20}{:20}{:20}{:20}{:20}{}'.format(cont,cancion[0],cancion[1],cancion[2],cancion[3],cancion[4],cancion[5])
			print(tabla) #muestra lista de todas las canciones seleccionadas y sus atributos

	def all_Music(): #muestra toda la musica
		datos = open("Datos/Info_canciones.txt","r")
		canciones = datos.readlines()
		datos.close()
		system('cls')
		print('{:^90}'.format('Toda la Musica'))
		print_Music(canciones)#GENERAL

	def add_Music():
		datos = open("Datos/Info_canciones.txt","r")
		canciones = datos.read()
		datos.close()

		system('cls')
		print('\n\nUsted eligio agregar una cancion a la lista de canciones \nAcegurese de copiar la cancion que desea agregar en la carpeta "Nueva Musica"\n')
		nombre = input('- Ingrese el nombre de la cancion que desea agregar:\n') #atributos de la nueva cancion
		autor = input('\n- Ingrese el autor de "{}":\n'.format(nombre))
		album = input('\n- Ingrese el album al que pertenece "{}" de "{}":\n'.format(nombre,autor))
		genero = input('\n- Ingrese el genero de "{}" de "{}":\n'.format(nombre,autor))
		año = input('\n- Ingrese el año de publicacion de "{}" de "{}":\n'.format(nombre,autor)) #el usuario ingresa todos los datos de la cancion

		archivos = []
		for archivo in scandir('Nueva Musica'):
			if (scandir('Nueva Musica') == 0):
				print('Acegurese de copiar la cancion que desea agregar en la carpeta "Nueva Musica"')
				time.sleep(3)
				return
			rename(archivo,'Datos/Musica/'+nombre+'.mp3')
		cancionNueva = [nombre, autor, album, genero, año,'\n']
		cancionNueva = '<>'.join(cancionNueva)

		datos = open("Datos/Info_canciones.txt","w")
		datos.write(canciones+cancionNueva)
		datos.close()

	def serch_Music(archivo):
		datos = open("Datos/"+archivo+".txt","r")
		canciones = datos.readlines()
		datos.close()

		busqueda = str(input('\nIngrese el Nombre de la Cancion, una palabra o frase clave:\n'))
		resultadosBusqueda = []

		for i in canciones:
			cancion = i.split('<>')
			for atributo in cancion:
				if (atributo == busqueda):
					resultadosBusqueda.append(i)

		system('cls')
		if resultadosBusqueda == []:
			print('\nNo se han encontrado resultados con "{}":'.format(busqueda))
			time.sleep(3)
			return
		print('\n\nLos resultados de la busqueda de "{}" son:'.format(busqueda))
		print_Music(resultadosBusqueda)

		seleccionar = True
		while seleccionar:
			desicion = int(input('Ingrese el numero de la cancion que desea seleccionar:\n'))
			if (desicion > 0) and (desicion <= len(resultadosBusqueda)):
				seleccionar = False
			else:
				print('No existe ese numero de cancion')
				continue

		resultado = resultadosBusqueda[desicion-1] 
		system('cls')

		return resultado#GENERAL

	def delet_Music(eliminar):
		datos = open("Datos/Info_canciones.txt","r")
		canciones = datos.readlines()
		datos.close()

		for i in canciones:
			if (i == eliminar):
				canciones.remove(i)
				cancion = i.split('<>')
				nombre = cancion[0]
				try:
					remove('Datos/Musica/'+nombre+'.mp3') #se eliminara la cancion del archivo, a menos que no la encuentre
				except FileNotFoundError: 
					print('')

		canciones = ''.join(canciones)
		datos = open("Datos/Info_canciones.txt","w")
		datos.write(canciones)
		datos.close()#GENERAL

	def play_Music(reproducir,lista):
		cancion = reproducir.split('<>')
		nombre = cancion[0]
		autor = cancion[1]
		album = cancion[2]
		file = 'Datos/Musica/'+nombre+'.mp3'
		pygame.init()
		pygame.display.set_mode((200,100))#inicializa una ventana
		pygame.mixer.music.load(file)#carga el archivo de musica
		pygame.mixer.music.play(0)#reproduce el archivo de musica

		play = True
		system('cls')
		while pygame.mixer.music.get_busy(): #mientras se este reproduciendo
			print('\n{:^30}-{:^30}-{:^30}\n'.format(nombre,autor,album))
			desicion = input("""\n[1] Anterior    [2] Play/Pause      [3] Siguiente
			
			[4] Regresar\n""")
			if desicion == '1':
				datos = open("Datos/"+lista+".txt","r")
				canciones = datos.readlines()
				datos.close()
				for i in canciones:
					if (i == reproducir):
						numero = canciones.index(i)
				numero -= 1 #le resta uno al indice para reproducir el la cancion con indice anterior
				if (numero < 0):
					numero = (len(canciones)) - 1
				pygame.mixer.music.stop() # detiene la reproduccion de la cancion actual
				reproducir = canciones[numero]
				cancion = reproducir.split('<>')
				nombre = cancion[0]
				autor = cancion[1]
				album = cancion[2]
				file = 'Datos/Musica/'+nombre+'.mp3'
				pygame.mixer.music.load(file)
				pygame.mixer.music.play(0) # reproduce la cancion con el nuevo indice
			elif desicion == '2':
				if play == True:
					play = False
					pygame.mixer.music.pause() #detiene la reproduccion temporalmente
				else:
					play = True
					pygame.mixer.music.unpause()
			elif desicion == '3':
				datos = open("Datos/"+lista+".txt","r")
				canciones = datos.readlines()
				datos.close()
				for i in canciones:
					if (i == reproducir):
						numero = canciones.index(i)
				numero += 1
				if (numero == len(canciones)):
					numero = 0
				pygame.mixer.music.stop() #detiene la reproduccion actual
				reproducir = canciones[numero]
				cancion = reproducir.split('<>')
				nombre = cancion[0]
				autor = cancion[1]
				album = cancion[2]
				file = 'Datos/Musica/'+nombre+'.mp3'
				pygame.mixer.music.load(file)
				pygame.mixer.music.play(0) #reproduce la cancion con el nuevo indice
			elif desicion == '4':
				pygame.mixer.music.stop()
				pygame.display.quit() #cierra la ventana de reproduccion
			else:
				print('Valor Erroneo')
			system('cls')

	def all_Listas():
		datos = open("Datos/Info_listas.txt","r")
		listas = datos.readlines()
		datos.close()
		system('cls')
		print('{:^90}'.format('Todas las Listas'))
		print_Listas(listas)
		
	def print_Listas(cadena):
		encabezado = '\n\n{:^10}{:50}{:20}'.format('Num','Nombre de la Lista de Reproduccion','Numero de canciones')
		linea = '-'*95
		print(encabezado)
		print(linea+'\n')
		cont = 0

		for i in cadena:
			cont += 1
			lista = i.split('<>')
			tabla = '{:^10}{:50}{:^20}{}'.format(cont,lista[0],lista[1],lista[2])
			print(tabla) #muestra las listas existentes y sus atributos 

	def add_Lista():
		datos = open("Datos/Info_listas.txt","r")
		listas = datos.read()
		datos.close()

		system('cls')
		print('\n\nUsted eligio agregar una lista de Reproduccion\n')
		titulo = input('- Ingrese el nombre de la lista de Reproduccion que desea agregar:\n')
		newList = open("Datos/"+titulo+".txt","w") # reescribe los datos con la nueva lista
		newList.close()

		agregar = True
		cant = 0
		while agregar: #agrega canciones continuamente hasta que el usuario determine lo contrario
			system('cls')
			all_Music()
			print('\nIngrese las canciones que desea agregar a la lista de Reproduccion "{}"'.format(titulo))
			newList = open("Datos/"+titulo+".txt","r")
			canciones = newList.read()
			newList.close()
			resultado = serch_Music('Info_canciones')
			if resultado != None:
				newList = open("Datos/"+titulo+".txt","w")
				newList.write(canciones+resultado)
				newList.close()
				cant += 1 #guarda el dato de numero de canciones en la lista
				print('\n\nCancion Agregada')
				time.sleep(3)
			else:
				if (cant == 0):
					continue
			seguir = True
			while seguir:
				system('cls')
				choise = input('¿Desea agregar otra Cancion?\n   [1] Si     [6] No\n')
				if (choise == '1'):
					seguir = False
				if (choise == '6'):
					seguir = False
					agregar = False

		listaNueva = [titulo, str(cant),'\n']
		listaNueva = '<>'.join(listaNueva)

		datos = open("Datos/Info_listas.txt","w")
		datos.write(listas+listaNueva)
		datos.close()

	def delet_Lista(eliminar):
		datos = open("Datos/Info_listas.txt","r")
		listas = datos.readlines()
		datos.close()

		for i in listas:
			if (i == eliminar):
				listas.remove(i)
				lista = i.split('<>')
				nombre = lista[0]
				remove('Datos/'+nombre+'.txt')

		listas = ''.join(listas)
		datos = open("Datos/Info_listas.txt","w")
		datos.write(listas) # reescribe los datos exceptuando la lista eliminada
		datos.close()

	def serch_Lista():
		datos = open("Datos/Info_listas.txt","r")
		listas = datos.readlines()
		datos.close()

		busqueda = str(input('\nIngrese el Nombre de la Lista de reproduccion, una palabra o frase clave:\n'))
		resultadosBusqueda = []

		for i in listas: # busca coincidencias entre las listas y la palabra clave
			lista = i.split('<>')
			for atributo in lista:
				if (atributo == busqueda):
					resultadosBusqueda.append(i)

		system('cls')
		if resultadosBusqueda == []:
			print('\nNo se han encontrado resultados con "{}":'.format(busqueda))
			time.sleep(3)
			return
		print('\n\nLos resultados de la busqueda de "{}" son:'.format(busqueda))
		print_Listas(resultadosBusqueda)

		seleccionar = True
		while seleccionar:
			desicion = int(input('Ingrese el numero de la cancion que desea seleccionar:\n'))
			if (desicion > 0) and (desicion <= len(resultadosBusqueda)): #se asegura que la cancion este dentro del rango
				seleccionar = False
			else:
				print('No existe ese numero de cancion')
				continue

		resultado = resultadosBusqueda[desicion-1] 
		system('cls')

		return resultado

	def edit_Lista(editada):
		lista = editada.split('<>')
		titulo = lista[0]
		cant = int(lista[1])
		modificarlista = True
		while modificarlista:
			datos = open("Datos/"+titulo+".txt","r")
			canciones = datos.readlines()
			datos.close()
			system('cls')
			print('{:^90}'.format(titulo))
			print_Music(canciones)
			menu4 = 'modificar lista'
			print_Menu(menu4)
			eleccion = input()
			if (eleccion == '1'):
				nuevoTitulo = input('Cual es el nuevo nombre de la lista?')
				rename('Datos/'+titulo+'.txt','Datos/'+nuevoTitulo+'.txt')
				datos = open("Datos/Info_listas.txt","r")
				listas = datos.readlines()
				datos.close()
				for i in listas:
					if (i == editada):
						listas.remove(i)
				lista = editada.split('<>')
				lista[0] = nuevoTitulo #cambia el primer atributo de la lista
				lista = '<>'.join(lista)
				listas = '<>'.join(listas)
				datos = open("Datos/Info_listas.txt","w")
				datos.write(listas+lista)
				datos.close()
				titulo = nuevoTitulo
			elif (eleccion == '2'):
				agregar = True
				while agregar:
					system('cls')
					all_Music()
					print('\nIngrese las canciones que desa agregar a la lista de Reproduccion "{}"'.format(titulo))
					datos = open("Datos/"+titulo+".txt","r")
					canciones = datos.read()
					datos.close()
					resultado = serch_Music('Info_canciones')
					if resultado != None:
						datos = open("Datos/"+titulo+".txt","w")
						datos.write(canciones+resultado) # reescribe los datos con la nueva cancion
						datos.close()
						cant += 1
						print('\n\nCancion Agregada')
						time.sleep(3)
					else:
						if (cant == 0):
							continue
					seguir = True
					while seguir: #sigue agregando canciones hasta que el usuario indique lo contrario
						system('cls')
						choise = input('Desea agregar otra Cancion?\n   [1] Si     [6] No\n')
						if (choise == '1'):
							seguir = False
						if (choise == '6'):
							seguir = False
							agregar = False
				datos = open("Datos/Info_listas.txt","r")
				listas = datos.readlines()
				datos.close()
				for i in listas:
					if (i == editada):
						listas.remove(i)
				lista = editada.split('<>')
				lista[1] = str(cant)
				lista = '<>'.join(lista)
				listas = '<>'.join(listas)
				datos = open("Datos/Info_listas.txt","w")
				datos.write(listas+lista) #agrega la lista ya editada a la carpeta
				datos.close()
				editada = lista
			elif (eleccion == '3'):
				if (cant == 1): # para que no quede una lista de reproduccion vacia
					print('No se puede eliminar la ultima cancion de la Lista')
					time.sleep(3)
					continue
				borrar = True
				while borrar:
					print('\nIngrese las canciones que desea eliminar de la lista de Reproduccion "{}"'.format(titulo))
					datos = open("Datos/"+titulo+".txt","r")
					canciones = datos.readlines()
					datos.close()
					resultado = serch_Music(titulo)
					if resultado != None:
						for i in canciones: #busca coincidencias entre el resultado y las canciones de la lista para luego eliminarla
							if (i == resultado):
								canciones.remove(i)
						canciones = ''.join(canciones)
						datos = open("Datos/"+titulo+".txt","w")
						datos.write(canciones) #reescribe los nuevos datos
						datos.close()
						cant -= 1
						print('\n\nCancion Eliminada')
						time.sleep(3)
						borrar = False
					else:
						break
				datos = open("Datos/Info_listas.txt","r")
				listas = datos.readlines()
				datos.close()
				for i in listas:
					if (i == editada):
						listas.remove(i)
				lista = editada.split('<>')
				lista[1] = str(cant)
				lista = '<>'.join(lista)
				listas = '<>'.join(listas)
				datos = open("Datos/Info_listas.txt","w")
				datos.write(listas+lista)
				datos.close()
				editada = lista
			elif (eleccion == '6'):
				modificarlista = False

	def play_Lista():
		lista = serch_Lista()
		if lista == None:
			return
		componentes = lista.split('<>')
		nombre = componentes[0]
		verlista = True
		while verlista:
			system('cls')
			datos = open("Datos/"+nombre+".txt","r")
			canciones = datos.readlines()
			datos.close()
			print('{:^90}'.format(nombre))
			print_Music(canciones)
			menu5 = 'ver lista'
			print_Menu(menu5)
			eleccion = input('')
			if (eleccion == '1'):
				resultado = serch_Music(nombre)
				if resultado == None:
					continue
				play_Music(resultado,nombre)
			elif (eleccion == '2'):
				reordenar = True
				while reordenar:
					system('cls')
					datos = open("Datos/"+nombre+".txt","r")
					canciones = datos.readlines()
					datos.close()
					print_Music(canciones)
					print('Como desea ordenar su Musica')
					print_Menu(menu3)
					parametro = input()
					if parametro == '1':
						ordenar('Nombre',nombre)
					elif parametro == '2':
						ordenar('Autor',nombre)
					elif parametro == '3':	
						ordenar('Album',nombre)
					elif parametro == '4':	
						ordenar('Genero',nombre)
					elif parametro == '5':	
						ordenar('Año',nombre)
					elif parametro == '6':	
						reordenar = False
			elif (eleccion == '6'):
				verlista = False

	def ordenar(factor,lista):
		datos = open("Datos/"+lista+".txt","r")
		canciones = datos.readlines()
		datos.close()

		if factor == 'Nombre':
			factor = 0
		elif factor == 'Autor':
			factor = 1
		elif factor == 'Album':
			factor = 2
		elif factor == 'Genero':
			factor = 3
		elif factor == 'Año':
			factor = 4
		elif factor == 'NombreLista':
			factor = 0
		elif factor == 'NumeroDeCanciones':
			factor = 1

		listaDeOrden = []

		for i in canciones:
			cancion = i.split('<>')
			atributo = cancion[factor]
			if atributo not in listaDeOrden:
				listaDeOrden.append(atributo)
		listaDeOrden.sort(key = str.lower) #ordena el atributo alfabeticamente

		listaOrdenada = []
		for i in listaDeOrden:
			for j in canciones:
				cancion = j.split('<>')
				for atributo in cancion:
					if atributo == i:
						listaOrdenada.append(j) #ordena las canciones segun el orden del atributo

		listaOrdenada = ''.join(listaOrdenada)
		datos = open("Datos/"+lista+".txt","w")
		datos.write(listaOrdenada)
		datos.close()#GENERAL





	abierto = True
	menu1 = 'canciones'
	menu2 = 'listas de reproduccion'
	menu3 = 'reordenar'
	menu4 = 'reordenar listas'
	while abierto:
		all_Music()
		print_Menu(menu1)
		eleccion = input()
		if (eleccion == '1'):
			resultado = serch_Music('Info_canciones')
			if resultado == None:
				continue
			play_Music(resultado,'Info_canciones')
		elif (eleccion == '2'):
			add_Music()
		elif (eleccion == '3'):
			resultado = serch_Music('Info_canciones')
			if resultado == None:
				continue
			delet_Music(resultado)
		elif (eleccion == '4'):
			verListas = True
			while verListas:
				all_Listas()
				print_Menu(menu2)
				eleccion = input()
				if (eleccion == '1'):
					play_Lista()
				elif (eleccion == '2'):
					add_Lista()
				elif (eleccion == '3'):
					resultado = serch_Lista()
					if resultado == None:
						continue
					delet_Lista(resultado)
				elif (eleccion == '4'):
					resultado = serch_Lista()
					if resultado == None:
						continue
					edit_Lista(resultado)
				elif (eleccion == '5'):
					reordenar = True
					while reordenar:
						all_Listas()
						print('¿Como desea ordenar sus Listas?')
						print_Menu(menu4)
						parametro = input()
						if parametro == '1':
							ordenar('NombreLista','Info_listas')
						elif parametro == '2':
							ordenar('NumeroDeCanciones','Info_listas')
						elif parametro == '6':	
							reordenar = False
				elif (eleccion == '6'):
					verListas = False
		elif (eleccion == '5'):
			reordenar = True
			while reordenar:
				all_Music()
				print('Como desea ordenar su Musica')
				print_Menu(menu3)
				parametro = input()
				if parametro == '1':
					ordenar('Nombre','Info_canciones')
				elif parametro == '2':
					ordenar('Autor','Info_canciones')
				elif parametro == '3':	
					ordenar('Album','Info_canciones')
				elif parametro == '4':	
					ordenar('Genero','Info_canciones')
				elif parametro == '5':	
					ordenar('Año','Info_canciones')
				elif parametro == '6':	
					reordenar = False
		elif (eleccion == '6'):
			abierto = False

def main():
	while(True):
		system('cls')
		print("BIENVENIDO A TU ORGANIZADOR MULTIMEDIA\n")
		print('{:30}{:30}\n{:30}{:30}'.format('[1] MUSICA','[2] FOTOS','[3] VIDEOS','[4]SALIR'))
		ver=input(">>")
		if (ver=="1"):
			MUSIC()
		elif (ver=="2"):
			PHOTOS()
		elif (ver=="3"):
			VIDEOS()
		elif (ver=="4"):
			print("Salio exitosamente\n")
			time.sleep(1)
			break
		else:
			print("Opcion invalida, intentelo otra vez")
			time.sleep(1)


main()

