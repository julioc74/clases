# importamos la libreria math
import math

# Se crea la clase Punto
class Punto:
    
    """ El metodo __init__ inicializa las coordenadas del punto
    se asigna la variable local x a la variable de instancia self.x 
    se asigna la variable local y a la variable de instancia self.y"""   
    def __init__(self, x, y):
        self.x = x  
        self.y = y

# El método __float__ calcula la distancia euclidiana entre dos puntos.
# La variable 'other' es otro objeto de la clase Punto.        
    def __float__(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distancia =   math.sqrt(dx ** 2 + dy ** 2)
        return distancia

    """ Verifica si el script se esta ejecutando como el programa principal 
    (y no siendo importado como un modulo en otro script). Se crea dos 
    instancias de la clase Punto (p1 y p2) y se calcula la distancia
    entre p1 y p2 mediante la funcion __float__"""    
if __name__ == '__main__':
    p1 = Punto(4, 7)
    p2 = Punto(-3, 12)
    
    print(f"La distancia entre p1 y p2 es {p1.__float__(p2)}")
    