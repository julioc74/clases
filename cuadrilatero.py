# Se crea una clase llamada Cuadrilatero de la cual heredan las clases Cuadrado, Rectangulo
# y Trapecio

class Cuadrilatero:
    def area(self):
        pass
    
class Cuadrado(Cuadrilatero):
    # EL metodo constructor se encarga de asignar variables iniciales
    # self.lado es una variable de clase osea su alcance es en toda la 
    # clase Cuadrado; mientras que lado es una variable local osea solo
    # existe dentro del metodo constructor.
    def __init__(self, lado):
        self.lado = lado
        
    def area(self, lado):
        area = lado * lado
        return area
    
class Rectangulo(Cuadrilatero):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        
    def area(self, largo, ancho):
        area = largo * ancho
        return area
    
class Trapecio(Cuadrilatero):
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        
    def area(self, base_mayor, base_menor, altura):
        area = (base_mayor + base_menor) * altura * 0.5
        return area

# Dentro de la funcion principal se crea instancias de las clases Cuadrado, Rectangulo, 
# Trapecio llamadas cuadrado, rectangulo y trapecio respectivamente, con sus respectivos
# argumentos.    
def main():
    cuadrado = Cuadrado(7)
    area_cuadrado = cuadrado.area(7)
    print(f"El area de un cuadrado de lado {7} es {area_cuadrado}") 
    
    rectangulo = Rectangulo(8,5)
    area_rectangulo = rectangulo.area(8,5)
    print(f"El area del rectangulo de largo {8} y ancho {5} es {area_rectangulo}")
    
    trapecio = Trapecio(10,4,5)
    area_trapecio = trapecio.area(10,4,5) 
    print(f"El area de un trapecio de base mayor de {10}, base menor de {4} y altura de {5} es {area_trapecio}")
 
# Verifica si el script se esta ejecutando como el programa principal (y no siendo importado
# como un modulo en otro script).
# Si el script se esta ejecutando como la funcion principal, se llama a la funcion main().     
if __name__ == "__main__":
    main()