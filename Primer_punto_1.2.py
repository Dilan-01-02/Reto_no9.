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
    # Función anónima lambda que calcula el perímetro de la figura recibiendo como argumentos el radio = r, la altura = a y la base = b
    perimetroFigura = (lambda radio, altura, base: 2 * base + 2 * altura + 4 * math.pi * radio) (r, a , b)
    print("El perimetro de la figura es: " +str(perimetroFigura))