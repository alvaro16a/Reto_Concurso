from time import sleep
class Jugador():
   
    def __init__(self):
        """
        Constructor de la clase jugador recibe el nombre y el id del jugador
        """
        self.nombre=input("¿Por favor ingresa tu nombre?: ")
        self.identificacion=0
        self.identificacion=0
        self.nivel = 1
        self.premio = 0
        self.premio_maximo = 0

    def validar_id(self):
        self.identificacion=input("¿Por favor ingresa tu numero de ientificacion?: ")
        try:
            self.identificacion=int(self.identificacion);
            return True
        except:
            print("La identificaciond debe ser un numero entero")
            sleep(5)
            return False