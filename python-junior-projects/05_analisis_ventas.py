"""Filtrado y análisis de ventas con fechas (datetime) y promedios por ubicación.
"""

from datetime import datetime

def analizar_ventas(ventas):

    ventas_filtradas = [venta for venta in ventas if datetime.strptime(venta["fecha_venta"], "%Y-%m-%d").month>=10]

    ventas_filtradas = [venta for venta in ventas_filtradas if venta["monto"]>500]

    ventas_agrupadas = {}

    for venta in ventas_filtradas:
        ubicacion =venta["ubicacion"]
        if ubicacion not in ventas_agrupadas:
            ventas_agrupadas[ubicacion]=[]
        ventas_agrupadas[ubicacion].append(venta)


    promedio_ventas =  {}
    for ubicacion in ventas_agrupadas:
        ventas_por_ubicacion = ventas_agrupadas[ubicacion]
        promedio_ventas[ubicacion]=sum(venta["monto"] for venta in ventas_por_ubicacion) /len(ventas_por_ubicacion)

    ubicaciones_ordenadas = sorted(promedio_ventas,key=lambda ubicacion:promedio_ventas[ubicacion],reverse=True)

    for ubicacion in ubicaciones_ordenadas:
        print(f"{ubicacion}: ${promedio_ventas[ubicacion]}")


if __name__ == "__main__":
    ventas = [
        {"nombre_producto": "iPhone 13", "fecha_venta": "2023-10-01", "monto": 1000, "ubicacion": "Ecuador"},
        {"nombre_producto": "MacBook Pro", "fecha_venta": "2023-11-01", "monto": 2000, "ubicacion": "Argentina"},
        {"nombre_producto": "MacBook Pro 4", "fecha_venta": "2023-12-01", "monto": 3000, "ubicacion": "Argentina"},
        {"nombre_producto": "Samsung Galaxy S22", "fecha_venta": "2023-12-01", "monto": 500, "ubicacion": "Bolivia"},
        {"nombre_producto": "Samsung Galaxy S12", "fecha_venta": "2024-01-12", "monto": 300, "ubicacion": "Chile"},
    ]
    
    analizar_ventas(ventas)
