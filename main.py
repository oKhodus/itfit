from stats import BMI
from user import user
print("Hello, this is welcome message from itfit!")

me = BMI(*user.show())
me.represent_weight_category()