class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_priveleges(self):
        print(f"The admin has the following privileges")
        for privilige in self.privileges:
            print(f"\t-{privilige}")
