from datetime import datetime
import calendar
from repository.plan_repository import PlanRepository
from repository.gasto_repository import GastoRepository


class FinanzasService:
    def __init__(self):
        self.plan_repository = PlanRepository()
        self.gasto_repository = GastoRepository()

    def calcular_ingresos_totales(self):
        planes = self.plan_repository.obtener_todos()
        return sum(plan['Precio'] for plan in planes)

    def calcular_gastos_totales(self):
        gastos = self.gasto_repository.obtener_todos()
        return sum(gasto['Monto'] for gasto in gastos)

    def calcular_balance(self):
        return self.calcular_ingresos_totales() - self.calcular_gastos_totales()

    def obtener_gastos_por_mes(self):
        gastos = self.gasto_repository.obtener_todos()
        gastos_por_mes = {}

        for gasto in gastos:
            fecha = datetime.strptime(gasto['Fecha_Gasto'], '%Y-%m-%d')
            mes_anio = fecha.strftime('%Y-%m')
            if mes_anio not in gastos_por_mes:
                gastos_por_mes[mes_anio] = 0
            gastos_por_mes[mes_anio] += gasto['Monto']

        return gastos_por_mes

    def obtener_resumen_mensual(self):
        ingresos = self.calcular_ingresos_totales()
        gastos_por_mes = self.obtener_gastos_por_mes()

        resumen = []
        for mes, gastos in gastos_por_mes.items():
            resumen.append({
                "mes": mes,
                "gastos": gastos,
                "ingresos": ingresos,
                "balance": ingresos - gastos
            })
        return resumen

    def top_gastos(self, limite=5):
        gastos = self.gasto_repository.obtener_todos()
        gastos_ordenados = sorted(gastos, key=lambda x: x['Monto'], reverse=True)
        return gastos_ordenados[:limite]

    def porcentaje_gastos_vs_ingresos(self):
        ingresos = self.calcular_ingresos_totales()
        gastos = self.calcular_gastos_totales()

        if ingresos == 0:
            return None
        return round((gastos / ingresos) * 100, 2)

    def generar_informe_json(self):
        resumen_mensual = self.obtener_resumen_mensual()
        top_gastos = self.top_gastos()
        balance = self.calcular_balance()

        return {
            "resumen_mensual": resumen_mensual,
            "top_gastos": top_gastos,
            "balance": balance
        }
