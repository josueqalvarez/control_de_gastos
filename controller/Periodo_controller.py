from models import utilities, Periodo

def definir_periodo_actual():

    periodo_diario = Periodo.Periodo()

    # Siesuqe no existe el periodo, se agrega.
    if not Periodo.obtener_periodo_por_id(periodo_diario.id_periodo):
        Periodo.agregar_periodo(periodo_diario.id_periodo, periodo_diario.año, periodo_diario.mes)

    utilities.periodo_actual_id = periodo_diario.id_periodo
