# entities/membresia.py
class Membresia:
    def __init__(self, ID_Membresia=None, ID_Cliente=None, ID_Plan=None, 
                 Fecha_Inicio=None, Fecha_Fin=None, Estado=None):
        self.ID_Membresia = ID_Membresia
        self.ID_Cliente = ID_Cliente
        self.ID_Plan = ID_Plan
        self.Fecha_Inicio = Fecha_Inicio
        self.Fecha_Fin = Fecha_Fin
        self.Estado = Estado
    
    def to_dict(self):
        return {
            'ID_Membresia': self.ID_Membresia,
            'ID_Cliente': self.ID_Cliente,
            'ID_Plan': self.ID_Plan,
            'Fecha_Inicio': str(self.Fecha_Inicio),
            'Fecha_Fin': str(self.Fecha_Fin),
            'Estado': self.Estado
        }

    @staticmethod
    def from_dict(data):
        return Membresia(
            ID_Membresia=data.get('ID_Membresia'),
            ID_Cliente=data.get('ID_Cliente'),
            ID_Plan=data.get('ID_Plan'),
            Fecha_Inicio=data.get('Fecha_Inicio'),
            Fecha_Fin=data.get('Fecha_Fin'),
            Estado=data.get('Estado')
        )