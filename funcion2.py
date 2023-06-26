# Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro
# , un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del
#  segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la
#  cadena

def reemplazarCaracteres(cadena:str,caracter_uno:str,caracter_dos:str)->int:
    """reemplaza caracteres recibidos de una cadena, buscando el primer parametro para reemplazarlo por el segundo

    Args:
        cadena (str): texto a evaluar
        caracter_uno (str): parametro a buscar
        caracter_dos (str): parametro a cambiar

    Returns:
        int: retorna la cantidad de veces que se reemplazo ese carácter  en la cadena
    """
    aux = ""
    contador = 0
    for letra in cadena:
        if letra == caracter_uno:
            aux += caracter_dos
            contador += 1
        else:
            aux += letra
    return contador

# print("La cantidad de reemplazos fue de: ",reemplazarCaracteres("pepito","t","z"))