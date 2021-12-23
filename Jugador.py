
class Jugador():
   
    def __init__(self):
        """
        Constructor de la clase jugador recibe el nombre y el id del jugador
        """
        self.nombre=""
        self.nivel = 1
        self.maximo_premio=[100000,200000,400000,650000,1000000]
        self.tiempo_nivel=60
        self.premio_acumulado=0
        self.premio_nivel=0
   
    def actualizar_premio(self,tiempo):
        self.premio_nivel=self.maximo_premio[self.nivel-1]*(0.5+(tiempo/(2*self.tiempo_nivel)))
        self.premio_acumulado=self.premio_nivel+self.premio_acumulado
    
    def set_nombre(self):
        self.nombre=input("¿Por favor ingresa tu nombre?: ")
    
    def reset_jugador(self):
        self.nombre=""
        self.nivel = 1
        self.tiempo_nivel=60
        self.premio_acumulado=0
        self.premio_nivel=0