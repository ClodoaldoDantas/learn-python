class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")


car = Car("Honda", "Fit", 2015)
car2 = Car("Ford", "Ka", 2010)

car.display_info()
car2.display_info()
