from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eat=0):
        self.name = name
        self.weight = weight
        self.food_eat = food_eat
        self.acceptable_foods = None
        self.weight_per_food = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if type(food) not in self.acceptable_foods:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * self.weight_per_food
        self.food_eat += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eat}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eat}]"