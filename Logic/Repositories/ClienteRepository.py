#ClienteRepository.py
from database import Database
from Logic.Models.Cliente import Cliente
from mysql.connector import Error  # Importa Error desde mysql.connector

class ClienteRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        self.db.connect()
        try:
            resultado = self.db.realizar_consulta("SELECT * FROM Cliente")
            return [Cliente(**cliente) for cliente in resultado] if resultado else []
        finally:
            self.db.disconnect()

    def obtener_por_id(self, id_cliente):
        self.db.connect()
        try:
            resultado = self.db.realizar_consulta("SELECT * FROM Cliente WHERE ID_Cliente = %s", (id_cliente,))
            return Cliente(**resultado[0]) if resultado else None
        finally:
            self.db.disconnect()



    def crear(self, cliente):
        query = """INSERT INTO Cliente (Nombre, Apellido, Fecha_Nacimiento, Email, Telefono) 
                   VALUES (%s, %s, %s, %s, %s)"""
        params = (cliente.Nombre, cliente.Apellido, cliente.Fecha_Nacimiento, 
                  cliente.Email, cliente.Telefono)
        self.db.connect()
        cursor = self.db.connection.cursor()  # Usa un cursor aquí
        try:
            cursor.execute(query, params)
            self.db.connection.commit()
            return cursor.lastrowid  # Usa lastrowid desde el cursor
        except Error as e:
            print(f"Error al crear cliente: {e}")
            self.db.connection.rollback()
            return None
        finally:
            cursor.close()  # Cierra el cursor después de usarlo
            self.db.disconnect()

    def actualizar(self, cliente):
        query = """UPDATE Cliente SET Nombre = %s, Apellido = %s, 
                   Fecha_Nacimiento = %s, Email = %s, Telefono = %s 
                   WHERE ID_Cliente = %s"""
        params = (cliente.Nombre, cliente.Apellido, cliente.Fecha_Nacimiento,
                  cliente.Email, cliente.Telefono, cliente.ID_Cliente)
        self.db.connect()
        try:
            resultado = self.db.consultas_update_delete(query, params)
            return resultado > 0
        finally:
            self.db.disconnect()

    def eliminar(self, id_cliente):
        self.db.connect()
        try:
            # Primero, intentamos eliminar las asistencias asociadas
            query_asistencia = "DELETE FROM Asistencia WHERE ID_Cliente = %s"
            self.db.consultas_update_delete(query_asistencia, (id_cliente,))
            
            # Luego, intentamos eliminar el cliente
            query_cliente = "DELETE FROM Cliente WHERE ID_Cliente = %s"
            resultado = self.db.consultas_update_delete(query_cliente, (id_cliente,))
            
            if resultado > 0:
                self.db.connection.commit()
                return True
            else:
                self.db.connection.rollback()
                return False
        except Error as e:
            print(f"Error al eliminar cliente: {e}")
            self.db.connection.rollback()
            return False
        finally:
            self.db.disconnect()