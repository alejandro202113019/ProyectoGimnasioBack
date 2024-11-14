# entities/clase.py
class Clase:
    def __init__(self, ID_Clase=None, Nombre_Clase=None, ID_Instructor=None, 
                 Capacidad_Maxima=None, Duracion=None):
        self.ID_Clase = ID_Clase
        self.Nombre_Clase = Nombre_Clase
        self.ID_Instructor = ID_Instructor
        self.Capacidad_Maxima = Capacidad_Maxima
        self.Duracion = Duracion
    
    def to_dict(self):
        return {
            'ID_Clase': self.ID_Clase,
            'Nombre_Clase': self.Nombre_Clase,
            'ID_Instructor': self.ID_Instructor,
            'Capacidad_Maxima': self.Capacidad_Maxima,
            'Duracion': self.Duracion
        }

    @staticmethod
    def from_dict(data):
        return Clase(
            ID_Clase=data.get('ID_Clase'),
            Nombre_Clase=data.get('Nombre_Clase'),
            ID_Instructor=data.get('ID_Instructor'),
            Capacidad_Maxima=data.get('Capacidad_Maxima'),
            Duracion=data.get('Duracion')
        )
