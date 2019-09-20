class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def drink(self):
        print(f"{self.name} is drinking")

if __name__ == "__main__":
    animal = Animal("dog")
    animal.eat()