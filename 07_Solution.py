# Static Method


class Car:
    total_cars = 0
    
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1

    def get_brand(self):
            return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petro or Diesel"
    @staticmethod
    def general_description():
        return "car is a vehicle that is used for transportation."
    

class ElectricCar(Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charger"



# my_tesla = ElectricCar("Tesla", "Model S", "85K Wh")
# # print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())


honda = Car("Honda", "Civic")
print(honda.fuel_type())


print(Car.general_description())
print(honda.general_description())


# my_car = Car("Toyyota", "Corolla")

# print(my_car.full_name())

# my_new_car = Car("Honda","Civic")
# print(my_new_car.brand)
# print(my_new_car.model)
