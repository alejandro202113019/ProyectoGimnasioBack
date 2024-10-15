import mysql.connector
from mysql.connector import Error, pooling
from datetime import date

class Database:
    def __init__(self):
        self.host = "bdgimnasio.chcmuq64oyqj.us-east-2.rds.amazonaws.com"
        self.port = "3306"
        self.database = "BD_Gimnasio"
        self.user = "admins"
        self.password = "ProyecGym2024"
        self.pool = None

    def connect(self):
        try:
            self.pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=5,
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Pool de conexiones creado exitosamente.")
        except Error as e:
            print(f"Error al crear el pool de conexiones: {e}")

    def get_connection(self):
        return self.pool.get_connection()

    def realizar_consulta(self, query, params=None):
        connection = None
        cursor = None
        try:
            connection = self.get_connection()
            cursor = connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()

            for row in result:
                for key, value in row.items():
                    if isinstance(value, date):
                        row[key] = value.isoformat()

            return result
        except Error as e:
            print(f"Error al realizar la consulta: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def consultas_update_delete(self, query, params=None):
        connection = None
        cursor = None
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error al realizar la operación: {e}")
            if connection:
                connection.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()