# ClienteController.py
from Logic.Services.ClienteService import ClienteService
from Logic.Models.Cliente import Cliente

class ClienteController:
    def __init__(self):
        self.service = ClienteService()

    def obtener_todos_los_clientes(self):
        return [cliente.to_dict() for cliente in self.service.obtener_todos_los_clientes()]

    def obtener_cliente_por_id(self, id_cliente):
        cliente = self.service.obtener_cliente_por_id(id_cliente)
        return cliente.to_dict() if cliente else None

    def crear_cliente(self, cliente_data):
        nuevo_cliente = Cliente(**cliente_data)
        return self.service.crear_cliente(nuevo_cliente)

    def actualizar_cliente(self, id_cliente, cliente_data):
        cliente_data['ID_Cliente'] = id_cliente
        cliente_actualizado = Cliente(**cliente_data)
        return self.service.actualizar_cliente(cliente_actualizado)

    def eliminar_cliente(self, id_cliente):
        return self.service.eliminar_cliente(id_cliente)
