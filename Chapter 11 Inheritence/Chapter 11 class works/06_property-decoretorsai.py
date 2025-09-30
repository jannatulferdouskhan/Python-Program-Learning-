class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.1416 * (self._radius ** 2)

    @radius.setter
    def radius(self, value):
         if value < 0:
            self._radius = value
         else:
            print("Radius must be non-negative")

# uses 
c = Circle(float(input("Enter The value: ")))

print(c.radius)   # 5
print(c.area)     # 78.54 (area method, but used like property)

# c.radius = 10     # setter কাজ করছে
# print(c.area)     # 314.16

c.radius = -2     # setter validation দিচ্ছে
