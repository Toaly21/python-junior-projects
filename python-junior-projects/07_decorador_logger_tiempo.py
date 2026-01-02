"""Decorador para medir tiempo de ejecución y manejo básico de errores.

Extraído y separado desde torrehanoi.py para portafolio.
"""

import time

def logger_con_tiempo_de_ejecucion(funcion):
  def wrapper():

    inicio=time.time()
    print(f"Invocando a la funcion '{funcion.__name__}' ...")

    try:
      resultado=funcion()
    except Exception as e:
      print(f" Se produjo un error en la funcion '{funcion.__name__}': {e}")
      raise

    fin=time.time()
    print(f"La funcion '{funcion.__name__}' ha tardado {fin-inicio} segundo en ejecutarse ")

    return resultado

  return wrapper


@logger_con_tiempo_de_ejecucion

def mi_funcion():
  fib_series=[0,1]
  for i in range(2,20):
    fib_series.append(fib_series[i-1]+fib_series[i-2])
  return fib_series


if __name__ == "__main__":
    print(mi_funcion())
