


class Celsius:
    """https://www.programiz.com/python-programming/property"""

    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value:")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError('Температура не может быть ниже 273 градусов')
        print("Setting value:")
        self._temperature = value


t = Celsius(37)
print(t.temperature)
t.temperature = 40
print(t.temperature)
