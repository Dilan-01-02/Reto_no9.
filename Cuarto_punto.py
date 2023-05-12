import time

def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2) 

def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  sumFibo = n2 
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo 

def tiempoIterativo():
  for i in range (1000):
    start_time1 = time.time()
    fibo(i)
    end_time1 = time.time()
    timer1 = end_time1 - start_time1
    
    start_time2 = time.time()
    fiboRecursivo(i)
    end_time2 = time.time()
    timer2 = end_time2 - start_time2
    
    if timer2 - timer1 > 1:
      print("Desde el número "+str(i)+" La diferencia temporal entre la función iterativa y la recursiva se vuelve significativa ("+str(timer2-timer1)+")")
      break

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
  tiempoIterativo()

  