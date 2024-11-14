from entities.clase import Clase
from repository.clase_repository import ClaseRepository

class ClaseService:
    def __init__(self):
        self.clase_repository = ClaseRepository()
    
    def obtener_todos(self):
        return self.clase_repository.obtener_todos()
    
    def obtener_por_id(self, id_clase):
        clase = self.clase_repository.obtener_por_id(id_clase)
        return clase if clase else None
    
    def crear(self, clase_data):
        clase = Clase.from_dict(clase_data)
        self.clase_repository.crear(clase)
        return "Clase creada exitosamente"
    
    def actualizar(self, id_clase, clase_data):
        clase_existente = self.clase_repository.obtener_por_id(id_clase)
        if not clase_existente:
            raise Exception('Clase no encontrada')
        
        clase_data['ID_Clase'] = id_clase
        clase = Clase.from_dict(clase_data)
        self.clase_repository.actualizar(clase)
        return "Clase modificada exitosamente"
    
    def eliminar(self, id_clase):
        clase_existente = self.clase_repository.obtener_por_id(id_clase)
        if not clase_existente:
            raise Exception('Clase no encontrada')
            
        self.clase_repository.eliminar(id_clase)
        return "Clase eliminada exitosamente"