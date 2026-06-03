from controller import Registro_controller, Usuario_controller
from views import App_view


print("=== Bienvenido al control de gastos personales ===\n")

# Seleccionamos el usuario activo (si no hay, se registra el primero)
usuario_activo = Usuario_controller.seleccionar_usuario()

# Menu principal
while True:
    match App_view.menu_principal():
        case "1. Registrar gasto":
            Registro_controller.registrar_gasto(usuario_activo.dni)
        case "2. Ver gastos":
            print("Ver gastos")
        case "3. Ver resumen por area":
            print("Ver resumen por area")

