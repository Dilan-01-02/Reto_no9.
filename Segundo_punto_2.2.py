'''
De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

'''
# Reto 6 - Punto 5
# Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

# Función para realizar el cálculo del interés compuesto
def interesCompuesto(*args) ->float:
    """Función con argumentos no definidos que calcula el valor de un préstamo C usando interés compuesto del i por n meses.

    Args:
        *args: Primer parámetro.
            Tupla con los argumentos no definidos

    Returns:
        float: Retorna Vf. 

    """
    Vf = args[0] * (1 + (args[1]/100)) ** args[2]
    return Vf

# Función principal
if __name__ == "__main__":

    # Declaración e ingreso de variables 
    c1 = float(input("Ingrese la cantidad del prestamo 1: "))
    i1 = float(input("Ingrese el porcentaje (%) de tasa de interes del prestamo 1: "))
    n1 = int(input("Ingrese el número de meses del prestamo 1: "))
    print("===================================")
    c2 = float(input("Ingrese la cantidad del prestamo 2: "))
    i2 = float(input("Ingrese el porcentaje (%) de tasa de interes del prestamo 2: "))
    n2 = int(input("Ingrese el número de meses del prestamo 2: "))

    # Llamado de la función  e impresión del resultado
    print("El valor final del prestamo "+str(c1)+" usando un interés compuesto del "+str(i1)+" % por "+str(n1)+ " meses es de: "+str(interesCompuesto(c1,i1,n1)))
    print("El valor final del prestamo "+str(c2)+" usando un interés compuesto del "+str(i2)+" % por "+str(n2)+ " meses es de: "+str(interesCompuesto(c2,i2,n2)))
