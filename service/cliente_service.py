# service/cliente_service.py
from repository.cliente_repository import ClienteRepository
from entities.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def obtener_todos_los_clientes(self):
        return self.repository.obtener_todos()

    def obtener_cliente_por_id(self, id_cliente):
        return self.repository.obtener_por_id(id_cliente)

    def crear_cliente(self, cliente_data):
        # Verificar si el ID ya existe
        if self.repository.verificar_id_existe(cliente_data.get('ID_Cliente')):
            raise Exception('El ID del cliente ya existe.')
            
        cliente = Cliente.from_dict(cliente_data)
        self.repository.crear(cliente)
        return "Cliente agregado exitosamente"

    def actualizar_cliente(self, id_cliente, cliente_data):
        if not self.repository.obtener_por_id(id_cliente):
            raise Exception('Cliente no encontrado')
            
        cliente_data['ID_Cliente'] = id_cliente
        cliente = Cliente.from_dict(cliente_data)
        self.repository.actualizar(cliente)
        return "Cliente modificado exitosamente"

    def eliminar_cliente(self, id_cliente):
        filas_afectadas = self.repository.eliminar(id_cliente)
        if filas_afectadas > 0:
            return "Cliente eliminado exitosamente."
        else:
            raise Exception("Cliente no encontrado.")