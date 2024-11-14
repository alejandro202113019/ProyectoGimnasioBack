class Asistencia:
    def __init__(self, ID_Asistencia=None, ID_Cliente=None, 
                 Fecha_Hora_Entrada=None, Fecha_Hora_Salida=None):
        self.ID_Asistencia = ID_Asistencia
        self.ID_Cliente = ID_Cliente
        self.Fecha_Hora_Entrada = Fecha_Hora_Entrada
        self.Fecha_Hora_Salida = Fecha_Hora_Salida
    
    def to_dict(self):
        return {
            'ID_Asistencia': self.ID_Asistencia,
            'ID_Cliente': self.ID_Cliente,
            'Fecha_Hora_Entrada': str(self.Fecha_Hora_Entrada),
            'Fecha_Hora_Salida': str(self.Fecha_Hora_Salida)
        }

    @staticmethod
    def from_dict(data):
        return Asistencia(
            ID_Asistencia=data.get('ID_Asistencia'),
            ID_Cliente=data.get('ID_Cliente'),
            Fecha_Hora_Entrada=data.get('Fecha_Hora_Entrada'),
            Fecha_Hora_Salida=data.get('Fecha_Hora_Salida')
        )
