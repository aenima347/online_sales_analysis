from product import Product
from product_manager import ProductManager
from user import User
from user_manager import UserManager
from employee import Employee
from employee_manager import EmployeeManager

# Inicijalizacija menadžera
product_manager = ProductManager()
user_manager = UserManager()
employee_manager = EmployeeManager()

# Dodavanje proizvoda
p1 = Product(1, "Laptop", 1200)
p2 = Product(2, "Monitor", 300)
product_manager.add_product(p1)
product_manager.add_product(p2)

# Dodavanje korisnika
u1 = User(1, "Ana", "ana@example.com")
u2 = User(2, "Milan", "milan@example.com")
user_manager.add_user(u1)
user_manager.add_user(u2)

# Dodavanje zaposlenih
e1 = Employee(1, "Petar", "Prodaja")
e2 = Employee(2, "Ivana", "Podrška")
employee_manager.add_employee(e1)
employee_manager.add_employee(e2)

# Ispis svih podataka
print("Proizvodi:")
for p in product_manager.products:
    print(f"{p.name} - {p.price} EUR")

print("\nKorisnici:")
for u in user_manager.users:
    print(f"{u.name} - {u.email}")

print("\nZaposleni:")
for e in employee_manager.employees:
    print(f"{e.name} - {e.position}")
