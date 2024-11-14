# repository/pago_repository.py
from utils.database import Database

class PagoRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = """
        SELECT p.*, m.ID_Cliente, CONCAT(c.Nombre, ' ', c.Apellido) as Nombre_Cliente 
        FROM Pago p 
        JOIN Membresia m ON p.ID_Membresia = m.ID_Membresia 
        JOIN Cliente c ON m.ID_Cliente = c.ID_Cliente
        """
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_pago):
        query = """
        SELECT p.*, m.ID_Cliente, CONCAT(c.Nombre, ' ', c.Apellido) as Nombre_Cliente 
        FROM Pago p 
        JOIN Membresia m ON p.ID_Membresia = m.ID_Membresia 
        JOIN Cliente c ON m.ID_Cliente = c.ID_Cliente 
        WHERE p.ID_Pago = %s
        """
        resultados = self.db.execute_query(query, (id_pago,), dictionary=True)
        return resultados[0] if resultados else None

    def obtener_por_membresia(self, id_membresia):
        query = "SELECT * FROM Pago WHERE ID_Membresia = %s"
        return self.db.execute_query(query, (id_membresia,), dictionary=True)

    def crear(self, pago):
        query = """INSERT INTO Pago (ID_Membresia, Fecha_Pago, Monto, 
                                   Metodo_Pago)
                   VALUES (%s, %s, %s, %s)"""
        params = (pago.ID_Membresia, pago.Fecha_Pago,
                 pago.Monto, pago.Metodo_Pago)
        return self.db.execute_query(query, params)

    def actualizar(self, pago):
        query = """UPDATE Pago 
                   SET ID_Membresia = %s, Fecha_Pago = %s,
                       Monto = %s, Metodo_Pago = %s
                   WHERE ID_Pago = %s"""
        params = (pago.ID_Membresia, pago.Fecha_Pago,
                 pago.Monto, pago.Metodo_Pago, pago.ID_Pago)
        return self.db.execute_query(query, params)

    def eliminar(self, id_pago):
        query = "DELETE FROM Pago WHERE ID_Pago = %s"
        return self.db.execute_query(query, (id_pago,))