# from functs.my_module import cube_number, greet_person
# from classes.my_classes import Car

# print(cube_number(3))
# print(greet_person("John"))

# my_car = Car(make="Ford", model="Expedition", year=2017, milage=125000, color="Black", condition="used")
# my_wife_car = Car(make="Jeep", model="Grand Cherokee", year=2022, milage=47000, color="Maroon", condition="new")

# print(my_car.__dict__)
# print(my_wife_car.__dict__)

from classes.my_classes import Car
my_car = Car(make="Ford", model="Expedition", year=2017, milage=125000, color="Black", condition="used")

my_car.start()
my_car.accelerate(20)
my_car.accelerate(30)
my_car.stop()