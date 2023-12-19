from abc import ABC
from abc import abstractmethod


class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @abstractmethod
    def wheels_num(self) -> int:
        return 0

    def vehicle_type(self) -> str:
        return f"{self.brand_name} {self.__class__.__name__}"

    def is_motorcycle(self) -> bool:
        return self.wheels_num() == 2

    @property
    def purchase_price(self) -> float:
        price = self.base_price - 0.1 * self.mileage

        if price < 100_000:
            return 100_000

        return price


# Don't change class implementation
class Car(Vehicle):
    def wheels_num(self):
        return 4


# Don't change class implementation
class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


# Don't change class implementation
class Truck(Vehicle):
    def wheels_num(self):
        return 10


# Don't change class implementation
class Bus(Vehicle):
    def wheels_num(self):
        return 6
