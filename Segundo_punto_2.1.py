'''
De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

'''
# Reto 8 - Punto 6
# Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

def calculoDePotencia(*args) -> float:
    """Función con argumentos no definidos que calcula el valor de un número real x elevado a un número natural n 

    Args:
        *args: Primer parámetro.
            Tupla con los argumentos no definidos

    Returns:
        int: Retorna potencia. 

    """
    potencia = 1
    for i in range(args[0]):
        # Bucle for que calcula la potencia de un número real x elevado a un número natural n
        potencia = potencia*args[1]
    return potencia

if __name__ == "__main__":
    # Ingreso de parámetros que serán enviados como parámetros no definidos
    a = int(input("Ingrese un número natural: "))
    b = float(input("Ingrese un número real: "))
    c = int(input("Ingrese un número natural: "))
    d = float(input("Ingrese un número real: "))
    # Llamado de la función y envio de los parámetros no definidos
    print(str(b)+" ^ "+str(a)+" = "+str(calculoDePotencia(a,b)))
    print(str(d)+" ^ "+str(a)+" = "+str(calculoDePotencia(a,d)))
    print(str(b)+" ^ "+str(c)+" = "+str(calculoDePotencia(c,b)))