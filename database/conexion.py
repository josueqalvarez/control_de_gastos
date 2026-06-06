import sqlite3

def obtener_conexion():
    conexion = sqlite3.connect("database/gastos.db")
    
    cursor = conexion.cursor(
        "PRAGMA foreign_keys = ON"
    )

    return cursor

def cerrar_conexion(conexion):
    conexion.commit()
    conexion.close()



def inicializar_bd():
    conexion = sqlite3.connect("database/gastos.db")

    cursor = conexion.cursor(
        "PRAGMA foreign_keys = ON"
    )

    cursor.execute(
            """

        CREATE TABLE IF NOT EXISTS areas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            monto_limite REAL NOT NULL,
            monto_usado REAL DEFAULT 0
        )
            """)
        
    cursor.execute(
            """                 
        CREATE TABLE IF NOT EXISTS subareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            area INTEGER NOT NULL,
            
            FOREIGN KEY (area)
                REFERENCES areas(id)
                ON DELETE CASCADE           
        )
            """)

    cursor.execute(
            """                 
        
        CREATE TABLE IF NOT EXISTS periodo (           
            id_periodo INTEGER PRIMARY KEY,
            anio INTEGER NOT NULL,
            mes INTEGER NOT NULL
        )

            """)
        
    cursor.execute(
            """                 
            CREATE TABLE IF NOT EXISTS usuario (           
            id_dni TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            sueldo REAL NOT NULL
        )
            """)

    cursor.execute(
            """ 
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