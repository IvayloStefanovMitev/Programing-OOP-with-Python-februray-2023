from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budged: int):
        self.budged = budged

    @property
    def budged(self):
        return self.__budged

    @budged.setter
    def budged(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budged = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        ...
