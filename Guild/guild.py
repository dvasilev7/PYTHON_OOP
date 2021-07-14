from Guild.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, name: str):
        for player in self.players:
            if name == player.name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {name} has been removed from the guild."
        return f"Player {name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}"
        if self.players:
            for p in self.players:
                result += f"\n{p.player_info()}"
        return result
