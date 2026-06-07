from controller import  Usuario_controller, Menu_controller
from database import conexion

conexion.inicializar_bd()

print("=== Bienvenido al control de gastos personales ===\n")

# Seleccionamos el usuario activo (si no hay, se registra el primero)
Usuario_controller.seleccionar_usuario()

# Menu principal
Menu_controller.menu_principal()

