"""Otra forma de hallar la distancia entre dos puntos usando poo a diferencia del archivo
    distancia.py, aqui usamos una funcion llamada distancia para calcular la distancia 
    entre dos puntos y usamos una funcion llamada main para ejecutar e imprimir la distancia 
    entre dos objetos de la clase Punto dados como p1 y p2 
"""
from math import sqrt
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distancia(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dist = sqrt(dx ** 2 + dy ** 2)
        return dist
    
def main():
    p1 = Punto(5,10)
    p2 = Punto(3,-1)
    print(f"La distancia entre los puntos (5,10) y (3,-1) es {p1.distancia(p2)}")
    
if __name__ == '__main__':
    main()