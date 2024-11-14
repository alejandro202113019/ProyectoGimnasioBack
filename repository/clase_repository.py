from utils.database import Database

class ClaseRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = """
        SELECT c.*, i.Nombre as Instructor_Nombre, i.Apellido as Instructor_Apellido 
        FROM Clase c 
        JOIN Instructor i ON c.ID_Instructor = i.ID_Instructor
        """
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_clase):
        query = """
        SELECT c.*, i.Nombre as Instructor_Nombre, i.Apellido as Instructor_Apellido 
        FROM Clase c 
        JOIN Instructor i ON c.ID_Instructor = i.ID_Instructor 
        WHERE c.ID_Clase = %s
        """
        resultados = self.db.execute_query(query, (id_clase,), dictionary=True)
        return resultados[0] if resultados else None

    def crear(self, clase):
        query = """INSERT INTO Clase (Nombre_Clase, ID_Instructor, 
                                    Capacidad_Maxima, Duracion)
                   VALUES (%s, %s, %s, %s)"""
        params = (clase.Nombre_Clase, clase.ID_Instructor,
                 clase.Capacidad_Maxima, clase.Duracion)
        return self.db.execute_query(query, params)

    def actualizar(self, clase):
        query = """UPDATE Clase 
                   SET Nombre_Clase = %s, ID_Instructor = %s,
                       Capacidad_Maxima = %s, Duracion = %s
                   WHERE ID_Clase = %s"""
        params = (clase.Nombre_Clase, clase.ID_Instructor,
                 clase.Capacidad_Maxima, clase.Duracion, clase.ID_Clase)
        return self.db.execute_query(query, params)

    def eliminar(self, id_clase):
        query = "DELETE FROM Clase WHERE ID_Clase = %s"
        return self.db.execute_query(query, (id_clase,))