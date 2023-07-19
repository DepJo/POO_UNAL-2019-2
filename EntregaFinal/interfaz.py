""" Reproductor de Contenido Multimedia """

"""
Integrantes:
        Juan Esteban Ochoa
        Delwin Jose Padilla
        Juan Camilo Reyes
        Leonardo Daniel Talledos 
"""

import cv2 #Librería que permite la captura de Fotos y Videos
#import pygame #Libreria utilizada para reproducir Audio
import os #Libreria utilizada para el control y administracion de archivos
from os import scandir, getcwd, rename, remove, system
import time #Libreria utilizada para el control del tiempo

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QLineEdit, QDialog, QStackedWidget
#from PyQt5.QtCore import Qt, QBuffer
from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QCameraInfo, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QCameraViewfinder, QVideoWidget

from PyQt5 import QtCore, QtGui, QtWidgets

class addmedia (QDialog): #Cuadro de dialogo para añadir multimedia
        def __init__(self):
                QDialog.__init__(self)
                uic.loadUi("aventana/add_media_dialog.ui", self)

                self.boton_agregar.clicked.connect(self.validar)

        def obtener_atributo (self,string,i):
                atributo = string[20*i:20*(i+1)]

                final = 20
                while True: #para quedarme solo con el atributo
                        if atributo[-1] == ' ':
                                final -= 1
                                atributo = atributo[:final]
                        else:
                                break
                return atributo
                
        def validar (self):
                
                #define que archivo abrir dependiendo la seccion del menu en que este
                if gui.seccion == 1:
                        self.info = 'Info_canciones'
                        self.carpeta_origen = 'Nueva Musica'
                        self.carpeta_destino = 'Musica'
                        self.extencion = '.mp3'
                if gui.seccion == 2:
                        self.info = 'Info_fotos'
                        self.carpeta_origen = 'Nueva Foto'
                        self.carpeta_destino = 'Fotos'
                        self.extencion = '.jpg'
                if gui.seccion == 3:
                        self.info = 'Info_videos'
                        self.carpeta_origen = 'Nuevo Video'
                        self.carpeta_destino = 'Videos'
                        self.extencion = '.avi'

                if gui.seccion == 11:
                        self.info = 'Info_listas'
                        self.carpeta_origen = ''
                        self.carpeta_destino = ''
                        self.extencion = ''

                if gui.seccion == 1 or gui.seccion == 2 or gui.seccion == 3:
                        self.nuevo_contenido = [self.lineEdit_nombre.text(),self.lineEdit_artista.text(),self.lineEdit_album.text(),self.lineEdit_genero.text(),self.lineEdit_ano.text(),'\n']
                        self.nuevo_contenido = '<>'.join(self.nuevo_contenido)
                
                        self.datos = open('Datos/' + self.info + '.txt','r')
                        self.canciones = self.datos.read()
                        self.datos.close()
                
                        self.datos = open('Datos/' + self.info + '.txt','w')
                        self.datos.write(self.canciones + self.nuevo_contenido)
                        self.datos.close()

                        #Busca la cancion en la carpeta, la renombra y la reubica


                        for self.__archivo in scandir(self.carpeta_origen):
                                rename(self.__archivo,'Datos/'+self.carpeta_destino+'/'+self.lineEdit_nombre.text()+self.extencion)

                if gui.seccion == 11:

                        num = 0
                        selected = []
                        for x in range(len(self.canciones.selectedItems())):
                                lista_atributos = []
                                
                                nombre = gui.obtener_atributo (self.canciones.selectedItems()[x].text(),0)
                                artista = gui.obtener_atributo (self.canciones.selectedItems()[x].text(),1)
                                album = gui.obtener_atributo (self.canciones.selectedItems()[x].text(),2)
                                genero = gui.obtener_atributo (self.canciones.selectedItems()[x].text(),3)
                                ano = gui.obtener_atributo (self.canciones.selectedItems()[x].text(),4)
                                selected.append(nombre + '<>' + artista + '<>' + album + '<>' + genero + '<>' + ano + '<>'+'\n')

                                num += 1

                                #self.canciones.setItemSelected(selectedItems()[x],False)
                                
                        
                        self.datos_r = open('Datos/Reproduccion/' + self.lineEdit_nombre.text() + '.txt','w')
                        for i in range(len(selected)):
                                self.datos_r.write(selected[i])
                        self.datos_r.close()

                        
                        nombre_l = str(self.lineEdit_nombre.text())
                        self.nuevo_contenido = [nombre_l,str(num)]
                        self.nuevo_contenido = '<>'.join(self.nuevo_contenido) +'<>'+ '\n'
                        
                        self.datos = open('Datos/' + self.info + '.txt','r')
                        self.cancions = self.datos.read()
                        self.datos.close()
                
                        self.datos = open('Datos/' + self.info + '.txt','w')
                        self.datos.write(self.cancions + self.nuevo_contenido)
                        self.datos.close()

                        self.canciones.clear()
                        
                self.lineEdit_nombre.selectAll()
                self.lineEdit_nombre.del_()
                self.lineEdit_artista.selectAll()
                self.lineEdit_artista.del_()
                self.lineEdit_album.selectAll()
                self.lineEdit_album.del_()
                self.lineEdit_genero.selectAll()
                self.lineEdit_genero.del_()
                self.lineEdit_ano.selectAll()
                self.lineEdit_ano.del_()

                gui.actualizar_lista()
                
                self.reject()#cierra el cudro de dialogo

class add_lista_r(QDialog):
        def __init__(self, lista):
                QDialog.__init__(self)
                uic.loadUi("aventana/agregar_a_lista_r.ui",self)

                #boton
                self.validar.clicked.connect(self.adicionar)

                indice = '{:20}{:20}{:20}{:20}{:20}'.format('Nombre'.ljust(18, ' '),'Artista'.ljust(18, ' '),'Album'.ljust(18, ' '),'Genero'.ljust(18, ' '),'Año'.ljust(18, ' '))
                self.not_lista_r.addItem(indice)
                for song in lista:
                        song = song.split('<>')
                        song_orden = '{:20}{:20}{:20}{:20}{:20}'.format(song[0].ljust(18, ' '),song[1].ljust(18, ' '),song[2].ljust(18, ' '),song[3].ljust(18, ' '),song[4].ljust(18, ' '))
                        self.not_lista_r.addItem(song_orden)

        def adicionar(self):
                num = 0
                selected = []
                for x in range(len(self.not_lista_r.selectedItems())):
                        song = self.not_lista_r.selectedItems()[x].text()
                        nombre = gui.obtener_atributo (song,0)
                        artista = gui.obtener_atributo (song,1)
                        album = gui.obtener_atributo (song,2)
                        genero = gui.obtener_atributo (song,3)
                        ano = gui.obtener_atributo (song,4)
                        selected.append(nombre + '<>' + artista + '<>' + album + '<>' + genero + '<>' + ano + '<>'+'\n')

                        num += 1

                old_archivo = open('Datos/Reproduccion/'+gui.archivo_lista+'.txt','r')
                old_datos = old_archivo.readlines()
                old_archivo.close()

                new_datos = old_datos + selected
                new_datos = ''.join(new_datos)
                print(new_datos)
                new_archivo = open('Datos/Reproduccion/'+gui.archivo_lista+'.txt','w')
                new_archivo.write(new_datos)
                new_archivo.close()
                
                new_num = str(int(gui.num_songs)+num)
                lista_de_r = gui.archivo_lista
                num_canciones = gui.num_songs
                #Abre el archivo con la base de datos
                datos = open("Datos/Info_listas.txt","r")
                elementos = datos.readlines()
                datos.close()

                #Compara los elementos con informacion a eliminar
                
                for i in elementos:
                        print(i)
                        if (i == lista_de_r+'<>'+num_canciones+'<>'+'\n'):
                                elementos.remove(i)
                  
                
                elementos.append(lista_de_r+'<>'+new_num+'<>'+'\n')
                elementos = ''.join(elementos)
                print(elementos)
                
                datos = open("Datos/Info_listas.txt","w")
                datos.write(elementos)
                datos.close()

                self.reject()#cierra el cudro de dialogo
                
class FOTO(QDialog): #es para tomar la foto, no para visualizarla
        def __init__(self):
                QDialog.__init__(self)
                uic.loadUi("aventana/camara.ui",self)
                
                #Esto es para mostrar la camara en el QDialog
                self.viewfinder = QCameraViewfinder() 
                self.stack.addWidget(self.viewfinder)
                self.viewfinder.show()
                self.camera = QCamera()
                self.camera.setViewfinder(self.viewfinder)
                self.imageCapture = QCameraImageCapture(self.camera)
                self.camera.start()

                #botones
                self.tomar.clicked.connect(self.capturar)
                self.salvar.clicked.connect(self.guardar)
                self.descartar.clicked.connect(self.no_usar)

        def capturar (self):
                if gui.seccion == 2:
                        self.salvar.setEnabled(True)
                        self.descartar.setEnabled(True)
                        self.tomar.setEnabled(False)
                
                        self.camera.stop() # desactivo la camara, sino no toma la foto
                
                        #Usar la Camara para tomar la Foto
                        self.__cap = cv2.VideoCapture(0) #Activar camara
                        self.__leido,self.__frames = self.__cap.read() #Asegurarse de que este activa
                        self.__cap.release() #Desactivar camara
                        if self.__leido == True:
                                #Busca la Foto la renombra y la reubica
                                self.__path="Nueva Foto/" #Carpeta de almacenamiento
                                cv2.imwrite("Nueva Foto/nueva.jpg",self.__frames)

                        self.camera.start()

                if gui.seccion == 3:
                        self.salvar.setEnabled(True)
                        self.descartar.setEnabled(True)
                        self.tomar.setEnabled(False)

                        self.camera.stop()

                        self.__vid=cv2.VideoCapture(0) #Activar camara
                        self.__frame_width=int(self.__vid.get(3))
                        self.__frame_height= int(self.__vid.get(4))

                        #Busca el Video lo renombra y lo reubica
                        self.__path="Nuevo Video/" #Carpeta de almacenamiento   
                        self.__out = cv2.VideoWriter(os.path.join(self.__path,"nuevo"+".avi"),cv2.VideoWriter_fourcc('M','J','P','G'), 15, (self.__frame_width,self.__frame_height))
                                        
                        #Ciclo para grabar el Video
                        while (True):
                                self.__ret,self.__frame = self.__vid.read() #Asegurarse de que este activa
                                                        
                                if (self.__ret == True):

                                        self.__out.write(self.__frame)

                                        cv2.imshow("Imagen",self.__frame)

                                self.__exit=cv2.waitKey(1) & 0xFF
                                if (self.__exit==27):
                                        break
                        #Finalizar proceso de Grabado
                        self.__vid.release()
                        self.__out.release() #Desactivar camara
                        cv2.destroyAllWindows()

                        self.camera.start()

        def guardar (self):
                self.salvar.setEnabled(False)
                self.descartar.setEnabled(False)
                self.tomar.setEnabled(True)
                
                gui.cuadro_anadir.exec_()

        def no_usar(self):
                self.salvar.setEnabled(False)
                self.descartar.setEnabled(False)
                self.tomar.setEnabled(True)
                
                os.remove("Nueva Foto/nueva.jpg")

class visor_de_foto(QDialog):
        def __init__(self,ver):
                QDialog.__init__(self)
                uic.loadUi("aventana/ver_la_foto.ui",self)
                self.ver = ver

                self.foto.setPixmap(QtGui.QPixmap("{}/Datos/Fotos/{}.jpg".format(getcwd(),self.ver)))

class ventana(QMainWindow): #Principal
        def __init__(self):
                QMainWindow.__init__(self)
                uic.loadUi("aventana/principal.ui", self)

                self.cuadro_anadir = addmedia() #crea el objeto del cuadro de dialogo para añadir contenido
                self.cuadro_anadir.canciones.hide()
                self.activar_camara = FOTO()


                #self.pr = QPushButton(self)
                #self.pr.setText("Abrr")
                #self.pr.clicked.connect(self.prueba)
  
                #oculta todos los menus
                self.menu_musica.hide()
                self.menu_video.hide()
                self.menu_foto.hide()
                
                self.previsualizador.hide()
                self.seccion = None
                self.fotito.hide()
                
                self.agregar_l.hide()
                self.renombrar_l.hide()
                self.edit_name.hide()

                self.agregar_cl.hide()
                self.eliminar_cl.hide()

                self.aviso.hide()
                
                #botones del menú principal
                self.musica.clicked.connect(self.desplegar_menu_musica)
                self.videos.clicked.connect(self.desplegar_menu_video)
                self.galeria.clicked.connect(self.desplegar_menu_foto)
                
                #botones que inicializan el cuadro "addmedia"
                self.agregar_f.clicked.connect(self.add_media)
                self.agregar_c.clicked.connect(self.add_media)
                self.agregar_v.clicked.connect(self.add_media)
                self.agregar_l.clicked.connect(self.add_media)

                #boton para borrar multimedia
                self.borrar.clicked.connect(self.delete_media)

                #boton para ordenar
                self.ordenar.clicked.connect(self.ordenar_media)

                #listas de reproduccion
                #eventos que despligan menus
                self.listasdereproduccion.clicked.connect(self.desplegar_menu_listas)
                self.lista.itemDoubleClicked.connect(self.desplegar_menu_de_la_lista)
                #botones
                self.renombrar_l.clicked.connect(self.desplegar_renombrar)
                self.ok_renombrar.clicked.connect(self.renombrar_lista_r)

                self.agregar_cl.clicked.connect(self.agregar_cancion_alista)
                self.eliminar_cl.clicked.connect(self.eliminar_cancion_delista)
                
                #fotos
                #boton para abrir camara
                self.tomar_f.clicked.connect(self.activarcamara)
                #evento para activar y desactivar la previsualizacion
                self.previsualizador.pressed.connect(self.previsualizacion_de_foto) #mientras lo mantiene oprimido
                self.previsualizador.released.connect(self.desprevisualizacion_de_foto)#cuando lo suelta
                #boton para "abrir" la imagen
                self.ver_f.clicked.connect(self.visualizar_foto)

                #videos
                self.tomar_v.clicked.connect(self.grabar_video)
                self.ver_v.clicked.connect(self.visualizar_video)


        def prueba(self):
                print(self.lista.currentItem())

        def desplegar_renombrar(self):
                if self.lista.currentItem() == None:
                        self.aviso.show()
                        return
                self.aviso.hide()
                
                self.edit_name.show()

                self.agregar_l.setEnabled(False)
                self.listasdereproduccion.setEnabled(False)
                self.galeria.setEnabled(False)
                self.videos.setEnabled(False)
                self.musica.setEnabled(False)

        def renombrar_lista_r(self):
                self.edit_name.hide()

                self.agregar_l.setEnabled(True)
                self.listasdereproduccion.setEnabled(True)
                self.galeria.setEnabled(True)
                self.videos.setEnabled(True)
                self.musica.setEnabled(True)
                
                item = self.lista.currentItem()
                lista_de_r = self.obtener_atributo(item.text(),0)
                num_canciones = self.obtener_atributo(item.text(),1)
                #Abre el archivo con la base de datos
                datos = open("Datos/Info_listas.txt","r")
                elementos = datos.readlines()
                datos.close()

                #Compara los elementos con informacion a eliminar
                
                for i in elementos:
                        if (i == lista_de_r+'<>'+num_canciones+'<>'+'\n'):
                                elementos.remove(i)
                  
                
                elementos.append(self.new_name.text()+'<>'+num_canciones+'<>'+'\n')
                elementos = ''.join(elementos)
                
                datos = open("Datos/Info_listas.txt","w")
                datos.write(elementos)
                datos.close()
                
                rename("Datos/Reproduccion/"+lista_de_r+".txt","Datos/Reproduccion/"+self.new_name.text()+".txt")
                self.new_name.selectAll()
                self.new_name.del_()

                self.vaciar_lista()
                lr_datos = open('Datos/Info_listas.txt','r')
                lr_canciones = lr_datos.readlines()
                lr_datos.close()
                self.mostrar_lista(lr_canciones)


        def agregar_cancion_alista(self):
                lr_datos = open('Datos/Reproduccion/'+self.archivo_lista+'.txt','r')
                lr_canciones = lr_datos.readlines()
                lr_datos.close()
                
                t_datos = open('Datos/Info_canciones.txt','r')
                t_canciones = t_datos.readlines()
                t_datos.close()
                
                not_lr = []
                for todas in t_canciones:
                        if todas in lr_canciones:
                                pass
                        else:
                                not_lr.append(todas)
        
                self.adicionar = add_lista_r(not_lr)
                self.adicionar.exec_()

                self.vaciar_lista()
                lr_datos = open('Datos/Reproduccion/'+self.archivo_lista+'.txt','r')
                lr_canciones = lr_datos.readlines()
                lr_datos.close()
                self.mostrar_lista(lr_canciones)

        def eliminar_cancion_delista(self):
                if self.lista.currentItem() == None:
                        self.aviso.show()
                        return
                self.aviso.hide()
                
                eliminar = self.lista.currentItem().text()
                nombre = gui.obtener_atributo (eliminar,0)
                artista = gui.obtener_atributo (eliminar,1)
                album = gui.obtener_atributo (eliminar,2)
                genero = gui.obtener_atributo (eliminar,3)
                ano = gui.obtener_atributo (eliminar,4)
                eliminar = nombre + '<>' + artista + '<>' + album + '<>' + genero + '<>' + ano + '<>'+'\n'

                datos = open("Datos/Reproduccion/"+self.archivo_lista+".txt","r")
                elementos = datos.readlines()
                
                datos.close()
                #Compara los elementos con informacion a eliminar
                for i in elementos:
                        
                        if i == eliminar:
                                elementos.remove(i)
                                
                elementos = ''.join(elementos)
                print(elementos)
                datos = open("Datos/Reproduccion/"+self.archivo_lista+".txt","w")
                datos.write(elementos)
                datos.close()

                datos = open("Datos/Info_listas.txt","r")
                elementos = datos.readlines()
                datos.close()
                old = self.archivo_lista + '<>' + self.num_songs  + '<>'+'\n'
                for i in elementos:
                        if i == old:
                                elementos.remove(i)
                elementos.append(self.archivo_lista + '<>' + str(int(self.num_songs) - 1)  + '<>'+'\n')
                elementos = ''.join(elementos)
                
                datos = open("Datos/Info_listas.txt","w")
                datos.write(elementos)
                datos.close()

                self.vaciar_lista()
                lr_datos = open('Datos/Reproduccion/'+self.archivo_lista+'.txt','r')
                lr_canciones = lr_datos.readlines()
                lr_datos.close()
                self.mostrar_lista(lr_canciones)
        def activarcamara(self):
                self.activar_camara.exec_()

        def previsualizacion_de_foto(self):
                if self.lista.currentItem() == None:
                        self.aviso.show()
                        return
                self.aviso.hide()
                
                if self.seccion == 2:
                        item = self.lista.currentItem()
                        self.nombreFoto = self.obtener_atributo(item.text(),0)
                        
                        self.fotito.setPixmap(QtGui.QPixmap("{}/Datos/Fotos/{}.jpg".format(getcwd(),self.nombreFoto)))
                        
        def desprevisualizacion_de_foto(self):
                self.fotito.setPixmap(QtGui.QPixmap(None))

        def visualizar_foto(self):
                if self.lista.currentItem() == None:
                        self.aviso.show()
                        return
                self.aviso.hide()
                
                item = self.lista.selectedItems()
                #Array para guardar los items seleccionados (se que es un bucle inecesario pero no me funciono de otra manera :V )
                selected = []
                for x in range(len(item)):
                        selected.append(item[x].text())
                self.nombreFoto = None              
                self.nombreFoto = selected[0][:20]
                final = 20
                while True: #para quedarme solo con el nombre
                        if self.nombreFoto[-1] == ' ':
                                final -= 1
                                self.nombreFoto = self.nombreFoto[:final]
                        else:
                                break
                
                self.visor_foto = visor_de_foto(self.nombreFoto)
                self.visor_foto.exec_()

        def grabar_video(self):
                
                self.activar_camara.exec_()

        def visualizar_video(self):
                if self.lista.currentItem() == None:
                        self.aviso.show()
                        return
                self.aviso.hide()

                item = self.lista.currentItem()
                nombre = self.obtener_atributo (item.text(),0)

                captura = cv2.VideoCapture('Datos/Videos/'+nombre+'.avi')
                while (captura.isOpened()):
                
                        ret, imagen = captura.read()
                        if ret == True:
                                cv2.imshow('video', imagen)
                        if cv2.waitKey(30) == ord('s'):
                                break
                        
                captura.release()
                cv2.destroyAllWindows()
                
        def obtener_atributo (self,string,i):
                atributo = string[20*i:20*(i+1)]

                final = 20
                while final != 0: #para quedarme solo con el atributo
                        if atributo[-1] == ' ':
                                final -= 1
                                atributo = atributo[:final+1]
                        else:
                                break
                if atributo != ' ':
                        return atributo
                else:
                        return ''
        def mostrar_lista(self,lista):
                if self.seccion == 11:
                        indice = '{:20}{:20}'.format('Nombre'.ljust(18, ' '),'N° Canciones'.ljust(18, ' '))
                        self.lista.addItem(indice)
                        
                        for song in lista:
                                song = song.split('<>')
                                song_orden = '{:20}{:20}'.format(song[0].ljust(18, ' '),song[1].ljust(18, ' '))
                                self.lista.addItem(song_orden)
                                
                if self.seccion == 1 or self.seccion == 2 or self.seccion == 3 or self.seccion == 12:
                        indice = '{:20}{:20}{:20}{:20}{:20}'.format('Nombre'.ljust(18, ' '),'Artista'.ljust(18, ' '),'Album'.ljust(18, ' '),'Genero'.ljust(18, ' '),'Año'.ljust(18, ' '))
                        self.lista.addItem(indice)
                        for song in lista:
                                song = song.split('<>')
                                song_orden = '{:20}{:20}{:20}{:20}{:20}'.format(song[0].ljust(18, ' '),song[1].ljust(18, ' '),song[2].ljust(18, ' '),song[3].ljust(18, ' '),song[4].ljust(18, ' '))
                                self.lista.addItem(song_orden)

        def vaciar_lista(self):#borra todos los items del QlistWidget llamado lista
                num_items = self.lista.count() #numero de items
                while num_items != 0:
                        self.lista.takeItem(0)
                        num_items -= 1
        
        def desplegar_menu_musica(self):
                self.aviso.hide()
                self.seccion = 1

                self.vaciar_lista()

                #mostrar solo el menu de musica
                self.menu_musica.show()
                self.menu_video.hide()
                self.menu_foto.hide()

                self.previsualizador.hide()
                self.fotito.hide()

                self.agregar_l.hide()
                self.renombrar_l.hide()
                self.agregar_c.setEnabled(True)
                self.reproducir_c.setEnabled(True)

                self.agregar_cl.hide()
                self.eliminar_cl.hide()

                self.orden_al.show()
                self.orden_g.show()
                self.orden_an.show()
                self.orden_ar.setText('Artista')

                self.borrar.setEnabled(True)
                #mostrar lista de canciones
                canciones = open('Datos/Info_canciones.txt','r')
                lista = canciones.readlines()
                canciones.close()
                self.mostrar_lista(lista)

        def desplegar_menu_video(self):
                self.aviso.hide()
                self.seccion = 3

                self.vaciar_lista()

                #mostrar solo el menu de videos
                self.menu_musica.hide()
                self.menu_video.show()
                self.menu_foto.hide()

                self.previsualizador.hide()
                self.fotito.hide()

                self.agregar_l.hide()
                self.renombrar_l.hide()

                self.agregar_cl.hide()
                self.eliminar_cl.hide()

                self.orden_al.show()
                self.orden_g.show()
                self.orden_an.show()
                self.orden_ar.setText('Artista')

                self.borrar.setEnabled(True)
                #mostrar lista de video
                videos = open('Datos/Info_videos.txt','r')
                lista = videos.readlines()
                videos.close()
                self.mostrar_lista(lista)

        def desplegar_menu_foto(self):
                self.aviso.hide()
                self.seccion = 2

                self.vaciar_lista()

                #mostrar solo el menu de fotos
                self.menu_musica.hide()
                self.menu_video.hide()
                self.menu_foto.show()

                self.previsualizador.show()
                self.fotito.show()

                self.agregar_l.hide()
                self.renombrar_l.hide()

                self.agregar_cl.hide()
                self.eliminar_cl.hide()

                self.orden_al.show()
                self.orden_g.show()
                self.orden_an.show()
                self.orden_ar.setText('Artista')

                self.borrar.setEnabled(True)
                #mostrar lista de fotos
                fotos = open('Datos/Info_fotos.txt','r')
                lista = fotos.readlines()
                fotos.close()
                self.mostrar_lista(lista)

        def desplegar_menu_listas(self):
                self.aviso.hide()
                self.seccion = 11
                
                self.vaciar_lista()
                
                #mostrar menu listas
                self.agregar_l.show()
                self.renombrar_l.show()
                self.agregar_c.setEnabled(False)
                self.reproducir_c.setEnabled(False)
                self.borrar.setEnabled(True)

                self.agregar_cl.hide()
                self.eliminar_cl.hide()

                self.orden_al.hide()
                self.orden_g.hide()
                self.orden_an.hide()
                self.orden_ar.setText('N° Canciones')
                
                #mostrar lista de listas de r
                listas_r = open('Datos/Info_listas.txt','r')
                lista = listas_r.readlines()
                listas_r.close()
                self.mostrar_lista(lista)

        def desplegar_menu_de_la_lista(self):
                self.aviso.hide()
                if self.seccion == 11:
                        self.seccion = 12
                        #mostrar la lista de reproduccion
                        self.archivo_lista = self.obtener_atributo(self.lista.currentItem().text(),0)
                        self.num_songs = self.obtener_atributo(self.lista.currentItem().text(),1)
                        
                        listas_r = open('Datos/Reproduccion/'+self.archivo_lista+'.txt','r')
                        lista = listas_r.readlines()
                        listas_r.close()
                        self.vaciar_lista()
                        self.mostrar_lista(lista)

                        #mostrar menu
                        self.agregar_l.hide()
                        self.renombrar_l.hide()
                        self.reproducir_c.setEnabled(True)
                        self.borrar.setEnabled(False)
                
                        self.agregar_cl.show()
                        self.eliminar_cl.show()

                        self.orden_al.show()
                        self.orden_g.show()
                        self.orden_an.show()
                        self.orden_ar.setText('Artista')
                else:
                        return
                
        def add_media(self):
                if self.seccion == 11:
                        self.cuadro_anadir.canciones.show()

                        #mostrar lista de canciones
                        canciones = open('Datos/Info_canciones.txt','r')
                        lista = canciones.readlines()
                        canciones.close()
                        indice = '{:20}{:20}{:20}{:20}{:20}'.format('Nombre'.ljust(18, ' '),'Artista'.ljust(18, ' '),'Album'.ljust(18, ' '),'Genero'.ljust(18, ' '),'Año'.ljust(18, ' '))
                        self.cuadro_anadir.canciones.addItem(indice)
                        for song in lista:
                                song = song.split('<>')
                                song_orden = '{:20}{:20}{:20}{:20}{:20}'.format(song[0].ljust(18, ' '),song[1].ljust(18, ' '),song[2].ljust(18, ' '),song[3].ljust(18, ' '),song[4].ljust(18, ' '))
                                self.cuadro_anadir.canciones.addItem(song_orden)
                                
                self.cuadro_anadir.exec_()

        def actualizar_lista(self):
                if self.seccion == 1:
                        actual_file = 'Info_canciones'
                if self.seccion == 2:
                        actual_file = 'Info_fotos'
                if self.seccion == 3:
                        actual_file = 'Info_videos'
                if self.seccion == 11:
                        actual_file = 'Info_listas'

                self.vaciar_lista()
                datos = open('Datos/'+actual_file+'.txt','r')
                items = datos.readlines()
                datos.close()
                print(items)
                self.mostrar_lista(items)
                
        def delete_media (self):
                if self.lista.currentItem() == None:
                        self.aviso.show()
                        return
                self.aviso.hide()
                
                borrar = self.lista.currentItem().text()
                if self.seccion == 1 or self.seccion == 2 or self.seccion == 3:
                        nombre = self.obtener_atributo(borrar,0)
                        artista = self.obtener_atributo(borrar,1)
                        album = self.obtener_atributo(borrar,2)
                        genero = self.obtener_atributo(borrar,3)
                        ano = self.obtener_atributo(borrar,4)
                        
                        todo =[nombre,artista,album,genero,ano]
                        
                if self.seccion == 11:
                        nombre_l = self.obtener_atributo(borrar,0)
                        num_c = self.obtener_atributo(borrar,1)

                        todo = [nombre_l,num_c]

                borrar = '<>'.join(todo)+'<>'
                              
                #copie y pegue esto de mexico
                #Dependiendo del valor de la seccion del objeto se usara una lista, una carpeta de ubicacion y una extencion para el archivo
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
                elif (self.seccion == 11): # ----- Videos -----
                        self.__lista = "Datos/Info_listas.txt"
                        self.__carpeta = 'Datos/Reproduccion/'
                        self.__extension = '.txt'

                #Abre el archivo con la base de datos
                self.__datos = open(self.__lista,"r")
                self.__elementos = self.__datos.readlines()
                self.__datos.close()
                #Compara los elementos con informacion a eliminar
                for self.__i in self.__elementos:
                        if (self.__i == borrar+'\n'):
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

                self.index = self.lista.currentRow()
                self.lista.takeItem(self.index)

        def ordenar_media (self):
                if (self.seccion == 11):# ----- Listas De Reproduccion -----
                        self.__lista = "Info_listas"
                if (self.seccion == 1): # ----- Canciones -----
                        self.__lista = "Info_canciones"
                if (self.seccion == 2): # ----- Fotos -----
                        self.__lista = "Info_fotos"
                if (self.seccion == 3): # ----- Videos -----
                        self.__lista = "Info_videos"
                if (self.seccion == 12):# ----- Lista De Reproduccion -----
                        self.__lista = self.archivo_lista

                #Abre el archivo con la base de datos
                self.__datos = open("Datos/"+self.__lista+".txt","r")
                self.__elementos = self.__datos.readlines()
                self.__datos.close()

                #Redefine el valor de factor asignandole un valor numerico
                if self.orden_n.isChecked():
                        self.__factor = 0
                if self.orden_ar.isChecked():
                        self.__factor = 1
                if self.orden_al.isChecked():
                        self.__factor = 2
                if self.orden_g.isChecked():
                        self.__factor = 3
                if self.orden_an.isChecked():
                        self.__factor = 4

                self.vaciar_lista()

                #Guarda el atributo de elemento segun el factor dado
                self.__listaDeOrden = [] #Lista de los atributos
                for self.__i in self.__elementos:
                        self.__media = self.__i.split('<>')
                        self.__atributo = self.__media[self.__factor]
                        if self.__atributo not in self.__listaDeOrden:
                                self.__listaDeOrden.append(self.__atributo) #Agrega el atributo a lalista
                self.__listaDeOrden.sort(key = str.lower) #Ordena alfabeticamente los atributos sin tomar en cuenta las mayusculas
                print(self.__listaDeOrden)
                #Agrega la informacion de la cancion con el orden de los atributos anteriores
                self.__listaOrdenada = [] #Lista de los elementos ordenados
                for self.__i in self.__listaDeOrden:
                        for self.__j in self.__elementos:
                                self.__media = self.__j.split('<>')
                                for self.__atributo in self.__media:
                                        if self.__atributo == self.__i:
                                                self.__listaOrdenada.append(self.__j) #Agrega un elemento a la lista conforme el orden establecido
                self.mostrar_lista(self.__listaOrdenada)


if __name__ == "__main__":
        aplicacion = QApplication(sys.argv)#inicializa la aplicacion
        gui = ventana()#creo el objeto "gui"
        gui.show()#muestra la ventana
        sys.exit(aplicacion.exec_())#ejecuta la aplicacion
