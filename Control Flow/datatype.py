Drivers = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi"]

FirstCar = {
    "Make": "Toyota",
    "Model": "Corolla",
    "Year": 2020,
    "Color": "Blue",
    "TankFull": True,
    "Drivers": [Drivers[0], Drivers[1]]
}

SecondCar = {
    "Make": "Honda",
    "Model": "Civic",
    "Year": 2019,
    "Color": "Red",
    "TankFull": False,
    "Drivers": [Drivers[2], Drivers[3]]
}

ThirdCar = {
    "Make": "Ford",
    "Model": "Mustang",
    "Year": 2021,
    "Color": "Black",
    "TankFull": True,
    "Drivers": [Drivers[4], Drivers[5]]
}

FouthCar = {
    "Make": "Chevrolet",
    "Model": "Impala",
    "Year": 2018,
    "Color": "White",
    "TankFull": False,
    "Drivers": [Drivers[6], Drivers[7]]
}


ListOfCars = [FirstCar, SecondCar, ThirdCar, FouthCar]

for Car in ListOfCars:
    if Car["TankFull"] == False:
        print(f"Make: {Car['Make']}, Model: {Car['Model']}, Year: {Car['Year']}, Color: {Car['Color']}, Tank Full: {Car['TankFull']}, Drivers: {', '.join(Car['Drivers'])}")