from entities.equipo import Equipo
from repository.equipo_repository import EquipoRepository

class EquipoService:
    def __init__(self):
        self.equipo_repository = EquipoRepository()
    
    def obtener_todos(self):
        return self.equipo_repository.obtener_todos()
    
    def obtener_por_id(self, id_equipo):
        equipo = self.equipo_repository.obtener_por_id(id_equipo)
        return equipo if equipo else None
    
    def crear(self, equipo_data):
        equipo = Equipo.from_dict(equipo_data)
        self.equipo_repository.crear(equipo)
        return "Equipo creado exitosamente"
    
    def actualizar(self, id_equipo, equipo_data):
        equipo_existente = self.equipo_repository.obtener_por_id(id_equipo)
        if not equipo_existente:
            raise Exception('Equipo no encontrado')
        
        equipo_data['ID_Equipo'] = id_equipo
        equipo = Equipo.from_dict(equipo_data)
        self.equipo_repository.actualizar(equipo)
        return "Equipo modificado exitosamente"
    
    def eliminar(self, id_equipo):
        equipo_existente = self.equipo_repository.obtener_por_id(id_equipo)
        if not equipo_existente:
            raise Exception('Equipo no encontrado')
            
        self.equipo_repository.eliminar(id_equipo)
        return "Equipo eliminado exitosamente"