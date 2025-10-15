class User:
    def __init__(self, name: str, age: int, weight: float, height: float, gender: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender

    def show(self):
        return self.name, self.age, self.weight, self.height, self.gender


user = User("Oleksii", 20, 63, 173, "Male")