from database import Database
from Logic.Models.Cliente import Cliente

class ClienteRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        """Obtiene todos los clientes de la base de datos."""
        self.db.connect()
        resultado = self.db.realizar_consulta("SELECT * FROM Cliente")
        self.db.disconnect()

        if resultado is None:
            return []

        return [Cliente(**cliente) for cliente in resultado]

    def obtener_por_id(self, id_cliente):
        """Obtiene un cliente específico por su ID."""
        self.db.connect()
        resultado = self.db.realizar_consulta("SELECT * FROM Cliente WHERE ID_Cliente = %s", (id_cliente,))
        self.db.disconnect()

        if not resultado:
            return None

        return Cliente(**resultado[0])

    def crear(self, cliente):
        """Crea un nuevo cliente en la base de datos."""
        query = """INSERT INTO Cliente (Nombre, Apellido, Fecha_Nacimiento, Email, Telefono) 
                   VALUES (%s, %s, %s, %s, %s)"""
        params = (cliente.nombre, cliente.apellido, cliente.fecha_nacimiento, 
                  cliente.email, cliente.telefono)
        self.db.connect()
        resultado = self.db.consultas_update_delete(query, params)
        self.db.disconnect()
        return resultado > 0

    def actualizar(self, cliente):
        """Actualiza la información de un cliente existente."""
        query = """UPDATE Cliente SET Nombre = %s, Apellido = %s, 
                   Fecha_Nacimiento = %s, Email = %s, Telefono = %s 
                   WHERE ID_Cliente = %s"""
        params = (cliente.nombre, cliente.apellido, cliente.fecha_nacimiento,
                  cliente.email, cliente.telefono, cliente.id_cliente)
        self.db.connect()
        resultado = self.db.consultas_update_delete(query, params)
        self.db.disconnect()
        return resultado > 0

    def eliminar(self, id_cliente):
        """Elimina un cliente de la base de datos."""
        query = "DELETE FROM Cliente WHERE ID_Cliente = %s"
        params = (id_cliente,)
        self.db.connect()
        resultado = self.db.consultas_update_delete(query, params)
        self.db.disconnect()
        return resultado > 0
