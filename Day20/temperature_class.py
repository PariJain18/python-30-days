class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value


t1 = Temperature(25)

print("Temperature:", t1.celsius)

t1.celsius = 30

print("New Temperature:", t1.celsius)