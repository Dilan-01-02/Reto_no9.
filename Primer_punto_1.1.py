'''
De los retos anteriores seleccione 3 funciones y escribalas en forma de lambdas.

'''
# Reto 6 - Segundo punto 
'''
Dado la figura de la imagen, desarrolle:

- Una función matemática para calcular el área y el perimetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi
'''
# Importación de la libreria math
import math

if __name__ =="__main__":
    # Declaración e ingreso de variables
    r = float(input("Ingrese la longitud de el radio de las circunferencias: "))
    a = float(input("Ingrese la longitud de la altura del rectángulo: "))
    b = float(input("Ingrese la longitud de la base del rectángulo: "))
    # Función anónima lambda que calcula el área de la figura recibiendo como argumentos el radio = r, la altura = a y la base = b
    areaFigura = (lambda radio, altura, base: 2*(math.pi * radio**2) + base * altura) (r, a , b)
    print("El area de la figura es: " +str(areaFigura))