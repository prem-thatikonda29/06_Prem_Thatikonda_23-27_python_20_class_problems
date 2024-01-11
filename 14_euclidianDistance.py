import math
class Euclidian:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate(self):
        self.square = (((self.x2-self.x1)**2) + ((self.y2-self.y1)**2))
        self.distance = math.sqrt(self.square)
        return self.distance


def main():
    x1 = int(input("Enter point X1: "))
    y1 = int(input("Enter point Y1: "))
    x2 = int(input("Enter point X2: "))
    y2 = int(input("Enter point Y2: "))

    calc = Euclidian(x1,y1,x2,y2)
    print(f"Euclidean distance between ({x1},{y1}) and ({x2},{y2}): {calc.calculate()}")


if __name__=="__main__":
    main()