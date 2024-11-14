# repository/equipo_repository.py
from utils.database import Database

class EquipoRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = "SELECT * FROM Equipo"
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_equipo):
        query = "SELECT * FROM Equipo WHERE ID_Equipo = %s"
        resultados = self.db.execute_query(query, (id_equipo,), dictionary=True)
        return resultados[0] if resultados else None

    def crear(self, equipo):
        query = "INSERT INTO Equipo (Nombre_Equipo, Estado) VALUES (%s, %s)"
        params = (equipo.Nombre_Equipo, equipo.Estado)
        return self.db.execute_query(query, params)

    def actualizar(self, equipo):
        query = """UPDATE Equipo 
                   SET Nombre_Equipo = %s, Estado = %s
                   WHERE ID_Equipo = %s"""
        params = (equipo.Nombre_Equipo, equipo.Estado, equipo.ID_Equipo)
        return self.db.execute_query(query, params)

    def eliminar(self, id_equipo):
        query = "DELETE FROM Equipo WHERE ID_Equipo = %s"
        return self.db.execute_query(query, (id_equipo,))