# repository/pago_repository.py
from utils.database import Database

class PagoRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = """SELECT Pago.*, Membresia.ID_Cliente, CONCAT(Cliente.Nombre, ' ', Cliente.Apellido) AS Nombre_Completo_Cliente, Plan.Nombre_Plan
        FROM  Pago INNER JOIN Membresia ON Membresia.ID_Membresia = Pago.ID_Membresia INNER JOIN Cliente ON Cliente.ID_Cliente = Membresia.ID_Cliente
        INNER JOIN Plan ON Membresia.ID_Plan = Plan.ID_Plan"""

        
        # return self.db.execute_query(query, dictionary=True)
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_pago):
        query = """SELECT Pago.*, Membresia.ID_Cliente, CONCAT(Cliente.Nombre, ' ', Cliente.Apellido) AS Nombre_Completo_Cliente, Plan.Nombre_Plan
        FROM  Pago INNER JOIN Membresia ON Membresia.ID_Membresia = Pago.ID_Membresia INNER JOIN Cliente ON Cliente.ID_Cliente = Membresia.ID_Cliente
        INNER JOIN Plan ON Membresia.ID_Plan = Plan.ID_Plan WHERE Cliente.ID_Cliente = %s
        """
        
        return self.db.execute_query(query, (id_pago,), dictionary=True)

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