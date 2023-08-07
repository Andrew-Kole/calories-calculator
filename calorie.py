from temperature import Temperature


class Calorie:
    """
    Represents amount of calculated calories
    formula: 10 * weight + 6.5 * height - 10 * actual temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        """Calculation of calorie amount"""
        if self.temperature is not None:
            result = 10 * self.weight + 6.5 * self.height - self.temperature * 10
            return result
        else:
            return None


if __name__ == '__main__':
    temperature = Temperature(country='USA', city='Los Angeles').get_temperature()
    calorie = Calorie(temperature=temperature, weight=60, height=174, age=32)
    print(calorie.calculate())
