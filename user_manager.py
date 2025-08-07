from user import User

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return True
        return False

    def display_all_users(self):
        for user in self.users:
            print(f"Korisnik: {user.name}, Email: {user.email}")
