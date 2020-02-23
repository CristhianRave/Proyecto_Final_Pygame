import pygame as pg
from pygame.locals import *
import sqlite3
import sys

VERDE = (30, 186, 22)
WHITE = (255, 255, 255)
NEGRO = (0, 0, 0)
RED = (255, 0, 0)


class Ranking():

    def __init__(self):

        pg.font.init()

        self.screen = pg.display.set_mode((800,600))
        self.background_image = pg.image.load('resources/images/fondo8.jpg').convert()
        pg.display.set_caption('The Quest')
        self.screen.blit(self.background_image, (0, 0))

        self.tamaño_titulo = pg.font.Font('resources/fonts/PressStart.ttf', 28)
        self.tamaño_titulo1 = pg.font.Font('resources/fonts/PressStart.ttf', 18)
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 32)

        self.query = "SELECT usuario, puntuacion FROM registros order by puntuacion desc"
        self.query1 = "CREATE TABLE IF NOT EXISTS `registros` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `usuario` TEXT NOT NULL, `puntuacion` INTEGER NOT NULL)"
        self.query2 = "INSERT INTO registros (usuario, puntuacion) VALUES(?,?)"
        self.query3 = "DELETE FROM registros WHERE id IN (SELECT id FROM registros ORDER BY puntuacion ASC LIMIT 1)"
        self.conn = sqlite3.connect('ranking.db')
        self.cursor = self.conn.cursor()
        self.lista_ranking = []

    def mostrar_datos_ranking(self):

        datos = self.lista_ranking
        self.linea_texto = self.font.render(' NickName  Puntuacion', True, RED)
        self.screen.blit(self.linea_texto, (60, 100))

        for i,n in enumerate(datos):      
              
            self.linea_texto1 = self.tamaño_titulo.render(f'{datos[i][1].upper()}', True, WHITE)   
            self.linea_texto2 = self.tamaño_titulo.render(f'{datos[i][2]}', True, WHITE)
            self.screen.blit(self.linea_texto1, [230, 230 + (42) * i])
            self.screen.blit(self.linea_texto2, [450, 230 + (42) * i])

        self.text_espacio()
        pg.display.flip()
        self.main_loop_ranking()

    def main_loop_ranking(self):
        
        bucle_ranking = True
        while bucle_ranking:
            for evento in pg.event.get():  
                if evento.type == pg.QUIT:
                    pg.quit()
                    sys.exit(0)
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    bucle_ranking = False

    def create_table(self, cursor):
        self.cursor.execute(self.query1)

    def insertar_puntuacion(self, cursor, conn, puntos, name):
        try:
            self.cursor.execute(self.query2, (name, puntos))
            conn.commit()
        except sqlite3.Error as e:
            print('Error en acceso a base de datos: {}'.format(e))
 

    def posicion_usuarios(self, cursor, conexion, puntos):
        entrada_texto = Entrada_texto()
        self.create_table(self.cursor)

        self.cursor.execute("SELECT count(*) FROM registros ")
        count = self.cursor.fetchone()
        filas = self.cursor.execute(self.query)

        iniciales = entrada_texto.mainloop_input()

        if count[0] > 0:
            for fila in filas:
                if count[0] >= 5:
                    if fila[1] < puntos:
                        cursor.execute(self.query3)
                        self.insertar_puntuacion(self.cursor, self.conn, puntos, iniciales[0])
                        break
                else:
                    self.insertar_puntuacion(self.cursor, self.conn, puntos, iniciales[0])
                    break
        else:
            self.insertar_puntuacion(self.cursor, self.conn, puntos, iniciales[0])

    def mostrar_ranking(self, puntos):
        self.posicion_usuarios(self.cursor, self.conn, puntos)

    def ver_base_datos(self):
        self.lista_ranking = self.cursor.execute("SELECT * FROM registros ")
        self.lista_ranking = self.cursor.fetchall()

        self.lista_ranking.sort(reverse=True, key=lambda list_rnk: list_rnk[2])
        self.mostrar_datos_ranking()
        
        return self.lista_ranking


    def text_espacio(self):

        self.linea_text_espacio = self.tamaño_titulo1.render('Menu pulsa "Escape" ', True, RED)
        self.screen.blit(self.linea_text_espacio,(50, 550))



class Entrada_texto():

    def __init__(self):
        pg.font.init()

        self.screen = pg.display.set_mode((800,600))
        self.background_image = pg.image.load('resources/images/fondo8.jpg').convert()
        pg.display.set_caption('The Quest')
        self.tamaño_titulo = pg.font.Font('resources/fonts/PressStart.ttf', 22)
        self.tamaño_titulo1 = pg.font.Font('resources/fonts/PressStart.ttf', 18)
        self.font = pg.font.Font('resources/fonts/CodaCaption-ExtraBold.ttf', 72)

        self.caracteres = ['']
        self.max_caracteres = 0

    def salir_pantalla(self):
        pg.quit()
        sys.exit()        

    def tecla(self, eventos):
        for evento in eventos:
            if evento.type == KEYDOWN:

                if evento.key == K_ESCAPE:
                    self.salir_pantalla()

                elif evento.key == K_BACKSPACE:
                    if self.caracteres[self.lineas] == '' and self.lineas > 0:
                        self.caracteres = self.caracteres[0:-1]
                        self.lineas -= 1
                    else:
                        self.caracteres[self.lineas] = self.caracteres[self.lineas][0:-1]
                        if self.max_caracteres > 0:
                            self.max_caracteres -= 1
                else:
                    if self.max_caracteres < 3:
                        self.caracteres[self.lineas] = str(self.caracteres[self.lineas] + evento.unicode)
                        self.max_caracteres += 1
                    if self.max_caracteres == 3 and evento.key == K_SPACE:
                        self.salir = True
                        return self.caracteres

    def mensaje(self, superficie):

        self.screen.blit(self.background_image, (0, 0))
        for self.lineas in range(len(self.caracteres)):
            nick = self.font.render(self.caracteres[self.lineas], True, WHITE)
            superficie.blit(nick, (300, 200))
        self.titulos()

        
    def titulos(self):

        self.linea_nick = self.tamaño_titulo.render('Escribe tus iniciales:', True, RED)
        self.screen.blit(self.linea_nick, (20, 60))
        self.linea_text_espacio = self.tamaño_titulo1.render('Guardar y regresar al menu pulsa "Espacio" ', True, RED)
        self.screen.blit(self.linea_text_espacio, (20, 550))


    def mainloop_input(self):
        self.salir = True
        texto_introducido = Entrada_texto()

        while self.salir:
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    self.salir = True

            iniciales = texto_introducido.tecla(eventos)
            if iniciales is not None:
                self.salir = False
            texto_introducido.mensaje(self.screen)
            pg.display.update()

        return iniciales


