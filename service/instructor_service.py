from entities.instructor import Instructor
from repository.instructor_repository import InstructorRepository

class InstructorService:
    def __init__(self):
        self.instructor_repository = InstructorRepository()
    
    def obtener_todos(self):
        return self.instructor_repository.obtener_todos()
    
    def obtener_por_id(self, id_instructor):
        instructor = self.instructor_repository.obtener_por_id(id_instructor)
        return instructor if instructor else None
    
    def crear(self, instructor_data):
        instructor = Instructor.from_dict(instructor_data)
        self.instructor_repository.crear(instructor)
        return "Instructor creado exitosamente"
    
    def actualizar(self, id_instructor, instructor_data):
        instructor_existente = self.instructor_repository.obtener_por_id(id_instructor)
        if not instructor_existente:
            raise Exception('Instructor no encontrado')
        
        instructor_data['ID_Instructor'] = id_instructor
        instructor = Instructor.from_dict(instructor_data)
        self.instructor_repository.actualizar(instructor)
        return "Instructor modificado exitosamente"
    
    def eliminar(self, id_instructor):
        instructor_existente = self.instructor_repository.obtener_por_id(id_instructor)
        if not instructor_existente:
            raise Exception('Instructor no encontrado')
            
        self.instructor_repository.eliminar(id_instructor)
        return "Instructor eliminado exitosamente"