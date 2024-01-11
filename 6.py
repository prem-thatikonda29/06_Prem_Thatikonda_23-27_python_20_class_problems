class Vehicle:
    def __init__(self, make,color = "White"):
        self.make = make
        self.color = color

    def display_info(self):
        print(f"Vehicle: {self.color} {self.make}")

def main():
    car1 = Vehicle("Ford")
    car2 = Vehicle("Porsche","Blue")
    car3 = Vehicle("Audi","Grey")
    car4 = Vehicle("Mercedes","Black")

    car1.display_info()  
    car2.display_info()
    car3.display_info()
    car4.display_info()


if __name__=="__main__":
    main()