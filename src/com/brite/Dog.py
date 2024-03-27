import random


class Dog:
    info = "Dog has four legs and its Barks"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(random.randint(1, 10))


mypuppy = Dog("puppy", 1)
print(mypuppy.info + mypuppy.name + " " + str(mypuppy.age))
bigdog = Dog("Fiddo", 4)
print(mypuppy.info + bigdog.name + " " + str(bigdog.age))
