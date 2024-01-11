class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass 

    def behaviour(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def behaviour(self):
        return f"{self.name} is wagging its tail."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def behaviour(self):
        return f"{self.name} is purring."

def main():
    dog = Dog("Bruno", 3, "Golden Retriever")
    cat = Cat("Chippy", 2, "ginger")

    print(f"{dog.name} is a {dog.age}-year-old {dog.breed}.")
    print(f"{cat.name} is a {cat.age}-year-old {cat.color} cat.")

    print(f"{dog.name} goes {dog.make_sound()}")
    print(f"{cat.name} goes {cat.make_sound()}")

    print(dog.behaviour())  
    print(cat.behaviour())      

if __name__=="__main__":
    main()