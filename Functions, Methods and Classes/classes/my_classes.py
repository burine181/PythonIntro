class Car:
    def __init__ (self, make: str, model: str, year: int, milage: int, condition: str, color: str) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.milage = milage
        self.condition = condition
        self.color = color
        self.running =  False
        self.speed = 0

    def start(self) -> None:
        if self.running:
            print(f"{self.make} {self.model} is already running.")
            return
        else:
            self.running = True
            print(f"{self.make} {self.model} has started.")

    def stop(self) -> None:
        if not self.running:
            print(f"{self.make} {self.model} is already stopped.")
            return
        else:
            self.running = False
            print(f"{self.make} {self.model} has stopped.")

    def accelerate(self, increase: int) -> None:    
        if not self.running:
            print(f"{self.make} {self.model} is not running. Please start the car first.")
            return
        else:
            self.speed += increase
            print(f"{self.make} {self.model} has accelerated to {self.speed} mph.")