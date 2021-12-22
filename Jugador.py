from time import sleep
from BaseDeDatos import BaseDeDatos

class Jugador():
   
    def __init__(self):
        """
        Constructor de la clase jugador recibe el nombre y el id del jugador
        """
        self.nombre=""
        self.nivel = 0
        self.premio = 0
        self.identificacion= 0

    def validar_id(self):
        self.identificacion=input("¿Por favor ingresa tu numero de ientificacion?: ")
        try:
            baseDeDatos=BaseDeDatos()
            self.identificacion=int(self.identificacion);
            if (baseDeDatos.existeJugador(self.identificacion)== NoneType):
                print("usuario no existe")
                sleep(15)
            else:
                print("usuario existe")
            sleep(15)
        except:
            print("La identificaciond debe ser un numero entero")
            sleep(7)
            return False
