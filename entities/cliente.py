class Cliente:
    def __init__(self, ID_Cliente=None, Nombre=None, Apellido=None, Fecha_Nacimiento=None, Email=None, Telefono=None):
        self.ID_Cliente = ID_Cliente
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Fecha_Nacimiento = Fecha_Nacimiento
        self.Email = Email
        self.Telefono = Telefono
    
    def to_dict(self):
        return {
            'ID_Cliente': self.ID_Cliente,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'Fecha_Nacimiento': str(self.Fecha_Nacimiento),
            'Email': self.Email,
            'Telefono': self.Telefono
        }

    @staticmethod
    def from_dict(data):
        return Cliente(
            ID_Cliente=data.get('ID_Cliente'),
            Nombre=data.get('Nombre'),
            Apellido=data.get('Apellido'),
            Fecha_Nacimiento=data.get('Fecha_Nacimiento'),
            Email=data.get('Email'),
            Telefono=data.get('Telefono')
        )