class Producto:

    """Inicializamos la variable con None para luego en el método de
        clase descuento darle el valor deseado."""    
    
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
        if Producto.desc is None:
            return self.precio_venta
        else:
            return self.precio_venta * (1 - Producto.desc)

# precio final de venta sin descuento        
p1 = Producto(300, 500)
pventa1 = p1.precio_final()
print(f"El precio final del producto p1 es {pventa1}")
# salida El precio final del producto p1 es 500


# precio final de venta con descuento del 25%
p2 = Producto(250, 550)
desc2 = Producto.descuento(0.25)
pf2 = p2.precio_final()
print(f"El precio final del producto p2 cuyo precio de venta es {p2.precio_venta} con descuento del 25% es {pf2}")
# salida El precio final del producto p2 cuyo precio de venta es 550 con descuento del 25% es 412.5         
        