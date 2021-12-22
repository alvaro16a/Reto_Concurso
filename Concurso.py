import utility
import time
from Jugador import Jugador
from Pantalla import Pantalla 

#Variable global
estado = 0 #Esta variable le indica al probrama cual es su estado de operacion actual
ejecucion = True


#Estados
def state0():
    """
    Despliega el menu inicial en el que el usuario puede escoger:
        1-iniciar nuevo juego
        2-ver lista de ganadores
        3-lista de mayores puntajes
        4-cerrar la app
    """

    global estado,ejecucion
    pantalla=Pantalla()
    opcion=pantalla.menu_inicial()

    if opcion == "1":
        jugador=Jugador()
        estado=1 if(jugador.validar_id()) else 0  
        
    elif (opcion== "4"):
        ejecucion=False

def state1():
    """
    En este estado se carga la pregunta deacuerdo al nivel
    se inicia el temporizador
    """
    global estado
    print("estoy en el estado 1")
    time.sleep(50)
def state2():
    """
    deacuerdo al resultado de la interacion anterior decide: 
    si el jugador se retiro
    acerto o se equivo 
    termino el juego
    """
    global estado

def state3():
    """
    despliega mensaje de ganador
    """
    global estado

def state4():
    """
    despliega mensaje de retiro
    """
    global estado

def state5():
    """
    despliega mensaje de derrota
    """
    global estado

def state6():
    """
    almacena informacion del jugador en la base de datos
    """
    global estado

def FSM():
    global estado
    switch = {
        0:state0,
        1:state1,
        2:state2,
        3:state3,
        4:state3,
        5:state3,
        6:state3,
    }
    switch.get(estado, state0)()
    
while ejecucion:    #Programa Principal
    FSM()