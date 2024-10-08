import mysql.connector
from mysql.connector import Error
from datetime import date

class Database:
    def __init__(self):
        self.host = "bdgimnasio.chcmuq64oyqj.us-east-2.rds.amazonaws.com"
        self.port = "3306"
        self.database = "BD_Gimnasio"
        self.user = "admins"
        self.password = "ProyecGym2024"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def realizar_consulta(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
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
            cursor.close()

    def consultas_update_delete(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error al realizar la operación: {e}")
            self.connection.rollback()
            return 0
        finally:
            cursor.close()
