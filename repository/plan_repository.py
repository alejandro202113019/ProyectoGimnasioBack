# repository/plan_repository.py
from utils.database import Database

class PlanRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        query = "SELECT * FROM Plan"
        return self.db.execute_query(query, dictionary=True)

    def obtener_por_id(self, id_plan):
        query = "SELECT * FROM Plan WHERE ID_Plan = %s"
        resultados = self.db.execute_query(query, (id_plan,), dictionary=True)
        return resultados[0] if resultados else None

    def crear(self, plan):
        query = """INSERT INTO Plan (Nombre_Plan, Descripcion, Duracion, Precio)
                   VALUES (%s, %s, %s, %s)"""
        params = (plan.Nombre_Plan, plan.Descripcion, plan.Duracion, plan.Precio)
        return self.db.execute_query(query, params)

    def actualizar(self, plan):
        query = """UPDATE Plan 
                   SET Nombre_Plan = %s, Descripcion = %s, 
                       Duracion = %s, Precio = %s
                   WHERE ID_Plan = %s"""
        params = (plan.Nombre_Plan, plan.Descripcion, plan.Duracion, 
                 plan.Precio, plan.ID_Plan)
        return self.db.execute_query(query, params)

    def eliminar(self, id_plan):
        query = "DELETE FROM Plan WHERE ID_Plan = %s"
        return self.db.execute_query(query, (id_plan,))