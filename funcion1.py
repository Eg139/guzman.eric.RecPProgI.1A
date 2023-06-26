# Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto 
# y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(precio: int)->int:
    """aplica un aumento del 5% a el precio dado

    Args:
        precio (int): valor al cual se le aplicara el aumento

    Returns:
        int: precio con el aumento aplicado
    """
    precio_aumento = precio + precio * 5 / 100
    return precio_aumento

# print(aplicarAumento(1000))