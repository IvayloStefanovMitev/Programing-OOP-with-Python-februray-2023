from typing import Dict


class Player:
    NOT_IN_A_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = Player.NOT_IN_A_GUILD

    def add_skill(self, skill_name, mana_cost) -> str:
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self) -> str:
        result = [f"Name: {self.name}\n", f"Guild: {self.guild}\n", f"HP: {self.hp}\n", f"MP: {self.mp}\n"]

        [result.append(f"==={k} - {v}") for k, v in self.skills.items()]

        return f'{"".join(result)}\n'

        # skills = '\n'.join(f"==={s} - {m}" for s, m in self.skills.items())
        #
        # return f"Name: {self.name}\n" \
        #        f"Guild: {self.guild}\n" \
        #        f"HP: {self.hp}\n" \
        #        f"MP: {self.mp}\n" \
        #        f"{skills}\n"