from flask import Blueprint, jsonify, request
from service.finanzas_service import FinanzasService

finanzas_bp = Blueprint('finanzas', __name__)
finanzas_service = FinanzasService()


@finanzas_bp.route('/ingresos', methods=['GET'])
def obtener_ingresos_totales():
    ingresos_totales = finanzas_service.calcular_ingresos_totales()
    return jsonify({"ingresos_totales": ingresos_totales})


@finanzas_bp.route('/gastosTotales', methods=['GET'])
def obtener_gastos_totales():
    gastos_totales = finanzas_service.calcular_gastos_totales()
    return jsonify({"gastos_totales": gastos_totales})


@finanzas_bp.route('/balance', methods=['GET'])
def obtener_balance():
    balance = finanzas_service.calcular_balance()
    return jsonify({"balance": balance})


@finanzas_bp.route('/gastosTotales/mes', methods=['GET'])
def obtener_gastos_por_mes():
    gastos_por_mes = finanzas_service.obtener_gastos_por_mes()
    return jsonify(gastos_por_mes)


@finanzas_bp.route('/resumen-mensual', methods=['GET'])
def obtener_resumen_mensual():
    resumen = finanzas_service.obtener_resumen_mensual()
    return jsonify(resumen)


@finanzas_bp.route('/top-gastos', methods=['GET'])
def obtener_top_gastos():
    limite = request.args.get('limite', default=5, type=int)
    top_gastos = finanzas_service.top_gastos(limite)
    return jsonify(top_gastos)


@finanzas_bp.route('/porcentaje-gastos', methods=['GET'])
def obtener_porcentaje_gastos():
    porcentaje = finanzas_service.porcentaje_gastos_vs_ingresos()
    return jsonify({"porcentaje_gastos_vs_ingresos": porcentaje})


@finanzas_bp.route('/informe', methods=['GET'])
def generar_informe():
    informe = finanzas_service.generar_informe_json()
    return jsonify(informe)
