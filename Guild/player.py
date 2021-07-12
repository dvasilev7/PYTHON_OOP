class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        result = f"Name: {self.name}"
        result += f"\nGuild: {self.guild}"
        result += f"\nHP: {self.hp}"
        result += f"\nMP: {self.mp}"
        if self.skills:
            for key, value in self.skills.items():
                result += f"\n==={key} - {value}"
        return result
