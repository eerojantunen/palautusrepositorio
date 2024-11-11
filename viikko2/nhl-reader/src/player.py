class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.team = dict["team"]
        self.games = dict["games"]
        self.id = dict["id"]
        self.points = self.goals+self.assists
    
    def __str__(self):
        return f"{self.name:25}  {self.team:13}  {self.goals:<3} + {self.assists:<3} = {self.goals + self.assists:<2}"
