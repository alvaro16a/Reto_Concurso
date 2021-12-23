
import time
from Jugador import Jugador
from Pantalla import Pantalla 
from Pregunta import Pregunta
from BaseDeDatos import BaseDeDatos

#Variable global
estado = 0 #Esta variable le indica al probrama cual es su estado de operacion actual
ejecucion = True
nivel=1
pantalla=Pantalla()
jugador=Jugador()
baseDeDatos=BaseDeDatos()

#Estados
def state0():
    """
    Despliega el menu inicial y actua deacuerdo a lo seleccionado por el usuario
    """
    global estado,ejecucion,pantalla,jugador
    opcion=pantalla.menu_inicial()

    if opcion == "1":
        jugador.set_nombre()
        estado=1    
    elif (opcion == "2"):
        pantalla.mostrar_ganadores()
    elif (opcion == "3"):
        pantalla.max_premios()
    elif (opcion == "4"):
        ejecucion=False

def state1():
    """
    Despliega la pregunta y actua deacuerdo a la respuesta del usuario
    """
    global estado,nivel,pantalla,jugador
    pregunta=Pregunta(nivel)
    respuesta_seleccionada,tiempo=pantalla.mostrar_pregunta(pregunta.pregunta,pregunta.desordenar_opciones(), jugador.premio_acumulado,nivel)
    print(respuesta_seleccionada)
    time.sleep(3)
    
    if(respuesta_seleccionada==pregunta.respuesta_correcta):
        respuesta_correcta(tiempo)
    elif(respuesta_seleccionada == "Retirarse"):
        if(jugador.premio_acumulado>0):
            print("Te retiras con tu premio desde ahora puedes ver tu nombre en la lista de Mayores premios")
            baseDeDatos.set_jugador(jugador.nombre,jugador.nivel,jugador.premio_acumulado)
            reset()
        else:
            print("No gano nada por lo que no se guarda el usuario")
            reset()
    elif(respuesta_seleccionada == "se acabo el tiempo"):
            print("Te demoraste mucho para responder")
            reset()
    else:
            print("Respuesta incorrecta")
            reset()

def reset():
    """
    Esta funcion reinicia el juego
    """
    global estado,nivel,jugador
    jugador.reset_jugador()
    time.sleep(5)
    estado=0
    nivel=1

def respuesta_correcta(tiempo):
    """
    Esta funcion ejecuta las acciones a realizar cuando se ha dado una respuesta correcta
    """
    global estado,nivel,jugador
    jugador.actualizar_premio(tiempo)
    nivel=nivel+1
    jugador.nivel=nivel
    print("respuesta correcta")
    time.sleep(4)
    if (nivel==6):
        baseDeDatos.set_jugador(jugador.nombre,5,jugador.premio_acumulado)
        print("Felicitaciones, ya puedes ver tu nombre en la lista de ganadores")
        reset()    

def FSM():
    global estado
    switch = {
        0:state0,
        1:state1,
    }
    switch.get(estado, state0)()
    
while ejecucion:    #Programa Principal
    FSM()