# entities/equipo.py
class Equipo:
    def __init__(self, ID_Equipo=None, Nombre_Equipo=None, Estado=None):
        self.ID_Equipo = ID_Equipo
        self.Nombre_Equipo = Nombre_Equipo
        self.Estado = Estado
    
    def to_dict(self):
        return {
            'ID_Equipo': self.ID_Equipo,
            'Nombre_Equipo': self.Nombre_Equipo,
            'Estado': self.Estado
        }

    @staticmethod
    def from_dict(data):
        return Equipo(
            ID_Equipo=data.get('ID_Equipo'),
            Nombre_Equipo=data.get('Nombre_Equipo'),
            Estado=data.get('Estado')
        )