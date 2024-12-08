# repository/horario_repository.py
from utils.database import Database

class HorarioRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = """SELECT h.*, c.Nombre_Clase, CONCAT(i.Nombre,' ',i.Apellido) as Nombre_Instructor
        FROM Horario h 
        JOIN Clase c ON h.ID_Clase = c.ID_Clase JOIN Instructor i ON c.ID_Instructor = i.ID_Instructor
        """
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_horario):
        query = """SELECT h.*, c.Nombre_Clase 
        FROM Horario h 
        JOIN Clase c ON h.ID_Clase = c.ID_Clase 
        WHERE h.ID_Horario = %s
        """
        resultados = self.db.execute_query(query, (id_horario,), dictionary=True)
        return resultados[0] if resultados else None

    def obtener_por_clase(self, id_clase):
        query = "SELECT * FROM Horario WHERE ID_Clase = %s"
        return self.db.execute_query(query, (id_clase,), dictionary=True)

    def crear(self, horario):
        query = """INSERT INTO Horario (ID_Clase, Dia_Semana, 
                                      Hora_Inicio, Hora_Fin)
                   VALUES ((SELECT MAX(ID_Clase) FROM Clase), %s, %s, %s)"""
        params = (horario.Dia_Semana,
                 horario.Hora_Inicio, horario.Hora_Fin)
        return self.db.execute_query(query, params)

    def actualizar(self, horario):
        query = """UPDATE Horario 
                   SET ID_Clase = %s, Dia_Semana = %s,
                       Hora_Inicio = %s, Hora_Fin = %s
                   WHERE ID_Horario = %s"""
        params = (horario.ID_Clase, horario.Dia_Semana,
                 horario.Hora_Inicio, horario.Hora_Fin, horario.ID_Horario)
        return self.db.execute_query(query, params)

    def eliminar(self, id_horario):
        query = "DELETE FROM Horario WHERE ID_Horario = %s"
        return self.db.execute_query(query, (id_horario,))