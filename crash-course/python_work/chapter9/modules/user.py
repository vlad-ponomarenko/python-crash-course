class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age} years old")
        print(f"Country of Origin: {self.country}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges(
            ["can add post", "can delete post", "can ban user"]
        )


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_priveleges(self):
        print(f"The admin has the following privileges")
        for privilige in self.privileges:
            print(f"\t-{privilige}")


privileges = Privileges(["can add post", "can delete post", "can ban user"])

admin_1 = Admin("Alex", "Arkhipov", 31, "Russia")

# admin_1.privileges.show_priveleges()
