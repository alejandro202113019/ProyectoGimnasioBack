# repository/asistencia_repository.py
from utils.database import Database

class AsistenciaRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):

        query = """SELECT `ID_Asistencia`,`ID_Cliente`, CONCAT(`Nombre`,' ',`Apellido`) AS `NombreCompleto`,`FechaAsistencia`,`Hora_Entrada`,`Hora_Salida` FROM `Asistencia` JOIN `Cliente` USING (`ID_Cliente`)"""
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_cliente):
        query = """SELECT `ID_Asistencia`,`ID_Cliente`, CONCAT(`Nombre`,' ',`Apellido`) AS `NombreCompleto`,`FechaAsistencia`,`Hora_Entrada`,`Hora_Salida` FROM `Asistencia` JOIN `Cliente` USING (`ID_Cliente`) WHERE ID_CLiente = %s"""
        resultados = self.db.execute_query(query, (id_cliente,), dictionary=True)
        return resultados[0] if resultados else None

    def obtener_por_idAsistencia(self, id_asistencia):
        query = """SELECT `ID_Asistencia`,`ID_Cliente`, CONCAT(`Nombre`,' ',`Apellido`) AS `NombreCompleto`,`FechaAsistencia`,`Hora_Entrada`,`Hora_Salida` FROM `Asistencia` JOIN `Cliente` USING (`ID_Cliente`) WHERE ID_Asistencia = %s"""
        resultados = self.db.execute_query(query, (id_asistencia,), dictionary=True)
        return resultados[0] if resultados else None

    def crear(self, asistencia):
        query = """INSERT INTO `Asistencia` (`ID_Cliente`, `FechaAsistencia`, `Hora_Entrada`, `Hora_Salida`) VALUES (%s, %s, %s, %s)"""
        params = (asistencia.ID_Cliente, asistencia.FechaAsistencia, asistencia.Hora_Entrada, asistencia.Hora_Salida)
        return self.db.execute_query(query, params)

    #falta
    def actualizar(self, asistencia):
        query = """UPDATE `Asistencia` SET `Hora_Salida` = %s WHERE `ID_Asistencia` = %s"""
        params = (asistencia.Hora_Salida, asistencia.ID_Asistencia)
        return self.db.execute_query(query, params)
    

    def eliminar(self, id_asistencia):
        query = "DELETE FROM Asistencia WHERE ID_Asistencia = %s"
        return self.db.execute_query(query, (id_asistencia,))
