from entities.pago import Pago
from repository.pago_repository import PagoRepository

class PagoService:
    def __init__(self):
        self.pago_repository = PagoRepository()
    
    def obtener_todos(self):
        return self.pago_repository.obtener_todos()
    
    def obtener_por_id(self, id_pago):
        pago = self.pago_repository.obtener_por_id(id_pago)
        return pago if pago else None
    
    def crear(self, pago_data):
        pago = Pago.from_dict(pago_data)
        self.pago_repository.crear(pago)
        return "Pago registrado exitosamente"
    
    def actualizar(self, id_pago, pago_data):
        pago_existente = self.pago_repository.obtener_por_id(id_pago)
        if not pago_existente:
            raise Exception('Pago no encontrado')
        
        pago_data['ID_Pago'] = id_pago
        pago = Pago.from_dict(pago_data)
        self.pago_repository.actualizar(pago)
        return "Pago modificado exitosamente"
    
    def eliminar(self, id_pago):
        pago_existente = self.pago_repository.obtener_por_id(id_pago)
        if not pago_existente:
            raise Exception('Pago no encontrado')
            
        self.pago_repository.eliminar(id_pago)
        return "Pago eliminado exitosamente"