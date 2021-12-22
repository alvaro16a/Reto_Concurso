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
        print(self.opciones)