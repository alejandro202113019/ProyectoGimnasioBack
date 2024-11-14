from entities.plan import Plan
from repository.plan_repository import PlanRepository

class PlanService:
    def __init__(self):
        self.plan_repository = PlanRepository()
    
    def obtener_todos(self):
        planes = self.plan_repository.obtener_todos()
        # Retornamos directamente los planes ya que vienen como diccionarios de la BD
        return planes
    
    def obtener_por_id(self, id_plan):
        plan = self.plan_repository.obtener_por_id(id_plan)
        return plan if plan else None
    
    def crear(self, plan_data):
        # Convertimos los datos a un objeto Plan
        plan = Plan.from_dict(plan_data)
        self.plan_repository.crear(plan)
        return "Plan creado exitosamente"
    
    def actualizar(self, id_plan, plan_data):
        # Verificar si el plan existe
        plan_existente = self.plan_repository.obtener_por_id(id_plan)
        if not plan_existente:
            raise Exception('Plan no encontrado')
        
        # Asegurar que el ID_Plan esté en los datos
        plan_data['ID_Plan'] = id_plan
        plan = Plan.from_dict(plan_data)
        self.plan_repository.actualizar(plan)
        return "Plan modificado exitosamente"
    
    def eliminar(self, id_plan):
        # Verificar si el plan existe
        plan_existente = self.plan_repository.obtener_por_id(id_plan)
        if not plan_existente:
            raise Exception('Plan no encontrado')
            
        self.plan_repository.eliminar(id_plan)
        return "Plan eliminado exitosamente"