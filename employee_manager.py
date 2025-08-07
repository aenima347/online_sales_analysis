from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                return True
        return False

    def display_all_employees(self):
        for employee in self.employees:
            print(f"Zaposleni: {employee.name}, Pozicija: {employee.position}")
