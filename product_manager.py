from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                return True
        return False

    def display_all_products(self):
        for product in self.products:
            print(f"Proizvod: {product.name}, Cena: {product.price}, Količina: {product.quantity}")

    def total_inventory_value(self):
        total = sum([product.price * product.quantity for product in self.products])
        print(f"Ukupna vrednost zaliha: {total} RSD")
