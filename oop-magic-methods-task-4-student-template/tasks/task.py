class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __set_name__(self, owner, name):
        self.name = name.capitalize()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):
        if not 0 <= value <= 100:
            raise ValueError(f"{self.name} must be between 0 and 100.")


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __set_name__(self, owner, name):
        self.name = name.capitalize()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if instance.__dict__.get(self.name) is not None:
            raise ValueError(f"{self.name} can not be changed.")

        setattr(instance, self.name, value)


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
