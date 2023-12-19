# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show(self) -> str:
        attr_str = ", ".join([
            f"{attr.capitalize()}: {value}"
            for attr, value in self.__dict__.items()
        ])
        return f"{attr_str}"


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int) -> None:
        super().__init__(name, age)
        self.salary = salary


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: int) -> None:
        super().__init__(name, age)
        self.grades = grades
