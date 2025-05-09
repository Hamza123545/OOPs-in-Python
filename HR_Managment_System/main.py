class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"{self.name} earns {self.salary}"
    

class Developer(Employee):
    def __init__(self, name, salary, langauge):
        super().__init__(name, salary)
        self.language = langauge

    def get_details(self):
        return f"{self.name} is a {self.language} developer is earning {self.salary}"
    


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


    def get_details(self):
        return f"{self.name}  manages {self.team_size} people and earns {self.salary}"
    

emp1 = Developer("Hamza", 120000, "Python")
emp2 = Manager("Junaid", 65000, 10)


print(emp1.get_details())
print(emp2.get_details())