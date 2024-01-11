class Vehicle:
    def drive(self):
        print("Generic vehicle is being driven.")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven on the road.")

class Bicycle(Vehicle):
    def drive(self):
        print("Bicycle is being pedaled on the path.")

def main():
    generic_vehicle = Vehicle()
    car = Car()
    bicycle = Bicycle()

    generic_vehicle.drive()
    car.drive()             
    bicycle.drive()       


if __name__=="__main__":
    main()