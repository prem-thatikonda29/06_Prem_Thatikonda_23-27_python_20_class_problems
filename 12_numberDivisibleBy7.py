class Generator:
    def __init__(self):
        self.numbers = []

    def iterate(self, number):
        for i in range(number+1):
            # d = i % 10
            # n = i // 10
            if i % 7 == 0:
                self.numbers.append(i)
        return self.numbers

def main():
    gen = Generator()
    print("Divisibility by 7 checker")
    num = int(input("Enter limit: "))
    print(gen.iterate(num))


if __name__=="__main__":
    main()