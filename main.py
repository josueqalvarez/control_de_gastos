from controller import Registro_controller, Usuario_controller, Menu_controller
from views import App_view


print("=== Bienvenido al control de gastos personales ===\n")

# Seleccionamos el usuario activo (si no hay, se registra el primero)
usuario_activo = Usuario_controller.seleccionar_usuario()

# Menu principal
Menu_controller.menu_principal (usuario_activo)

