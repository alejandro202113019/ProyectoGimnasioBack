# entities/pago.py
class Pago:
    def __init__(self, ID_Pago=None, ID_Membresia=None, Fecha_Pago=None, 
                 Monto=None, Metodo_Pago=None):
        self.ID_Pago = ID_Pago
        self.ID_Membresia = ID_Membresia
        self.Fecha_Pago = Fecha_Pago
        self.Monto = Monto
        self.Metodo_Pago = Metodo_Pago
    
    def to_dict(self):
        return {
            'ID_Pago': self.ID_Pago,
            'ID_Membresia': self.ID_Membresia,
            'Fecha_Pago': str(self.Fecha_Pago),
            'Monto': float(self.Monto) if self.Monto else None,
            'Metodo_Pago': self.Metodo_Pago
        }

    @staticmethod
    def from_dict(data):
        return Pago(
            ID_Pago=data.get('ID_Pago'),
            ID_Membresia=data.get('ID_Membresia'),
            Fecha_Pago=data.get('Fecha_Pago'),
            Monto=data.get('Monto'),
            Metodo_Pago=data.get('Metodo_Pago')
        )