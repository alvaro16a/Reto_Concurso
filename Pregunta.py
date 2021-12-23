import random


from BaseDeDatos import BaseDeDatos

class Pregunta():
   
    def __init__(self, nivel):
        """
        Constructor de la clase pregunta, esta se encarga de solicitarle a la base de datos la pregunta a ser desplegada
        """

        basededatos=BaseDeDatos()
        respuesta=basededatos.get_pregunta(nivel)
        self.pregunta=respuesta[0]
        self.respuesta_correcta = respuesta[1]
        self.opciones = respuesta[1:5]

    def desordenar_opciones(self):
        """
        Este metodo se encarga de desordenar las opciones.
        """
        opciones_desorden=[]
        lista=[0,1,2,3]
        nueva_lista=[]#en esta variable que da almacenado el nuevo orden
        contador=0
        while contador <4:
            valor=random.choice(lista)
            nueva_lista.append(valor)
            lista.remove(valor)
            contador=contador+1
       
        opciones_desorden.append(self.opciones[nueva_lista[0]])
        opciones_desorden.append(self.opciones[nueva_lista[1]])
        opciones_desorden.append(self.opciones[nueva_lista[2]])
        opciones_desorden.append(self.opciones[nueva_lista[3]])
        
        return(opciones_desorden)
        

    def validar_respuesta(self,respuesta):
        return True if(self.respuesta_correcta == respuesta) else False
 