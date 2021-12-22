import utility

class Pantalla():
   
    def __init__(self):
        """
        Constructor de la clase pantalla
        """
        self.nivel=0
        self.nombre=""
        self.premio_actual = 0

    def menu_inicial(self):
        utility.clear() 
        print ("""
        1.Iniciar un nuevo juego
        2.Ver lista de ganadores
        3.ver lista de mayores puntajes
        4.Terminar juego
        """)
        return(input("¿Que te gustaria hacer?: "))


    def set_nombre(self,jugador):
        self.nombre=jugador

    def set_premio(self,premio):
        self.premio_actual=premio