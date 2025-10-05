from user import User

class BMI(User):
    """
    BMI = weight / (height * height) ≈ res kg/m^2
    """

    def __init__(self, name: str, age: int, weight: float, height: float, gender: str):
        super().__init__(name, age, weight, height, gender)

    def calc_BMI(self):
        squared_height = pow((self.height / 100), 2)
        return round(self.weight / squared_height, 2)

    def define_weight_category(self):
        BMIRES = self.calc_BMI()

        weight_category = {
            (18.5, 25): "Normal",
            (25, 30): "Overweight",
            (30, 35): "Obese: Class I",
            (35, 40): "Obese: Class II",
            (40, 100): "Obese: Class III",
        }
        for key in weight_category:
            return (
                weight_category[key]
                if BMIRES >= key[0] and BMIRES < key[1]
                else "Underweight"
            )

    def represent_weight_category(self):
        BMIRES = self.calc_BMI()
        WC = self.define_weight_category()
        print(f"Your BMI is: {BMIRES}\nYour weight category is: {WC}")