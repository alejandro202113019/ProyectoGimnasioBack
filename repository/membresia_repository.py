# repository/membresia_repository.py
from utils.database import Database

class MembresiaRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        
        query = "UPDATE Membresia set Estado = 'Inactiva' WHERE Fecha_Fin < CURRENT_DATE"
        self.db.execute_query(query, dictionary=True)
        
        query = "UPDATE Membresia set Estado = 'Activa' WHERE Fecha_Fin > CURRENT_DATE"
        self.db.execute_query(query, dictionary=True)
        
        query = """SELECT Cliente.ID_Cliente, Membresia.ID_Cliente as ID_Cliente_Membresia, Membresia.ID_Membresia, CONCAT(Cliente.Nombre, ' ', Cliente.Apellido) as nombre, Plan.Nombre_Plan, Plan.Descripcion, 
        Membresia.Fecha_Inicio, Membresia.Fecha_Fin, Membresia.Estado
        FROM Cliente LEFT JOIN Membresia ON Cliente.ID_Cliente = Membresia.ID_Cliente 
        LEFT JOIN Plan ON Membresia.ID_Plan = Plan.ID_Plan"""
        
        
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_membresia):
        query = """SELECT Cliente.ID_Cliente, Membresia.ID_Cliente as ID_Cliente_Membresia, Membresia.ID_Membresia, CONCAT(Cliente.Nombre, ' ', Cliente.Apellido) as nombre, Plan.Nombre_Plan, Plan.Descripcion, 
        Membresia.Fecha_Inicio, Membresia.Fecha_Fin, Membresia.Estado
        FROM Cliente LEFT JOIN Membresia ON Cliente.ID_Cliente = Membresia.ID_Cliente 
        LEFT JOIN Plan ON Membresia.ID_Plan = Plan.ID_Plan WHERE Cliente.ID_Cliente = %s"""
        resultados = self.db.execute_query(query, (id_membresia,), dictionary=True)
        return resultados[0] if resultados else None

    def obtener_por_id_2(self, id_membresia):
        query = """SELECT * FROM Membresia WHERE ID_Membresia = %s"""
        return self.db.execute_query(query, (id_membresia,), dictionary=True)

    def crear(self, membresia):
        query = """INSERT INTO Membresia (ID_Cliente, ID_Plan, Fecha_Inicio, 
                                        Fecha_Fin, Estado)
                   VALUES (%s, %s, %s, %s, %s)"""
                
        params = (membresia.ID_Cliente, membresia.ID_Plan, membresia.Fecha_Inicio,
                 membresia.Fecha_Fin, membresia.Estado)
        
        return self.db.execute_query(query, params)

    def actualizar(self, membresia):
        if (membresia.Estado == 'null'):
            query = """UPDATE Membresia SET Fecha_Fin = %s WHERE ID_Cliente = %s"""
            params = (membresia.Fecha_Fin, membresia.ID_Membresia)
            return self.db.execute_query(query, params)
        else:
            query = """UPDATE Membresia 
                   SET ID_Cliente = %s, ID_Plan = %s, 
                       Fecha_Inicio = %s, Fecha_Fin = %s, Estado = %s
                   WHERE ID_Cliente = %s"""
            params = (membresia.ID_Cliente, membresia.ID_Plan, membresia.Fecha_Inicio,
                 membresia.Fecha_Fin, membresia.Estado, membresia.ID_Membresia)
            return self.db.execute_query(query, params)
        

    def eliminar(self, id_membresia):
        query = "DELETE FROM Pago WHERE ID_Membresia = %s"
        self.db.execute_query(query, (id_membresia,))
        query = "DELETE FROM Membresia WHERE ID_Membresia = %s"
        return self.db.execute_query(query, (id_membresia,))