'''
Escriba una función recursiva para calcular la operación de la potencia.

'''
import time
def potenciaRecursiva(n:int,x:float) -> float:
    if n == 0:
        return 1
    else:
        return x * potenciaRecursiva(n-1,x)

if __name__ == "__main__":
    x = float(input("Ingrese un número real: "))
    n = int(input("Ingrese un número natural: "))
    # Llamado de la función y envio de los parámetros n y x 
    pot = potenciaRecursiva(n,x)
    print(str(x)+" ^ "+str(n)+" = "+str(pot))

    start_time = time.time()
    # instrucciones sobre las cuales se quiere medir tiempo de ejecución
    end_time = time.time()

    timer = end_time - start_time
    print(timer)