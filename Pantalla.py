import utility
from BaseDeDatos import BaseDeDatos

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

    def mostrar_ganadores(self):
        baseDeDatos=BaseDeDatos()
        ganadores=baseDeDatos.ganadores()
        utility.clear() 
        print("LISTA DE GANADORES")
        for fila in ganadores:
            print(fila)
        salir=input("Presiona la tecla enter para volver al menu inicial ")


    def max_premios(self):
        baseDeDatos=BaseDeDatos()
        ganadores=baseDeDatos.premiados()
        utility.clear() 
        print("LISTA EN ORDEN DESCENDENTE DE MAYORES PREMIOS")
        for fila in ganadores:
            print(fila)
        salir=input("Presiona la tecla enter para volver al menu inicial ") 
