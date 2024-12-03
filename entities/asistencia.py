class Asistencia:
    def __init__(self, ID_Asistencia=None, ID_Cliente=None, 
                 FechaAsistencia=None, Hora_Entrada=None,
                 Hora_Salida=None):
        self.ID_Asistencia = ID_Asistencia
        self.ID_Cliente = ID_Cliente
        self.FechaAsistencia = FechaAsistencia
        self.Hora_Entrada = Hora_Entrada
        self.Hora_Salida = Hora_Salida
    
    def to_dict(self):
        return {
            'ID_Asistencia': self.ID_Asistencia,
            'ID_Cliente': self.ID_Cliente,
            'FechaAsistencia': str(self.FechaAsistencia),
            'Hora_Entrada': str(self.Hora_Entrada),
            'Hora_Salida': str(self.Hora_Salida)
        }

    @staticmethod
    def from_dict(data):
        return Asistencia(
            ID_Asistencia=data.get('ID_Asistencia'),
            ID_Cliente=data.get('ID_Cliente'),
            FechaAsistencia=data.get('FechaAsistencia'),
            Hora_Entrada=data.get('Hora_Entrada'),
            Hora_Salida=data.get('Hora_Salida')
        )
