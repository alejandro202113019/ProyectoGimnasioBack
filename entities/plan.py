# entities/plan.py
class Plan:
    def __init__(self, ID_Plan=None, Nombre_Plan=None, Descripcion=None, Duracion=None, Precio=None):
        self.ID_Plan = ID_Plan
        self.Nombre_Plan = Nombre_Plan
        self.Descripcion = Descripcion
        self.Duracion = Duracion
        self.Precio = Precio
    
    def to_dict(self):
        return {
            'ID_Plan': self.ID_Plan,
            'Nombre_Plan': self.Nombre_Plan,
            'Descripcion': self.Descripcion,
            'Duracion': self.Duracion,
            'Precio': float(self.Precio) if self.Precio else None
        }

    @staticmethod
    def from_dict(data):
        return Plan(
            ID_Plan=data.get('ID_Plan'),
            Nombre_Plan=data.get('Nombre_Plan'),
            Descripcion=data.get('Descripcion'),
            Duracion=data.get('Duracion'),
            Precio=data.get('Precio')
        )