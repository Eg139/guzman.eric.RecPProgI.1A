# Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y
#  su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenarCaracteres(cadena:str)->str:
    """ordenar los caracteres de manera ascendente dentro de la cadena.

    Args:
        cadena (str): Cadena que debe ordenarze ascendentemente

    Returns:
        str: cadena ordenada
    """
    aux_cadena = list(cadena)
    retorno = ""

    for i in range(len(aux_cadena)):
        for j in range(i+1, len(aux_cadena)):
            if aux_cadena[i] > aux_cadena[j]:
                aux = aux_cadena[j]
                aux_cadena[j] = aux_cadena[i]
                aux_cadena[i] = aux

    for letra in aux_cadena:
        retorno += letra

    return retorno



# print(ordenarCaracteres("algoritmo"))
