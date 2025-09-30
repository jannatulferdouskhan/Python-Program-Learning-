class Animal():
    pass
class pet(Animal):
    pass
class Dog(pet):
    # @staticmethod
    def bark():
        print("Bow Bow!")
d=Dog
d.bark()
