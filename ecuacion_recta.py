
# Programa que calcula la ecuacion de una recta dada dos puntos como datos
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    """ Recordemos que lo que devuelve una funcion con return de varios valores a la vez,
        es una tupla con dichos valores; en nuestro caso nos devolvera una tupla con 
        los valores m y b"""        
    def ec_recta(self, other):
        dy = self.y - other.y
        dx = self.x - other.x
        if dx != 0:
            m = dy/dx
        
            b = self.y - m * self.x
        
            return m,b
        else:
            print(f"la ecuacion de la recta es x = {self.x}")
    
    """Donde p1.ec_recta(p2)[0] nos devolvera el primer elemento de la tupla en este caso
        el valor de 'm' obtenido de los puntos p1 y p2 y p1.ec_recta(p2)[1] nos devolvera
        el segundo elemento de la tupla osea 'b' obtenido de los puntos p1 y p2"""
    
if __name__ == '__main__':
    p1 = Punto(4,1)
    p2 = Punto(12,10)
    print("La ecuacion de la recta que pasa por los puntos (4,1) y (12,10) es:")
    print(f" y = {p1.ec_recta(p2)[0]}x + {p1.ec_recta(p2)[1]} ")
    
    p3 = Punto(5,2)
    p4 = Punto(9,2)
    print("La ecuacion de la recta que pasa por los puntos (5,2) y (9,2) es:")
    print(f" y = {p3.ec_recta(p4)[0]}x + {p3.ec_recta(p4)[1]} ")
    
    p5 = Punto(8, -10)
    p6 = Punto(-12,5)
    print("La ecuacion de la recta que pasa por los puntos (8,-10) y (-12,5) es:")
    print(f" y = {p5.ec_recta(p6)[0]}x + {p5.ec_recta(p6)[1]} ")
    
    p7 = Punto(7,8)
    p8 = Punto(7,-3)
    print("La ecuacion de la recta que pasa por los puntos (7,8) y (7,-3) es:")
    print(f"{p7.ec_recta(p8)}")
   