class Vehicle:
    def __init__(self):
        self.seating_capacity = 0
    

    def calculate_rent(self):
        rent = self.seating_capacity * 100
        return rent
    

class Bike(Vehicle):
    def __init__(self):
        self.seating_capacity = 2
    

    def calculate_rent(self):
        return super().calculate_rent()
    

class Car4Seater(Vehicle):
    def __init__(self):
        self.seating_capacity = 4
    

    def calculate_rent(self):
        return super().calculate_rent()
    

class Bus(Vehicle):
    def __init__(self, seats):
        self.seating_capacity = seats
    

    def calculate_rent(self):
        rent =  (self.seating_capacity * 100) + 0.1*(self.seating_capacity * 100 )
        return rent

def main():
    bike = Bike()
    rent = bike.calculate_rent()
    print(f"Rent of bike: {rent}")

    car = Car4Seater()
    rent = car.calculate_rent()
    print(f"Rent of car : {rent}")

    seats = int(input("Enter no. of seats in bus: "))
    bus = Bus(seats)
    rent = bus.calculate_rent()
    print(f"Rent of Bus : {rent}")


main()