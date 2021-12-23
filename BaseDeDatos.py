import sqlite3

class BaseDeDatos():


    def ganadores(self):

        conexion = sqlite3.connect('Concurso.sqlite')
        cursor = conexion.cursor()
        cursor.execute('SELECT nombre FROM Jugadores WHERE nivel = 5')
        respuesta=cursor.fetchall()
        cursor.close()
        return(respuesta)

    def premiados(self):

        conexion = sqlite3.connect('Concurso.sqlite')
        cursor = conexion.cursor()
        cursor.execute('SELECT nombre,premio FROM Jugadores ORDER BY premio DESC')
        respuesta=cursor.fetchall()
        cursor.close()
        return(respuesta)
   
    def get_pregunta(self,nivel):

        conexion = sqlite3.connect('Concurso.sqlite')
        cursor = conexion.cursor()
        cursor.execute('SELECT pregunta,respuesta,opcion1,opcion2,opcion3 FROM Preguntas WHERE nivel = ? ORDER BY RANDOM() LIMIT 1',(nivel,))
        respuesta=cursor.fetchone()
        return(respuesta)

    def set_jugador(self,nombre,nivel,premio):

        conexion = sqlite3.connect('Concurso.sqlite')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO Jugadores (nombre,nivel,premio) VALUES ( ? ,? ,?)',(nombre, nivel, premio))
        conexion.commit()
        cursor.close()

        


