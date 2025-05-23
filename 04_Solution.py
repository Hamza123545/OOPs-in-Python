#Encapsulation


class Car:
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
            return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size





my_tesla = ElectricCar("Tesla", "Model S", "85K Wh")
# print(my_tesla.__brand)
print(my_tesla.get_brand())





# my_car = Car("Toyyota", "Corolla")

# print(my_car.full_name())

# my_new_car = Car("Honda","Civic")
# print(my_new_car.brand)
# print(my_new_car.model)
