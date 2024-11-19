from utils.database import Database

class ClienteRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        
        query = "UPDATE Membresia set Estado = 'Inactiva' WHERE Fecha_Fin < CURRENT_DATE"
        self.db.execute_query(query, dictionary=True)
        
        query = "UPDATE Membresia set Estado = 'Activa' WHERE Fecha_Fin > CURRENT_DATE"
        self.db.execute_query(query, dictionary=True)
        
        query = """SELECT Cliente.*, Plan.Nombre_Plan, Membresia.Estado
        FROM Cliente LEFT JOIN Membresia ON Cliente.ID_Cliente = Membresia.ID_Cliente LEFT JOIN Plan ON Membresia.ID_Plan = Plan.ID_Plan"""
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_cliente):
        query = "SELECT * FROM Cliente WHERE ID_Cliente = %s"
        resultados = self.db.execute_query(query, (id_cliente,), dictionary=True)
        return resultados[0] if resultados else None

    def verificar_id_existe(self, id_cliente):
        query = "SELECT ID_Cliente FROM Cliente WHERE ID_Cliente = %s"
        return bool(self.db.execute_query(query, (id_cliente,)))

    def crear(self, cliente):
        query = """INSERT INTO Cliente (ID_Cliente, Nombre, Apellido, Email, Fecha_Nacimiento, Telefono)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        params = (cliente.ID_Cliente, cliente.Nombre, cliente.Apellido, 
                 cliente.Email, cliente.Fecha_Nacimiento, cliente.Telefono)
        return self.db.execute_query(query, params)

    def actualizar(self, cliente):
        query = """UPDATE Cliente 
                   SET Nombre = %s, Apellido = %s, Email = %s, 
                       Fecha_Nacimiento = %s, Telefono = %s
                   WHERE ID_Cliente = %s"""
        params = (cliente.Nombre, cliente.Apellido, cliente.Email,
                 cliente.Fecha_Nacimiento, cliente.Telefono, cliente.ID_Cliente)
        return self.db.execute_query(query, params)

    def eliminar(self, id_cliente):
        # Eliminar pagos relacionados
        self.db.execute_query(
            "DELETE FROM Pago WHERE ID_Membresia IN (SELECT ID_Membresia FROM Membresia WHERE ID_Cliente = %s)",
            (id_cliente,)
        )
        
        # Eliminar membresías
        self.db.execute_query(
            "DELETE FROM Membresia WHERE ID_Cliente = %s",
            (id_cliente,)
        )
        
        # Eliminar asistencias
        self.db.execute_query(
            "DELETE FROM Asistencia WHERE ID_Cliente = %s",
            (id_cliente,)
        )
        
        # Eliminar cliente
        return self.db.execute_query(
            "DELETE FROM Cliente WHERE ID_Cliente = %s",
            (id_cliente,)
        )