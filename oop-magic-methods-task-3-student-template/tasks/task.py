from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    currency_dct = {
        "EUR": {
            "USD": 2,
            "GBP": 100,
            "EUR": 1
        },
        "USD": {
            "EUR": 0.5,
            "GBP": 50,
            "USD": 1
        },
        "GBP": {
            "USD": 0.02,
            "EUR": 0.01,
            "GBP": 1
        }
    }

    def __init__(self, value: float):
        self.value = float(value)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        currency_to = other_cls.symbol
        currency_for = cls.symbol
        value = cls.currency_dct[currency_for][currency_to]
        return f"{float(value)} {currency_to} for 1 {currency_for}"

    def to_currency(self, other_cls: Type[Currency]):
        value = self.currency_dct[self.symbol][other_cls.symbol]
        return other_cls(self.value * value)

    def __add__(self, other):
        value = float(other.to_currency(self.__class__).value)
        return self.__class__(self.value + value)

    def __eq__(self, other):
        value = float(other.to_currency(self.__class__).value)
        return self.value == value

    def __lt__(self, other):
        value = float(other.to_currency(self.__class__).value)
        return self.value < value

    def __gt__(self, other):
        value = float(other.to_currency(self.__class__).value)
        return self.value > value

    def __str__(self):
        return f"{self.value} {self.symbol}"


class Euro(Currency):
    symbol: str = "EUR"

    def __init__(self, value: float):
        super().__init__(value)


class Dollar(Currency):
    symbol: str = "USD"

    def __init__(self, value: float):
        super().__init__(value)


class Pound(Currency):
    symbol: str = "GBP"

    def __init__(self, value: float):
        super().__init__(value)
