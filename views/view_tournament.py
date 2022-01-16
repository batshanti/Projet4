class View_tournament:

    def __init__(self, players):
        self.players = players

        pass

    def players_tournament(self, players):
        for line in players:
            print(line.name, line.rank)

    def first_round(self, players, tournament_name):
        print("=============== ",tournament_name.upper()," ===================\n")
        print("ROUND 1\n")
        print("MATCH 1 : ",players[0].identity,"VS",players[4].identity)
        print("MATCH 2 : ",players[1].identity,"VS",players[5].identity)
        print("MATCH 3 : ",players[2].identity,"VS",players[6].identity)
        print("MATCH 4 : ",players[3].identity,"VS",players[7].identity)
        print("\n==========================================================\n")

        print("MATCH 1\n")
        match_1 = View_tournament.score_input(players[0], players[4])  
        print("\nMATCH 2\n")
        match_2 = View_tournament.score_input(players[1], players[5])
        print("\nMATCH 3\n")
        match_3 = View_tournament.score_input(players[2], players[6])
        print("\nMATCH 4\n")
        match_4 = View_tournament.score_input(players[3], players[7])
        return [match_1, match_2, match_3, match_4]

    def round(self, players, tournament_name, round_name):
        print("=============== ",tournament_name.upper()," ===================\n")
        print(round_name)
        print("MATCH 1 : ",players[0].identity,"VS",players[1].identity)
        print("MATCH 2 : ",players[2].identity,"VS",players[3].identity)
        print("MATCH 3 : ",players[4].identity,"VS",players[5].identity)
        print("MATCH 4 : ",players[6].identity,"VS",players[7].identity)

        print("MATCH 1\n")
        match_1 = View_tournament.score_input(players[0], players[1])
        print("MATCH 2\n")
        match_2 = View_tournament.score_input(players[2], players[3])
        print("MATCH 3\n")
        match_3 = View_tournament.score_input(players[4], players[5])
        print("MATCH 4\n")
        match_4 = View_tournament.score_input(players[6], players[7])
        return [match_1, match_2, match_3, match_4]


    def next_round(self):
        print("Play next round ?")
        next = input("1 > yes\n0 > return\n")
        return int(next)
            
    @staticmethod
    def score_input(player_1, player_2):
        print(player_1.identity," VS ",player_2.identity)
        player_1_message = player_1.identity+" -> Enter score : "
        player_2_message = player_2.identity+" -> Enter score : "
        valide_score = [0, 0.5, 1]
        while True:
            try:
                player_1_score = float(input(player_1_message))
                player_2_score = float(input(player_2_message))
                assert player_1_score in valide_score and player_2_score in valide_score
            except AssertionError:
                print("score must 0 or 0.5 or 1")
            except ValueError:
                print("score must 0 or 0.5 or 1")
                pass
            else:
                return [player_1.identity, player_1_score, player_2.identity, player_2_score]
                break
                

        




