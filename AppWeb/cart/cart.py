class Cart:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def agregar(self, juego):
        id = str(juego.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                "id_juego": juego.id,
                "nombre": juego.nombre,
                "precio": juego.precio,
                "cantidad": 1,
                "total_parcial": juego.precio,
                "imagen": juego.imagen.url
            }

        else:
            self.cart[id]["cantidad"] += 1
            self.cart[id]["total_parcial"] += juego.precio
        
        self.guardar()
    
    def guardar(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def eliminar(self, juego):
        id = str(juego.id)

        if id in self.cart:
            del self.cart[id]
            self.guardar()

    def disminuir(self, juego):
        id = str(juego.id)
        if id in self.cart.keys():
            self.cart[id]["cantidad"] -= 1
            self.cart[id]["total_parcial"] -= 1

            if self.cart[id]["cantidad"] < 1:
                self.eliminar(juego)
            self.guardar()
    
    def limpiar(self):
        self.session["cart"] = {}
        self.session.modified = True

    def obtener_juegos_en_carrito(self):
        return sum(item["cantidad"] for item in self.cart.values())

    def obtener_total(self):
        return sum((item["precio"]) * item["cantidad"] for item in self.cart.values())