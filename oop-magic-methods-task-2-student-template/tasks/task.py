class Bird:
    def __init__(self, name: str):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"

    def fly(self):
        return f"{self.name} bird can fly"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str ="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"


class NonFlyingBird(FlyingBird):
    def __init__(self, name: str, ration: str = "fish"):
        super().__init__(name, ration)

    def swim(self):
        return f"{self.name} bird can swim"

    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird):
    def __init__(self, name: str, ration: str = "fish"):
        super().__init__(name, ration)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"
