from utils.database import Database

class GastoRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = "SELECT * FROM Gasto"
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_gasto):
        query = "SELECT * FROM Gasto WHERE ID_Gasto = %s"
        return self.db.execute_query(query, (id_gasto,), dictionary=True)

    def crear(self, gasto):
        query = """INSERT INTO Gasto (Fecha_Gasto, Monto, Metodo_Pago, Descripcion)
                   VALUES (%s, %s, %s, %s)"""
        params = (gasto.Fecha_Gasto, gasto.Monto, gasto.Metodo_Pago, gasto.Descripcion)
        return self.db.execute_query(query, params)

    def actualizar(self, gasto):
        query = """UPDATE Gasto 
                   SET Fecha_Gasto = %s, Monto = %s, Metodo_Pago = %s, Descripcion = %s
                   WHERE ID_Gasto = %s"""
        params = (gasto.Fecha_Gasto, gasto.Monto, gasto.Metodo_Pago, gasto.Descripcion, gasto.ID_Gasto)
        return self.db.execute_query(query, params)

    def eliminar(self, id_gasto):
        query = "DELETE FROM Gasto WHERE ID_Gasto = %s"
        return self.db.execute_query(query, (id_gasto,))
