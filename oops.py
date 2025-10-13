# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model, rent_per_day):
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Rental Price per Day: ₹{self.rent_per_day}")

    def calculate_rent(self, days):
        total_rent = self.rent_per_day * days
        if days > 7:
            total_rent *= 0.9  # 10% discount for rentals longer than 7 days
        return total_rent


# Derived class: Car
class Car(Vehicle):
    def __init__(self, brand, model, rent_per_day, num_doors):
        super().__init__(brand, model, rent_per_day)
        self.num_doors = num_doors

    def display_info(self):
        print("Car Details")
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


# Derived class: Bike
class Bike(Vehicle):
    def __init__(self, brand, model, rent_per_day, engine_cc):
        super().__init__(brand, model, rent_per_day)
        self.engine_cc = engine_cc

    def display_info(self):
        print("Bike Details")
        super().display_info()
        print(f"Engine Capacity: {self.engine_cc} cc")


# ---- Test the program ----
car1 = Car("Toyota", "Camry", 2000, 4)
bike1 = Bike("Yamaha", "R15", 800, 150)

car1.display_info()
print(f"Total Rent for 10 Days: ₹{int(car1.calculate_rent(10))}")
print()

bike1.display_info()
print(f"Total Rent for 5 Days: ₹{int(bike1.calculate_rent(5))}")