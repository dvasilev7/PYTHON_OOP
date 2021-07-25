class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        pass

    def hire_worker(self, worker):
        pass

    def fire_worker(self, worker_name):
        pass

    def pay_workers(self):
        pass

    def tend_animals(self):
        pass

    def profit(self, amount):
        pass

    def animals_status(self):
        pass