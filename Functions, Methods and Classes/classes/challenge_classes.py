class Person:
    def __init__(self, f_name: str, l_name: str, age: int, height: float) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.height = height
        self.is_happy = False

    def greet(self):
        print(f"Hello, my name is {self.f_name} {self.l_name} and I am {self.age} years old.")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.f_name}! You are now {self.age} years old.")
        self.is_happy = True
        print(f"{self.f_name} is now happy")