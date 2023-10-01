from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price) -> str:
       if price > self.__budget:
           return "Not enough budget"

       elif len(self.animals) == self.__animal_capacity:
           return "Not enough space for animal"

       self.animals.append(animal)
       self.__budget -= price
       return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        try:
            curr_worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(curr_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        salaries = sum(w.salary for w in self.workers)
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        budged_of_animals = sum(a.money_for_care for a in self.animals)

        if budged_of_animals > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= budged_of_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lion = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tiger = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetah = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        result = [f"You have {len(self.animals)} animals"]

        result.append(f"----- {len(lion)} Lions:")
        result.extend(lion)

        result.append(f"----- {len(tiger)} Tigers:")
        result.extend(tiger)

        result.append(f"----- {len(cheetah)} Cheetahs:")
        result.extend(cheetah)

        return "\n".join(str(x) for x in result)

    def workers_status(self) -> str:
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet']
                  ]

        return "\n".join(result)