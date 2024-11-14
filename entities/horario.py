class Horario:
    def __init__(self, ID_Horario=None, ID_Clase=None, Dia_Semana=None, 
                 Hora_Inicio=None, Hora_Fin=None):
        self.ID_Horario = ID_Horario
        self.ID_Clase = ID_Clase
        self.Dia_Semana = Dia_Semana
        self.Hora_Inicio = Hora_Inicio
        self.Hora_Fin = Hora_Fin
    
    def to_dict(self):
        return {
            'ID_Horario': self.ID_Horario,
            'ID_Clase': self.ID_Clase,
            'Dia_Semana': self.Dia_Semana,
            'Hora_Inicio': str(self.Hora_Inicio),
            'Hora_Fin': str(self.Hora_Fin)
        }

    @staticmethod
    def from_dict(data):
        return Horario(
            ID_Horario=data.get('ID_Horario'),
            ID_Clase=data.get('ID_Clase'),
            Dia_Semana=data.get('Dia_Semana'),
            Hora_Inicio=data.get('Hora_Inicio'),
            Hora_Fin=data.get('Hora_Fin')
        )