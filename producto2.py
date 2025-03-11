class Producto:
    
    desc = None
    
    def __init__(self, precio_compra, precio_venta):
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        
    @classmethod
    def descuento(cls, desc):
        cls.desc = desc
        return cls.desc
   
    """Si no hay herencia de clases con solo usar Producto.desc es suficiente;
    en cambio con herencia se debe usar self.__class__.desc porque se adapta a las subclases""" 
    def precio_final(self):
        if self.__class__.desc is None:
            return self.precio_venta 
        else:
            return self.precio_venta * (1 - self.__class__.desc)

# Suponiendo que un producto que por ser fino o de lujo no tiene descuento y tiene un impuesto del 25%        
class ProductoFino(Producto):
    
    def __init__(self, precio_compra, precio_venta, impuesto):
        super().__init__(precio_compra, precio_venta)
        self.impuesto = impuesto
        
# al asignar self.__class__.desc = 0, nos aseguramos de que los productos finos nunca tengan descuento.        
    def precio_final(self):
        self.__class__.desc = 0
        return super().precio_final()*(1 + self.impuesto)


# verifica si el código se está ejecutando directamente o se está usando como módulo. 
if __name__ == '__main__':

    p1 = Producto(300, 600)
    print(p1.precio_final())

    p2 = Producto(200, 500)
    d2 = Producto.descuento(0.25)
    pf2 = p2.precio_final()
    print(pf2)

    p3 = ProductoFino(1200, 1800, 0.25).precio_final()
    print(p3)

# salida
"""600
   375.0
   2250.0"""             
            
