#Abstract Base Class (ABC) and Abstract Method

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def full_name(self):
        pass


class Car(Vehicle):
    total_cars = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Car is a vehicle that is used for transportation."


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charger"


class Battery:
    def battery_info(self):
        return "Battery info"

class Engine:
    def engine_info(self):
        return "Engine info"


class ElectricCarTwo(Battery, Engine, Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electric charger"

    def full_name(self):
        return f"{self.get_brand()} {self._Car__model}"


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
print(my_new_tesla.fuel_type())
print(my_new_tesla.full_name())
