from InquirerPy import inquirer

def opciones(mensaje:str, arr:list):
    var = inquirer.select(
        message=mensaje,
        choices=arr
        ).execute()

    return var