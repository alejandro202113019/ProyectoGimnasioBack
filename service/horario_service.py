from entities.horario import Horario
from repository.horario_repository import HorarioRepository

class HorarioService:
    def __init__(self):
        self.horario_repository = HorarioRepository()
    
    def obtener_todos(self):
        return self.horario_repository.obtener_todos()
    
    def obtener_por_id(self, id_horario):
        horario = self.horario_repository.obtener_por_id(id_horario)
        return horario if horario else None
    
    def crear(self, horario_data):
        horario = Horario.from_dict(horario_data)
        self.horario_repository.crear(horario)
        return "Horario creado exitosamente"
    
    def actualizar(self, id_horario, horario_data):
        horario_existente = self.horario_repository.obtener_por_id(id_horario)
        if not horario_existente:
            raise Exception('Horario no encontrado')
        
        horario_data['ID_Horario'] = id_horario
        horario = Horario.from_dict(horario_data)
        self.horario_repository.actualizar(horario)
        return "Horario modificado exitosamente"
    
    def eliminar(self, id_horario):
        horario_existente = self.horario_repository.obtener_por_id(id_horario)
        if not horario_existente:
            raise Exception('Horario no encontrado')
            
        self.horario_repository.eliminar(id_horario)
        return "Horario eliminado exitosamente"