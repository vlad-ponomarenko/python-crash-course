from user import User
from privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges(
            ["can add post", "can delete post", "can ban user"]
        )
