def estado_registro(estado = 'exitoso'):
    if estado == 'exitoso':
        print("El registro se ha realizado con éxito.")
    else:
        print("No se pudo realizar el registro.")


# Por revisar. La idea es enviarle una lista de registros ya filtrada, y solo se encargara de imprimir (obvio)
def mostrar_gastos(gastos):
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
    
    print("\nÚltimos gastos registrados:")
    for gasto in gastos:
        print(f"Subarea: {gasto['subarea']}, Monto: {gasto['monto']}, Fecha: {gasto['fecha']}, Notas: {gasto['notas']}")