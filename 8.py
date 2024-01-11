class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

def main():
    car1 = Car("Rolls-Royce", "Phantom VIII", 2017)
    car2 = Car("Lamborghini", "Sian", 2019)
    car1.display_details()
    car2.display_details()

if __name__=="__main__":
    main()