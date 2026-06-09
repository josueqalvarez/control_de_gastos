from models import Areas

def estado_registro(estado = 'exitoso'):
    if estado == 'exitoso':
        print("El registro se ha realizado con éxito.")
    else:
        print("No se pudo realizar el registro.")


# Por revisar. La idea es enviarle una lista de registros ya filtrada, y solo se encargara de imprimir (obvio)
def mostrar_ultimos_gastos(gastos, cantidad= ""):
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
    
    elif cantidad and cantidad > len(gastos):
        print(
            "La cantidad de gastos es menor a lo solicitado, solo hay los siguientes:"
        )

    print(f"\nÚltimos {cantidad} gastos registrados:")

    for gasto in gastos:
        print(
            f"=> Monto: S/ {gasto['monto']} - Area: {Areas.obtener_area_por_id(gasto['area'])}"
            f"   Fecha: {gasto['periodo']}"
            f"   Notas: {gasto['notas']}"
            )
