class Gasto:
    def __init__(self, ID_Gasto=None, Fecha_Gasto=None, Monto=None, Metodo_Pago=None, Descripcion=None):
        self.ID_Gasto = ID_Gasto
        self.Fecha_Gasto = Fecha_Gasto
        self.Monto = Monto
        self.Metodo_Pago = Metodo_Pago
        self.Descripcion = Descripcion

    def to_dict(self):
        return {
            'ID_Gasto': self.ID_Gasto,
            'Fecha_Gasto': str(self.Fecha_Gasto),
            'Monto': float(self.Monto) if self.Monto else None,
            'Metodo_Pago': self.Metodo_Pago,
            'Descripcion': self.Descripcion
        }

    @staticmethod
    def from_dict(data):
        return Gasto(
            ID_Gasto=data.get('ID_Gasto'),
            Fecha_Gasto=data.get('Fecha_Gasto'),
            Monto=data.get('Monto'),
            Metodo_Pago=data.get('Metodo_Pago'),
            Descripcion=data.get('Descripcion')
        )
