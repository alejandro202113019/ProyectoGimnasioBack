from database import Database
from Logic.Models.Cliente import Cliente
from mysql.connector import Error

class ClienteRepository:
    def __init__(self):
        self.db = Database()
        self.db.connect()  # Creamos el pool de conexiones al inicializar el objeto

    def obtener_todos(self):
        try:
            resultado = self.db.realizar_consulta("SELECT * FROM Cliente")
            return [Cliente(**cliente) for cliente in resultado] if resultado else []
        except Error as e:
            print(f"Error al obtener todos los clientes: {e}")
            return []

    def obtener_por_id(self, id_cliente):
        try:
            resultado = self.db.realizar_consulta("SELECT * FROM Cliente WHERE ID_Cliente = %s", (id_cliente,))
            return Cliente(**resultado[0]) if resultado else None
        except Error as e:
            print(f"Error al obtener cliente por ID: {e}")
            return None

    def crear(self, cliente):
        query = """INSERT INTO Cliente (Nombre, Apellido, Fecha_Nacimiento, Email, Telefono) 
                   VALUES (%s, %s, %s, %s, %s)"""
        params = (cliente.Nombre, cliente.Apellido, cliente.Fecha_Nacimiento, 
                  cliente.Email, cliente.Telefono)
        try:
            return self.db.consultas_update_delete(query, params)
        except Error as e:
            print(f"Error al crear cliente: {e}")
            return None

    def actualizar(self, cliente):
        query = """UPDATE Cliente SET Nombre = %s, Apellido = %s, 
                   Fecha_Nacimiento = %s, Email = %s, Telefono = %s 
                   WHERE ID_Cliente = %s"""
        params = (cliente.Nombre, cliente.Apellido, cliente.Fecha_Nacimiento,
                  cliente.Email, cliente.Telefono, cliente.ID_Cliente)
        try:
            resultado = self.db.consultas_update_delete(query, params)
            return resultado > 0
        except Error as e:
            print(f"Error al actualizar cliente: {e}")
            return False

    def eliminar(self, id_cliente):
        try:
            # Primero, intentamos eliminar las asistencias asociadas
            query_asistencia = "DELETE FROM Asistencia WHERE ID_Cliente = %s"
            self.db.consultas_update_delete(query_asistencia, (id_cliente,))
            
            # Luego, intentamos eliminar el cliente
            query_cliente = "DELETE FROM Cliente WHERE ID_Cliente = %s"
            resultado = self.db.consultas_update_delete(query_cliente, (id_cliente,))
            
            return resultado > 0
        except Error as e:
            print(f"Error al eliminar cliente: {e}")
            return False