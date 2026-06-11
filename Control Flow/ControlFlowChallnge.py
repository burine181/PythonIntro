favorite_cars = [
    {
        "make": "Tesla",
        "model": "Model S",
        "year": 2022,
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
        "make": "Ford",
        "model": "Mustang",
        "year": 2022,
        "price": 27995.00,
        "features": ["Rear-Wheel Drive", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Chevrolet",
        "model": "Corvette",
        "year": 2023,
        "price": 62995.00,
        "features": ["Supercharged", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Audi",
        "model": "R8",
        "year": 2023,
        "price": 144195.00,
        "features": ["All-Wheel Drive", "V10 Engine", "Convertible"],
        "is_electric": False,
        "owner": None
    }
]
for car in favorite_cars:
    try:
        if car['price'] > 100000:
            print(f"{car['make']} {car['model']} is ${car['price']:,.2f}.")
    except KeyError as e:
        print("An error occurred while processing the list of cars.")
        print(f"Error details: {e}")
    except TypeError as e:
        print("An error occurred while processing the list of cars.")
        print(f"Error details: {e}")
    except Exception as e:
        print("An unexpected error occurred while processing the list of cars.")
        print(f"Error details: {e}")
    except BaseException as e:
        print("A critical error occurred while processing the list of cars.")
        print(f"Error details: {e}")
        