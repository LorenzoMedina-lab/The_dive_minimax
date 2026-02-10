#Creo el laberinto
import random

class Laberinto:
    def __init__(self, filas, columnas):
        self.filas=filas
        self.columnas=columnas
        # Genero la matrix representando los puntos como suelo vacio
        self.tablero = [['.'for _ in range(columnas)]for _ in range (filas)]

        #Posicion inicial (Fila, Columna)
        self.gato_pos = [0,0]
        self.raton_pos= [filas -1, columnas -1]
        self.actualizar_posiciones()

    def actualizar_posiciones(self):
        #Coloca al raton y gato en sus lugares
        for f in range(self.filas):
            for c in range(self.columnas):
                self.tablero[f][c] = '.'
        #Ubico a los personajes
        self.tablero[self.gato_pos[0]][self.gato_pos[1]] = 'G'
        self.tablero[self.raton_pos[0]][self.raton_pos[1]]= 'R'
    def mostrar(self):
        #Dibuja el tablero en la consola
        for fila in self.tablero:
            print("-" * (self.columnas * 2))  #Una linea separadora

mi_juego = Laberinto(5,5)
mi_juego.mostrar()