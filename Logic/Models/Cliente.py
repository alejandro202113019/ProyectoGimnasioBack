# Cliente.py
class Cliente:
    def __init__(self, ID_Cliente=None, Nombre=None, Apellido=None, Fecha_Nacimiento=None, Email=None, Telefono=None):
        self.id_cliente = ID_Cliente
        self.nombre = Nombre
        self.apellido = Apellido
        self.fecha_nacimiento = Fecha_Nacimiento
        self.email = Email
        self.telefono = Telefono

    def to_dict(self):
        return {
            'ID_Cliente': self.id_cliente,
            'Nombre': self.nombre,
            'Apellido': self.apellido,
            'Fecha_Nacimiento': str(self.fecha_nacimiento),
            'Email': self.email,
            'Telefono': self.telefono
        }
