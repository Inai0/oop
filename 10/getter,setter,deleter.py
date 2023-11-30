class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        else:
            self._radius = value

    @radius.deleter
    def radius(self):
        print("Radius is deleted")
        del self._radius

circle = Circle(5)

print(circle.radius)

circle.radius = 10
print(circle.radius)

del circle.radius
