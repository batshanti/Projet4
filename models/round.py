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
        ''''''
        match_1 = Match(*round_score[0])
        match_2 = Match(*round_score[1])
        match_3 = Match(*round_score[2])
        match_4 = Match(*round_score[3])
        self.end_time = time.strftime("%d/%m/%Y")+" "+time.strftime("%Hh%Mm%Ss")
        self.matchs = [match_1.match(), match_2.match(), match_3.match(), match_4.match()]
        return [self.round_name, self.start_time, self.end_time, self.matchs]

    def info_rep(self):
        '''Return list of round information to make reports'''
        matchs = ''
        for line in self.matchs:
            matchs = matchs + line[0][0]+' VS '+line[1][0]+'\n'
        return [self.round_name, self.start_time, self.end_time, matchs]

    def get_match_reports(self):
        '''Return list of matches information to make reports'''
        list_match = []
        for line in self.matchs:
            match = Match(line[0][0], line[0][1], line[1][0], line[1][1])
            list_match.append(match)
        return list_match

    @staticmethod
    def load_round(choice):
        round = tournament_table.get(doc_id=int(choice))
        return round.get('rounds')

        