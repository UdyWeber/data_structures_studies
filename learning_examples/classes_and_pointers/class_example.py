class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    # The dunder init method is what we call a magic method that are especial methods to manipulate our data struct

    def set_name(self, name: str):
        self.name = name
    # Here we have a func that changes the value of the property when we call it

# We create a structure that has a constructor which will apply variables passed in to our class properties
# So each instance of the class will have different data


def create_persons():
    person_one = Person(name="Bob", age=18)
    person_two = Person(name="Sally", age=15)

    print("Person 1: ", person_one.name, person_one.age)
    print("Person 2: ", person_two.name, person_two.age)

    person_two.set_name("Jawlestest")

    print("Person 2:", person_two.name, person_two.age)


if __name__ == "__main__":
    create_persons()

