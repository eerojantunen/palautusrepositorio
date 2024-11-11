import requests
from player import Player

class PlayerReader():
    def __init__(self, url):
        self.response = requests.get(url).json()

class PlayerStats():
    def __init__(self,reader:PlayerReader):
        self.reader = reader
        
    def top_scorers_by_nationality(self,nationality:str):
        self.players = []
        for player_dict in self.reader.response:
            if player_dict["nationality"]== nationality:
                player = Player(player_dict)
                self.players.append(player)
        self.players = sorted(self.players,key=lambda x: x.goals, reverse =True)
        result = []
        for i in self.players:
            result.append(str(i))
        return result

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("CAN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()

