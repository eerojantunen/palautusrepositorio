import requests
from player import Player
from rich.console import Console
from rich.table import Table
class UI():
    def __init__(self):
        pass


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
        #result = []
        #for i in self.players:
        #    result.append(str(i))
        return self.players

def main():
    console = Console()
    console.print("[italic]NHL[/italic] statistics by nationality",)
    season = console.input("Select the season: [magenta][2018-2019/2019-20/2020-21/2021-22/2022-23/2023-2024/2024-2025][/magenta]: ")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = console.input("\nSelect nationality: [magenta][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/][/magenta]: ")
       
        table = Table(title=f"[italic]Top scorers of {nationality} season {season}[/italic]", show_header=True, header_style="bold")
        table.add_column("name", style="cyan", width=25)
        table.add_column("team", style="magenta", width=10)
        table.add_column("goals", style="green", width=10)
        table.add_column("assists", style="green", width=10)
        table.add_column("points", style="green", width=10)

        players = stats.top_scorers_by_nationality(nationality)
        for player in players:
            table.add_row(str(player.name),str(player.team),str(player.goals),str(player.assists),str(player.points))
        console.print(table)
if __name__ == "__main__":
    main()

