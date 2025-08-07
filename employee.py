class Employee:
    def __init__(self, id, name, position):
        self.id = id
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} - {self.position}"