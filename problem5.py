# Q5: Vehicle Inheritance Example

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors

class SportsCar(Car):
    def __init__(self, brand, model, number_of_doors, top_speed):
        super().__init__(brand, model, number_of_doors)
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.number_of_doors}, Top Speed: {self.top_speed} km/h")

# Demo
sc = SportsCar("Ferrari", "488", 2, 330)
sc.display_info()
