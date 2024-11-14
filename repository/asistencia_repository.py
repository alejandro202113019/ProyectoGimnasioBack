# repository/asistencia_repository.py
from utils.database import Database

class AsistenciaRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = """
        SELECT a.*, CONCAT(c.Nombre, ' ', c.Apellido) as Nombre_Completo 
        FROM Asistencia a 
        JOIN Cliente c ON a.ID_Cliente = c.ID_Cliente
        """
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_asistencia):
        query = """
        SELECT a.*, CONCAT(c.Nombre, ' ', c.Apellido) as Nombre_Completo 
        FROM Asistencia a 
        JOIN Cliente c ON a.ID_Cliente = c.ID_Cliente 
        WHERE a.ID_Asistencia = %s
        """
        resultados = self.db.execute_query(query, (id_asistencia,), dictionary=True)
        return resultados[0] if resultados else None

    def obtener_por_cliente(self, id_cliente):
        query = "SELECT * FROM Asistencia WHERE ID_Cliente = %s"
        return self.db.execute_query(query, (id_cliente,), dictionary=True)

    def crear(self, asistencia):
        query = """INSERT INTO Asistencia (ID_Cliente, Fecha_Hora_Entrada, 
                                         Fecha_Hora_Salida)
                   VALUES (%s, %s, %s)"""
        params = (asistencia.ID_Cliente, asistencia.Fecha_Hora_Entrada,
                 asistencia.Fecha_Hora_Salida)
        return self.db.execute_query(query, params)

    def actualizar(self, asistencia):
        query = """UPDATE Asistencia 
                   SET ID_Cliente = %s, Fecha_Hora_Entrada = %s,
                       Fecha_Hora_Salida = %s
                   WHERE ID_Asistencia = %s"""
        params = (asistencia.ID_Cliente, asistencia.Fecha_Hora_Entrada,
                 asistencia.Fecha_Hora_Salida, asistencia.ID_Asistencia)
        return self.db.execute_query(query, params)

    def eliminar(self, id_asistencia):
        query = "DELETE FROM Asistencia WHERE ID_Asistencia = %s"
        return self.db.execute_query(query, (id_asistencia,))
