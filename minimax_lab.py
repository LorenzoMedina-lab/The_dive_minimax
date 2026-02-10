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
            print(' '.join(fila))
        print("-" * 15)  # Linea separadora

    def realizar_movimiento(self, personaje, direccion):
        # 1. ¿Quién se mueve?
        if personaje == 'R':
            pos_actual = self.raton_pos
        else:
            pos_actual = self.gato_pos
    
        # 
        fila_actual = pos_actual[0]
        columna_actual = pos_actual[1]
        nueva_fila = fila_actual
        nueva_columna = columna_actual

        # Posicion
        if direccion == 'arriba':
            nueva_fila -= 1
        elif direccion == 'abajo':
            nueva_fila += 1
        elif direccion == 'izquierda':
            nueva_columna -= 1
        elif direccion == 'derecha':
            nueva_columna += 1

        # 4. Verifico limiyes
        if (0 <= nueva_fila < self.filas) and (0 <= nueva_columna < self.columnas):
            if personaje == 'R':
                self.raton_pos = [nueva_fila, nueva_columna]
            else:
                self.gato_pos = [nueva_fila, nueva_columna]
            
            self.actualizar_posiciones()
            return True 
        else:
            print(f"¡{personaje} intentó chocar contra una pared!")
            return False
#Agrego la Funcion de Evaluacion. medir que tan cerca esta el gato del raton
    def evaluar(self):
        distancia_fila = abs(self.gato_pos[0] - self.raton_pos[0])
        distancia_columna = abs(self.gato_pos[1] - self.raton_pos[1])
        return distancia_fila +  distancia_columna