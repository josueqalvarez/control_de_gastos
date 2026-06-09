import sqlite3


def obtener_conexion():
    conexion = sqlite3.connect("database/gastos.db")

    cursor = conexion.cursor("PRAGMA foreign_keys = ON")

    return cursor


def cerrar_conexion(conexion):
    conexion.commit()
    conexion.close()


def realizar_consulta(sql, parametros = None):
    conexion = sqlite3.connect("database/gastos.db")
    cursor = conexion.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # Realizamos la consulta
    if parametros != None:
        # Validamos que si es un str, lo convertimos a tupla
        if isinstance(parametros, str):
            parametros = (parametros,)
            
        cursor.execute(sql, parametros)
    else:
        cursor.execute(sql)

    # Preparamos el resultado
    response = cursor.fetchall()

    if response:
        response_list = [list(fila) for fila in response]

        # Si se recibe solo 1 valor en cada registro solicitado, DEVOLVERA UNA LISTA CON TODOS LOS VALORES
        if len(response_list[0]) == 1:
            res = [res[0] for res in response_list]
        else:
            columnas = [columna[0] for columna in cursor.description]
            # Si recibimos mas de 1 valor en cada registro solicitado, convertirlo a una lista con objetos cuyos atributos sean las columnas. DEVUELVE UNA LISTA CON DICCIONARIOS (O DICT)
            res = [
                dict(zip(columnas, fila))
                for fila in response_list
            ]

    else:
        res = []

    conexion.commit()
    conexion.close()

    return res
    


def inicializar_bd():
    conexion = sqlite3.connect("database/gastos.db")

    cursor = conexion.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    # Areas
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS areas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            monto_limite REAL NOT NULL,
            monto_usado REAL DEFAULT 0
        )
            """)    

    # Subareas
    cursor.execute("""                 
        CREATE TABLE IF NOT EXISTS subareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            area INTEGER NOT NULL,
            
            FOREIGN KEY (area)
                REFERENCES areas(id)
                ON DELETE CASCADE           
        )
            """)

    # Periodo
    cursor.execute("""                 
        
        CREATE TABLE IF NOT EXISTS periodo (           
            id_periodo INTEGER PRIMARY KEY,
            anio INTEGER NOT NULL,
            mes INTEGER NOT NULL
        )

            """)

    # Usuario
    cursor.execute("""                 
            CREATE TABLE IF NOT EXISTS usuario (           
            id_dni TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            sueldo REAL NOT NULL
        )
            """)

    # Registro
    cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS registros (           
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subarea INTEGER NOT NULL,
            periodo INTEGER NOT NULL,
            dni_usuario TEXT NOT NULL,

            monto REAL NOT NULL,
            notas TEXT,

            FOREIGN KEY (subarea)
                REFERENCES subareas(id),

            FOREIGN KEY (periodo)
                REFERENCES periodo(id_periodo)
                ON DELETE RESTRICT,
            
            FOREIGN KEY (dni_usuario)
                REFERENCES usuario(id_dni)
                ON DELETE CASCADE  
            )
    """)

    conexion.commit()
    conexion.close()
