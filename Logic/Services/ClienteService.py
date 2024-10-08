# ClienteService.py
from Logic.Repositories.ClienteRepository import ClienteRepository

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def obtener_todos_los_clientes(self):
        return self.repository.obtener_todos()

    def obtener_cliente_por_id(self, id_cliente):
        return self.repository.obtener_por_id(id_cliente)

    def crear_cliente(self, cliente):
        return self.repository.crear(cliente)

    def actualizar_cliente(self, cliente):
        return self.repository.actualizar(cliente)

    def eliminar_cliente(self, id_cliente):
        return self.repository.eliminar(id_cliente)
