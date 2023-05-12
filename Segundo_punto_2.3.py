'''
De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

'''
# Reto 5 - Punto 6
# Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo. 

def triangulo(*args):
    """Función con argumentos no definidos que determina si las longitudes x, y, z se puede construir un triángulo.
    Args:
        *args: Primer parámetro.
            Tupla con los argumentos no definidos

    """
    if x<0 or y<0 or z<0:
        print("Las longitudes no pueden ser negativas")
    else:
        if (x>y-z and x<y+z) and (y>x-z and y<x+z) and (z>y-x and z<y+x):
            print("Con las longitudes ingresadas es posible construir un triángulo")
        else: 
            print("Con las longitudes ingresadas no es posible construir un triángulo") 

if __name__ == "__main__":
    # Ingreso de parámetros
    x = float(input("Ingrese la primera longitud: "))
    y = float(input("Ingrese la segunda longitud: "))
    z = float(input("Ingrese la tercera longitud: "))
    # Llamado de la función triangulo y envío de parámetros 
    triangulo(x,y,z)