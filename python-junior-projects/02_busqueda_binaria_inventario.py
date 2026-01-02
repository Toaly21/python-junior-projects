"""Búsqueda binaria recursiva en un inventario (lista de dicts).
"""

def buscar_cantidad_producto(inventario, codigo_producto, inicio = 0, fin = None):
    if fin is None:
        fin = len(inventario)-1

    if inicio > fin:
        return 0

    medio = (inicio+fin)//2
    print(medio)

    if inventario[medio]["codigo"] == codigo_producto:
        return inventario[medio]["cantidad"]

    elif inventario[medio] ["codigo"] < codigo_producto:

        return buscar_cantidad_producto (inventario, codigo_producto, medio + 1, fin)

    else:
        return buscar_cantidad_producto(inventario,codigo_producto,inicio, medio-1)


if __name__ == "__main__":
    inventario = [
        {"codigo":101, "cantidad": 50},
        {"codigo":204, "cantidad": 30},
        {"codigo":307, "cantidad": 80},
        {"codigo":412, "cantidad": 20},
        {"codigo":515, "cantidad": 40},
    
    ]
    
    codigo_producto = 515
    
    cantidad_disponible = buscar_cantidad_producto(inventario,codigo_producto)
    print(f"Cantidad de insumos disponibles ppara el producto {codigo_producto}, es de: {cantidad_disponible}")
