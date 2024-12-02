class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        
        if self.is_tied():
            return self.tied_score()
        if self.score_over_four():
            if self.game_over():
                return self.announce_winner()
            return self.over_four_score()
        return self.normal_score()

    def score_to_text(self,score):
        scores = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}
        return scores[score]

    def tied_score(self):
        if self.m_score1 >= 3:
            return "Deuce"
        current_score = self.score_to_text(self.m_score1)
        return f"{current_score}-All"

    def normal_score(self):
        return f"{self.score_to_text(self.m_score1)}-{self.score_to_text(self.m_score2)}"

    def score_over_four(self):
        if max(self.m_score1,self.m_score2) >= 4:
            return True

    def over_four_score(self):
        player_name = self.winning_player()
        return f"Advantage {player_name}"
        
    def is_tied(self):
        return self.m_score1 == self.m_score2

    def winning_player(self):
        if self.m_score1 > self.m_score2:
            return self.player1_name
        return self.player2_name

    def game_over(self):
        return abs(self.m_score1-self.m_score2) >= 2
    
    def announce_winner(self):
        winner = self.winning_player()
        return f"Win for {winner}"