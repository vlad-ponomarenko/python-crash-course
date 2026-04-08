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
    def __init__(self, first_name, last_name, age, country, privileges):
        super().__init__(first_name, last_name, age, country)
        self.privileges = privileges

    def show_priveleges(self):
        print(f"The {self.first_name} has the following privileges")
        for privilige in self.privileges:
            print(f"\t-{privilige}")


# user_1 = User("Alex", "Arkhipov", 31, "Russia")
# user_2 = User("Daniel", "Marass", 32, "Poland")

# user_1.describe_user()
# user_2.describe_user()


# user_1.increment_login_attempts()
# print(f"{user_1.first_name} login attempts: {user_1.login_attempts}")
# user_1.reset_login_attempts()
# print(f"{user_1.first_name} login attempts: {user_1.login_attempts}")


# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# print(f"{user_2.first_name} login attempts: {user_2.login_attempts}")
# user_2.reset_login_attempts()
# print(f"{user_2.first_name} login attempts: {user_2.login_attempts}")


# ["can add post", "can delete post", "can ban user"]

admin_1 = Admin(
    "Alex",
    "Arkhipov",
    31,
    "Russia",
    ["can add post", "can delete post", "can ban user"],
)

admin_1.show_priveleges()
