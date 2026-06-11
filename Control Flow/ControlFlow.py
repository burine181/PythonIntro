favorite_cars = [
    {
        "make": "Tesla",
        "model": "Model S",
        "year": 2020,
        "price": 79999.99,
        "features": ["Autopilot", "Electric", "All-Wheel Drive"],
        "is_electric": True,
        "owner": None
    },
    {
        "make": "Porsche",
        "model": "911 Carrera",
        "year": 2023,
        "price": 106500.00,
        "features": ["Sport Mode", "Rear-Wheel Drive", "Turbocharged"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Audi",
        "model": "A4",
        "year": 2021,
        "price": 39999.99,
        "features": ["Quattro All-Wheel Drive", "Virtual Cockpit", "LED Headlights"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "BMW",
        "model": "3 Series",
        "year": 2022,
        "price": 45000.00,
        "features": ["xDrive All-Wheel Drive", "Heated Seats", "Navigation"],
        "is_electric": False,
        "owner": None
    }
]
favorite_cars[0] = None
for car in favorite_cars:
    try:
        if car['make'] == 'Tesla':
            print("The first item is a Tesla.")
            print(f"{car['make']} {car['model']}")
            break
        else:
            print("The current item is not a Tesla.")
    except TypeError as e:
        print("An error occurred while processing the list of cars.")
        print(f"Error details: {e}")

        car = {
            "make": "Tesla",
            "model": "Model S",
            "year": 2020,
            "price": 79999.99,
            "features": ["Autopilot", "Electric", "All-Wheel Drive"],
            "is_electric": True,
            "owner": None
        }
        if car['make'] == 'Tesla':
            print("The first item is a Tesla.")
            print(f"{car['make']} {car['model']}")
            # break
        else:
            print("The current item is not a Tesla.")
            continue
    else:
        print("Finished processing the list of cars without any errors.")
    finally:
        print("This block will always execute, regardless of any exceptions.")

# if any(car['make'] == 'Porsche' for car in favorite_cars):
#     print("Porsche found!")
#     print("Details of the Porsche:")
#     print("-" * 30)
#     for car in favorite_cars:
#         if car['make'] == 'Porsche':
#             print(f"Model: {car['model']}")
#             print(f"Year: {car['year']}")
#             print(f"Price: ${car['price']:.2f}")
#             print(f"Features: {', '.join(car['features'])}")
#             print(f"Is Electric: {'Yes' if car['is_electric'] else 'No'}")
#             print(f"Owner: {car['owner'] if car['owner'] else 'None'}")
# else:
#     print("Porsche not found.")



# if favorite_cars == []:
#     print("This list is empty.")
#     print("Please add some cars to the list.")
#     print("Thank You.")
# elif favorite_cars[0]['make'] == "Tesla":
#     print("The first item is a Tesla.")
#     print(favorite_cars[0]['make'] + " " + favorite_cars[0]['model'])
# else:
#     print("The first item is not a Tesla.")
#     print(favorite_cars[0]['make'] + " " + favorite_cars[0]['model'])

# n = 100
# if n < 50:
#     print("The number is less than 50.")
# elif n == 50:
#     print("The number is equal to 50.")
# else:
#     print("The number is greater than 50.")

# code = 200
# match code:
#     case 404:
#         print("Not found")
#     case 401:
#         print("Unauthorized - please authenticate")
#     case 403:
#         print("Forbidden - you don't have permission to access this resource")
#     case 301:
#         print("Moved Permanently - the resource has been moved to a new URL")
#     case 200:
#         print("OK - the request was successful")
#     case _:
#         print("Unknown Status Code")