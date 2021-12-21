class Jugador():
   
    def __init__(self, nombre,id):
        """
        Constructor de la clase jugador recibe el nombre y el id del jugador
        """
        self.nombre = nombre
        self.id = id
        self.nivel = 1
        self.premio= 0