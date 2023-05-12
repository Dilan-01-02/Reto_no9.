'''
De los retos anteriores seleccione 3 funciones y escribalas en forma de lambdas.

'''
# Reto 6 - Tercer punto
'''
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
'''
if __name__ == "__main__":
    # Declaración e ingreso de variables
    N = float(input("Ingrese la cantidad de gallinas: "))
    M = float(input("Ingrese la cantidad de gallos: "))
    K = float(input("Ingrese la cantidad de pollos: "))
    # Función anónima lambda que calcula la cantidad de carne de aves en kilos para N gallinas, M gallos y K pollos (recibidos como argumentos) cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
    carne = (lambda a, b, c: a * 6 + b * 7 + c) (N, M, K)
    print("La cantidad de carne de aves es: " +str(carne))