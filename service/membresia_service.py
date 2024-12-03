from entities.membresia import Membresia
from repository.membresia_repository import MembresiaRepository

class MembresiaService:
    def __init__(self):
        self.membresia_repository = MembresiaRepository()
    
    def obtener_todos(self):
        return self.membresia_repository.obtener_todos()
    
    def obtener_por_id(self, id_membresia):
        membresia = self.membresia_repository.obtener_por_id(id_membresia)
        return membresia if membresia else None
    
    def crear(self, membresia_data):
        membresia = Membresia.from_dict(membresia_data)
        self.membresia_repository.crear(membresia)
        return "Membresía creada exitosamente"
    
    def actualizar(self, id_membresia, membresia_data):
        membresia_existente = self.membresia_repository.obtener_por_id(id_membresia)
        if not membresia_existente:
            raise Exception('Membresía no encontrada')
        
        membresia_data['ID_Membresia'] = id_membresia
        membresia = Membresia.from_dict(membresia_data)
        self.membresia_repository.actualizar(membresia)
        return "Membresía modificada exitosamente"
    
    def eliminar(self, id_membresia):
        membresia_existente = self.membresia_repository.obtener_por_id_2(id_membresia)
        if not membresia_existente:
            raise Exception('Membresía no encontrada')
            
        self.membresia_repository.eliminar(id_membresia)
        return "Membresía eliminada exitosamente"