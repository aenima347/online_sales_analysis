from product import Product
from product_manager import ProductManager

# Kreiramo ProductManager
manager = ProductManager()

# Dodajemo proizvode
p1 = Product("Laptop", 70000, 5)
p2 = Product("Miš", 1500, 10)
p3 = Product("Tastatura", 3500, 7)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz svih proizvoda
manager.display_all_products()

# Ukupna vrednost zaliha
manager.total_inventory_value()