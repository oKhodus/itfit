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

    def __init__(self, name: str, age: int, weight: float, height: float, gender: str):
        super().__init__(name, age, weight, height, gender)

    def calc_BMI(self):
        recalc_height = self.height / 100
        h2 = recalc_height * recalc_height
        BMIRES = round(self.weight / h2, 2)
        return BMIRES

    def define_Wcategory(self):
        BMIRES = self.calc_BMI()
        
        weight_category = {
            (18.5, 25): "Normal",
            (25, 30): "Overweight",
            (30, 35): "Obese: Class I",
            (35, 40): "Obese: Class II",
            (40, 100): "Obese: Class III"
        }
        for key in weight_category:
            if BMIRES >= key[0] and BMIRES < key[1]:
                WC = weight_category[key]
                template_text = f"Your BMI is: {BMIRES}\nYour weight category is: {WC}"
                return print(template_text)
            else:
                template_text = f"Your BMI is: {BMIRES}\nYour weight category is: Underweight"
                return print(template_text)

me = BMI("Oleksii", 20, 63, 173, "Male")
me.define_Wcategory()
