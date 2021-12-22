from time import sleep
from BaseDeDatos import BaseDeDatos

class Jugador():
   
    def __init__(self):
        """
        Constructor de la clase jugador recibe el nombre y el id del jugador
        """
        self.nombre=input("¿Por favor ingresa tu nombre?: ")
        self.nivel = 1
        self.premio = 0

   
