# repository/membresia_repository.py
from utils.database import Database

class MembresiaRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = "SELECT * FROM Membresia"
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_membresia):
        query = "SELECT * FROM Membresia WHERE ID_Membresia = %s"
        resultados = self.db.execute_query(query, (id_membresia,), dictionary=True)
        return resultados[0] if resultados else None

    def crear(self, membresia):
        query = """INSERT INTO Membresia (ID_Cliente, ID_Plan, Fecha_Inicio, 
                                        Fecha_Fin, Estado)
                   VALUES (%s, %s, %s, %s, %s)"""
        params = (membresia.ID_Cliente, membresia.ID_Plan, membresia.Fecha_Inicio,
                 membresia.Fecha_Fin, membresia.Estado)
        return self.db.execute_query(query, params)

    def actualizar(self, membresia):
        query = """UPDATE Membresia 
                   SET ID_Cliente = %s, ID_Plan = %s, 
                       Fecha_Inicio = %s, Fecha_Fin = %s, Estado = %s
                   WHERE ID_Membresia = %s"""
        params = (membresia.ID_Cliente, membresia.ID_Plan, membresia.Fecha_Inicio,
                 membresia.Fecha_Fin, membresia.Estado, membresia.ID_Membresia)
        return self.db.execute_query(query, params)

    def eliminar(self, id_membresia):
        query = "DELETE FROM Membresia WHERE ID_Membresia = %s"
        return self.db.execute_query(query, (id_membresia,))