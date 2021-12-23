import utility
import keyboard
import time
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

    def mostrar_pregunta(self,pregunta,opcion,premio,nivel):
        t=time.time()+30
        self.pintar_pregunta(pregunta,opcion,premio,nivel)
        while (t-time.time()) > 0:
            tiempo=t-time.time()

            if keyboard.is_pressed('1'):
                return(opcion[0],tiempo)
                break 
            elif keyboard.is_pressed('2'):
                return(opcion[1],tiempo)
                break
            elif keyboard.is_pressed('3'):
                return(opcion[2],tiempo)
                break 
            elif keyboard.is_pressed('4'):
                return(opcion[3],tiempo)
                break 
            elif keyboard.is_pressed('5'):
                return("Retirarse",tiempo)
                break
        return(" se acabo el tiempo",tiempo)      

    
    def pintar_pregunta(self,pregunta,opcion,premio,nivel):
        utility.clear()
        print(pregunta)
        print(  "\n 1->  ",opcion[0],
                "\n 2->  ",opcion[1],  
                "\n 3->  ",opcion[2],
                "\n 4->  ",opcion[3],
                "\n 5->  Retirarse",
                "\n\n Premio Acumulado: ",premio,"   Nivel: ",nivel,
                "\n Ingrese el numero de la respuesta escogida: ") 


""""
        print("\n Tiempo restante: ",tiempo,
              "\n Premi Actual= ",premio_nivel,
              "\n Ingrese el numero de la respuesta escogida: ")
        time.sleep(float(1))
"""
"""
        utility.clear()
        print(pregunta)
        
        print(  "\n 1->  ",opcion[0],
                "\n 2->  ",opcion[1],  
                "\n 3->  ",opcion[2],
                "\n 4->  ",opcion[3]) 
        print("\n Ingrese el numero de la respuesta escogida: ") 
   
    def mostar_derrota(self,causa):
        utility.clear()
        if(causa=="tiempo"):
            print("lo siento se agoto el tiempo")
        else:
            print("Respuesta incorrecta")    
        sleep(10)
        """ 