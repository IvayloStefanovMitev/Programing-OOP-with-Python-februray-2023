from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed, Food


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def type_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def type_food(self):
        return[Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35
