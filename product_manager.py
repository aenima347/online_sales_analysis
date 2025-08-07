from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod '{product.name}' dodat u listu.")

    def display_all_products(self):
        print("Lista svih proizvoda:")
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Ukupna vrednost zaliha: {total} RSD")
        return total