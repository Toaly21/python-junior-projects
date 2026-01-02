"""Ordenamiento y agrupación de empleados por país (sorted + groupby).
"""

from itertools import groupby

def ordenar_empleados(empleados,):
    empleados_ordenados = sorted(empleados,key=lambda emp: (emp["rendimiento"], -emp["edad"]), reverse=True)
    return empleados_ordenados

def agrupar_empleados_por_pais(empleados_ordenados):
    empleados_agrupados = {pais: list(grupo_empleados) for pais, grupo_empleados in groupby(empleados_ordenados,key=lambda emp:emp["pais"])}
    return empleados_agrupados

def mostrar_empleados_agrupados(empleados_agrupados):
    for pais, grupo_empleados in empleados_agrupados.items():
        print(f"\nPais: {pais}")
        for empleado in grupo_empleados:
            print(empleado)


if __name__ == "__main__":
    empleados = [
        {"nombre": "Juan Pérez", "edad": 30, "pais": "España", "rendimiento": 90},
        {"nombre": "María García", "edad": 28, "pais": "España", "rendimiento": 85},
        {"nombre": "Pedro Rodríguez", "edad": 26, "pais": "Argentina", "rendimiento": 95},
        {"nombre": "Ana Rodríguez", "edad": 32, "pais": "Argentina", "rendimiento": 105},
        {"nombre": "Sofía Gómez", "edad": 29, "pais": "Argentina", "rendimiento": 95},
        {"nombre": "José López", "edad": 32, "pais": "Bolivia", "rendimiento": 80},
        {"nombre": "Ana Sánchez", "edad": 35, "pais": "Bolivia", "rendimiento": 85},
    
    ]
    
    empledos_ordenados = ordenar_empleados(empleados)
    empleados_agrupados = agrupar_empleados_por_pais(empledos_ordenados)
    mostrar_empleados_agrupados(empleados_agrupados)
