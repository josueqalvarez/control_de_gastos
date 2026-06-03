from datetime import datetime

class Periodo:

    bd_temporal = []

    def __init__(self):

        fecha_actual = datetime.now()
        self.año = fecha_actual.year
        self.mes = fecha_actual.month

        # Ejemplo: 202605
        self.id_periodo = int(
                f"{self.año}{self.mes:02d}"
                )
        
        if self.id_periodo not in Periodo.bd_temporal:
            Periodo.bd_temporal.append(self)