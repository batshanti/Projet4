

class Match:

    def __init__(self, player1, score_p1, player2, score_p2):
        self.player1 = player1
        self.player2 = player2
        self.score_p1 = score_p1
        self.score_p2 = score_p2


    def match(self):
        return ([self.player1, self.score_p1], [self.player2, self.score_p2])
