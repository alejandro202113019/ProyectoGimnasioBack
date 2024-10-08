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
        # Validate required fields
        required_fields = ['Nombre', 'Apellido', 'Fecha_Nacimiento', 'Email', 'Telefono']
        for field in required_fields:
            if field not in cliente_data or not cliente_data[field]:
                return None, f"El campo '{field}' es requerido y no puede estar vacío."

        nuevo_cliente = Cliente(
            Nombre=cliente_data['Nombre'],
            Apellido=cliente_data['Apellido'],
            Fecha_Nacimiento=cliente_data['Fecha_Nacimiento'],
            Email=cliente_data['Email'],
            Telefono=cliente_data['Telefono']
        )
        created_cliente_id = self.service.crear_cliente(nuevo_cliente)
        if created_cliente_id:
            return created_cliente_id, None
        return None, "No se pudo crear el cliente."

    def actualizar_cliente(self, id_cliente, cliente_data):
        cliente_existente = self.service.obtener_cliente_por_id(id_cliente)
        if not cliente_existente:
            return False
        cliente_actualizado = Cliente(
            ID_Cliente=id_cliente,
            Nombre=cliente_data.get('Nombre'),
            Apellido=cliente_data.get('Apellido'),
            Fecha_Nacimiento=cliente_data.get('Fecha_Nacimiento'),
            Email=cliente_data.get('Email'),
            Telefono=cliente_data.get('Telefono')
        )
        return self.service.actualizar_cliente(cliente_actualizado)

    def eliminar_cliente(self, id_cliente):
        return self.service.eliminar_cliente(id_cliente)