# Solution 01 Basic Class and Object
# Question 1: Create a class called Car with attributes brand and model. Create an instance of the Car class and print its attributes.

# Solution:

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model


my_car = Car("Toyyota","Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Honda","Civic")
print(my_new_car.brand)
print(my_new_car.model)