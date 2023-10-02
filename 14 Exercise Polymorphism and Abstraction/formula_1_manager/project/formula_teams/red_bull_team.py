from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250_000
    FIRST_POS = 1_500_000
    SECOND_POS = 800_000
    EIGHTH_POS = 20_000
    TENTH_POS = 10_000

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            revenue = (RedBullTeam.EIGHTH_POS + RedBullTeam.EIGHTH_POS) - RedBullTeam.EXPENSES
            self.budged += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budged}$"
        elif race_pos == 2:
            revenue = (RedBullTeam.SECOND_POS + RedBullTeam.EIGHTH_POS) - RedBullTeam.EXPENSES
            self.budged += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budged}$"
        elif 2 < race_pos <= 8:
            revenue = RedBullTeam.EIGHTH_POS - RedBullTeam.EXPENSES
            self.budged += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budged}$"
        elif 8 < race_pos <= 10:
            revenue = RedBullTeam.TENTH_POS - RedBullTeam.EXPENSES
            self.budged += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budged}$"


obj = RedBullTeam(2_000_000)

print(obj.calculate_revenue_after_race(1))
