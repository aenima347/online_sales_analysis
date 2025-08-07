class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return self.employees
        def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                return True
        return False
