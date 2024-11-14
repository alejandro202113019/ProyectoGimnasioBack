class Instructor:
    def __init__(self, ID_Instructor=None, Nombre=None, Apellido=None, 
                 Especialidad=None, Email=None, Telefono=None):
        self.ID_Instructor = ID_Instructor
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Especialidad = Especialidad
        self.Email = Email
        self.Telefono = Telefono
    
    def to_dict(self):
        return {
            'ID_Instructor': self.ID_Instructor,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'Especialidad': self.Especialidad,
            'Email': self.Email,
            'Telefono': self.Telefono
        }

    @staticmethod
    def from_dict(data):
        return Instructor(
            ID_Instructor=data.get('ID_Instructor'),
            Nombre=data.get('Nombre'),
            Apellido=data.get('Apellido'),
            Especialidad=data.get('Especialidad'),
            Email=data.get('Email'),
            Telefono=data.get('Telefono')
        )
