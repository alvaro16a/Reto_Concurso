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
   




