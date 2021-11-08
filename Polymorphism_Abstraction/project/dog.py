from project.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super(Dog, self).__init__(name, age, gender)

    def make_sound(self):
        return "Woof!"