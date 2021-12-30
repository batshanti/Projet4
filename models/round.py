import time
from models.match import Match
from tinydb import TinyDB, Query

db = TinyDB("db.json")
tournament_table = db.table("tournaments")
tournament_query = Query()


class Round:

    def __init__(self, round_name, start_time='', end_time='', matchs=[]):
        self.round_name = round_name
        self.start_time = start_time
        self.end_time = end_time
        self.matchs = matchs

    def save(self, round_score):
        match_1 = Match(*round_score[0])
        match_2 = Match(*round_score[1])
        match_3 = Match(*round_score[2])
        match_4 = Match(*round_score[3])
        self.end_time = time.strftime("%d/%m/%Y")+" "+time.strftime("%Hh%Mm%Ss")
        self.matchs = [match_1.match(), match_2.match(), match_3.match(), match_4.match()]
        return [self.round_name, self.start_time, self.end_time, self.matchs]

    def save_rep(self):
        matchs = ''
        for line in self.matchs:
            matchs = matchs + line[0][0]+' VS '+line[1][0]+'\n'
        return [self.round_name, self.start_time, self.end_time, matchs]

    @staticmethod
    def load_round(choice):
        round = tournament_table.get(doc_id=int(choice))
        return round.get('rounds')
