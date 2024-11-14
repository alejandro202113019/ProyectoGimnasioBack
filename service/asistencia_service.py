from entities.asistencia import Asistencia
from repository.asistencia_repository import AsistenciaRepository

class AsistenciaService:
    def __init__(self):
        self.asistencia_repository = AsistenciaRepository()
    
    def obtener_todos(self):
        return self.asistencia_repository.obtener_todos()
    
    def obtener_por_id(self, id_asistencia):
        asistencia = self.asistencia_repository.obtener_por_id(id_asistencia)
        return asistencia if asistencia else None
    
    def crear(self, asistencia_data):
        asistencia = Asistencia.from_dict(asistencia_data)
        self.asistencia_repository.crear(asistencia)
        return "Asistencia registrada exitosamente"
    
    def actualizar(self, id_asistencia, asistencia_data):
        asistencia_existente = self.asistencia_repository.obtener_por_id(id_asistencia)
        if not asistencia_existente:
            raise Exception('Asistencia no encontrada')
        
        asistencia_data['ID_Asistencia'] = id_asistencia
        asistencia = Asistencia.from_dict(asistencia_data)
        self.asistencia_repository.actualizar(asistencia)
        return "Asistencia modificada exitosamente"
    
    def eliminar(self, id_asistencia):
        asistencia_existente = self.asistencia_repository.obtener_por_id(id_asistencia)
        if not asistencia_existente:
            raise Exception('Asistencia no encontrada')
            
        self.asistencia_repository.eliminar(id_asistencia)
        return "Asistencia eliminada exitosamente"