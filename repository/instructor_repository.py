# repository/instructor_repository.py
from utils.database import Database

class InstructorRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = "SELECT * FROM Instructor"
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_instructor):
        query = "SELECT * FROM Instructor WHERE ID_Instructor = %s"
        resultados = self.db.execute_query(query, (id_instructor,), dictionary=True)
        return resultados[0] if resultados else None

    def crear(self, instructor):
        query = """INSERT INTO Instructor (Nombre, Apellido, Especialidad, 
                                         Email, Telefono)
                   VALUES (%s, %s, %s, %s, %s)"""
        params = (instructor.Nombre, instructor.Apellido, instructor.Especialidad,
                 instructor.Email, instructor.Telefono)
        return self.db.execute_query(query, params)

    def actualizar(self, instructor):
        query = """UPDATE Instructor 
                   SET Nombre = %s, Apellido = %s, 
                       Especialidad = %s, Email = %s, Telefono = %s
                   WHERE ID_Instructor = %s"""
        params = (instructor.Nombre, instructor.Apellido, instructor.Especialidad,
                 instructor.Email, instructor.Telefono, instructor.ID_Instructor)
        return self.db.execute_query(query, params)

    def eliminar(self, id_instructor):
        query = "DELETE FROM Instructor WHERE ID_Instructor = %s"
        return self.db.execute_query(query, (id_instructor,))