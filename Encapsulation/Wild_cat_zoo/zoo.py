from Wild_cat_zoo.animal import Animal
from Wild_cat_zoo.worker import Worker
from Wild_cat_zoo.vet import Vet
from Wild_cat_zoo.lion import Lion
from Wild_cat_zoo.tiger import Tiger
from Wild_cat_zoo.cheetah import Cheetah
from Wild_cat_zoo.keeper import Keeper
from Wild_cat_zoo.caretaker import Caretaker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care = 0
        for animal in self.animals:
            total_care += animal.money_for_care
        if total_care <= self.__budget:
            self.__budget -= total_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        lions = []
        cheetahs = []
        tigers = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
        result += f"\n----- {len(lions)} Lions:"
        for lion in lions:
            result += f"\n{lion.__repr__()}"
        result += f"\n----- {len(tigers)} Tigers:"
        for tiger in tigers:
            result += f"\n{tiger.__repr__()}"
        result += f"\n----- {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            result += f"\n{cheetah.__repr__()}"
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                vets.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
        result += f"\n----- {len(keepers)} Keepers:"
        for keeper in keepers:
            result += f"\n{keeper.__repr__()}"
        result += f"\n----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            result += f"\n{caretaker.__repr__()}"
        result += f"\n----- {len(vets)} Vets:"
        for vet in vets:
            result += f"\n{vet.__repr__()}"
        return result
