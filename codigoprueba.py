import random
def camaleon(num):
    suma = sum(int(d) for d in str(num))
    cond1 = (suma % 2 == 0)
    invertido = int(str(num)[::-1])
    cond2 = (invertido % 3 == 0)
    return cond1 and cond2, suma, invertido

def main():
  cantidad = int(input("Ingrese la cantidad de números a generar: "))
  numeros = [random.randint(1, 9999) for _ in range(cantidad)]
  print("Números generados:", ", ".join(map(str, numeros)))
  print("Resultados:")
  for num in numeros:
     cumple, suma, invertido = camaleon(num)
     if cumple:
         print(f"{num} -> Sí (suma={suma}, invertido={invertido})")
     else:  
         print(f"{num} -> No (suma={suma}, invertido={invertido})")

if __name__ == "__main__":
    main() 