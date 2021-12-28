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

        

        # end_time = time.strftime("%d/%m/%Y")+" "+time.strftime("%Hh%Mm%Ss")
        # serialized_round = {
        # self.round_name : [self.match_1.match(),
        #                    self.match_2.match(),
        #                    self.match_3.match(),
        #                    self.match_4.match(),
        #                    self.start_time,
        #                    end_time]
        # }

        # tournament_info = tournament_table.get(doc_id=choice)
        # tournament_round = tournament_info.get('rounds')
        # if not tournament_round:
        #   tournament_table.update({'rounds': serialized_round}, tournament_query.name == tournament_info.get('name'))

        # else:
        #   tournament_round[self.round_name] = serialized_round[self.round_name]
        #   tournament_table.update({'rounds': tournament_round}, tournament_query.name == tournament_info.get('name'))

    # def update_score(self, players, choice):
    #     print(type(players))
    #     players_scores = [[self.match_1.player_1_name, self.match_1.player_1_score],
    #                       [self.match_1.player_2_name, self.match_1.player_2_score],
    #                       [self.match_2.player_1_name, self.match_2.player_1_score],
    #                       [self.match_2.player_2_name, self.match_2.player_2_score],
    #                       [self.match_3.player_1_name, self.match_3.player_1_score],
    #                       [self.match_3.player_2_name, self.match_3.player_2_score],
    #                       [self.match_4.player_1_name, self.match_4.player_1_score],
    #                       [self.match_4.player_2_name, self.match_4.player_2_score],
    #     ]

    #     for line in players_scores:
    #         for player in players:
    #             player_name = player['name']+' '+player['first_name']
    #             if line[0] == player_name:
    #                 score = float(player['score']) + float(line[1]) 
    #                 player.update({'score' : score})
    #             else:
    #                 pass


    #     tournament_info = tournament_table.get(doc_id=int(choice))
    #     tournament_table.update({'players': players}, tournament_query.name == tournament_info.get('name'))
 

    @staticmethod    
    def load_round(choice):
        round = tournament_table.get(doc_id=int(choice))   
        return round.get('rounds')
