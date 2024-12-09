from entities.gasto import Gasto
from repository.gasto_repository import GastoRepository

class GastoService:
    def __init__(self):
        self.gasto_repository = GastoRepository()
    
    def obtener_todos(self):
        return self.gasto_repository.obtener_todos()
    
    def obtener_por_id(self, id_gasto):
        gasto = self.gasto_repository.obtener_por_id(id_gasto)
        return gasto if gasto else None
    
    def crear(self, gasto_data):
        gasto = Gasto.from_dict(gasto_data)
        self.gasto_repository.crear(gasto)
        return "Gasto registrado exitosamente"
    
    def actualizar(self, id_gasto, gasto_data):
        gasto_existente = self.gasto_repository.obtener_por_id(id_gasto)
        if not gasto_existente:
            raise Exception('Gasto no encontrado')
        
        gasto_data['ID_Gasto'] = id_gasto
        gasto = Gasto.from_dict(gasto_data)
        self.gasto_repository.actualizar(gasto)
        return "Gasto modificado exitosamente"
    
    def eliminar(self, id_gasto):
        gasto_existente = self.gasto_repository.obtener_por_id(id_gasto)
        if not gasto_existente:
            raise Exception('Gasto no encontrado')
            
        self.gasto_repository.eliminar(id_gasto)
        return "Gasto eliminado exitosamente"
