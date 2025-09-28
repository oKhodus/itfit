# import typing
class User:
    def __init__(self, name: str, age: int, weight: float, height: float, gender: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender


class BMI(User):
    """
    BMI = weight / (height * height) ≈ res kg/m^2
    """

    def __init__(self, name, age, weight, height, gender):
        super().__init__(name, age, weight, height, gender)

    def calc(self):
        recalc_height = self.height / 100
        h2 = recalc_height * recalc_height
        result = round(self.weight / h2, 2)
        return print(result)


me = BMI("Oleksii", 20, 62, 173, "Male")
me.calc()
