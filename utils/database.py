#utils/database.py
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.config = {
            'host': 'bdgimnasio.chcmuq64oyqj.us-east-2.rds.amazonaws.com',
            'port': '3306',
            'database': 'BD_Gimnasio',
            'user': 'admins',
            'password': 'ProyecGym2024'
        }

    def get_connection(self):
        return mysql.connector.connect(**self.config)

    def execute_query(self, query, params=None, dictionary=False):
        connection = None
        cursor = None
        try:
            connection = self.get_connection()
            cursor = connection.cursor(dictionary=dictionary)
            cursor.execute(query, params or ())
            if query.upper().startswith('SELECT'):
                result = cursor.fetchall()
            else:
                connection.commit()
                result = cursor.rowcount
            return result
        except Error as e:
            if connection:
                connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()