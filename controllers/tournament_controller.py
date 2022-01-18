import time
from models.tournament import Tournament
from models.round import Round
from views.view_tournament import View_tournament


class Tournament_controller:

    def __init__(self, choice):

        self.choice = choice
        self.tournament = Tournament.get_tournament(choice)
        self.play_tournament_view = View_tournament(self.tournament.players_object)
        self.tournament.choice = choice

    def first(self):
        """Play the first round.
        Ranks the players by their rank.
        Get the results of the matches.
        Create round obj with results of the matche.
        Update the players score.
        Save tournament.
        Returns
        -------
        int
            Retunr choice for playing new round or not.
        """
        self.tournament.sort_player_rank()
        start_time = time.strftime("%d/%m/%Y")+" "+time.strftime("%Hh%Mm%Ss")
        round_1_score = self.play_tournament_view.first_round(self.tournament.players_object, self.tournament.name)
        round_1 = Round("Round_1", start_time)
        self.tournament.rounds = [round_1.save(round_1_score)]
        self.tournament.players_object = Tournament_controller.update_score(
            self.tournament.players_object,
            round_1_score
            )

        self.tournament.save_tournament(1)
        next = -1
        while next != 0 and next != 1:
            next = self.play_tournament_view.next_round()
        return next

    def round(self):
        """Play round

        Determines the round to be played.
        Ranks the players by their rank and score.
        Get the results of the matches.
        Create round object with results of the matche.
        Update the players score.
        Save tournament.
        
        Returns
        -------
        int
            Retunr choice for playing new round or not.
        """
        round_number = self.tournament.check_round() + 1
        round_name = "Round_"+str(round_number)
        start_time = time.strftime("%d/%m/%Y")+" "+time.strftime("%Hh%Mm%Ss")
        self.tournament.sort_player_score()
        round_score = self.play_tournament_view.round(
            self.tournament.players_object,
            self.tournament.name, round_name
            )

        round = Round(round_name, start_time)
        self.tournament.rounds = self.tournament.rounds + [round.save(round_score)]
        self.tournament.players_object = Tournament_controller.update_score(
            self.tournament.players_object,
            round_score
            )

        self.tournament.save_tournament(1)
        if self.tournament.check_round() == 4:
            return 3
        else:
            next = -1
            while next != 0 and next != 1:
                next = self.play_tournament_view.next_round()
            return next

    def check_players(self):
        '''check if there are players in in self.tournament.players and return bool.'''
        if len(self.tournament.players) == 0:
            return False
        else:
            return True

    @staticmethod
    def update_score(players, score):
        """Update the players score
        
        Parameters
        ----------
        players : list
        list of player object
        score : list
        list result matches

        Returns
        -------
        list
            Return list of players object with new score  
        """
        tab_score = [
            [score[0][0], score[0][1]],
            [score[0][2], score[0][3]],
            [score[1][0], score[1][1]],
            [score[1][2], score[1][3]],
            [score[2][0], score[2][1]],
            [score[2][2], score[2][3]],
            [score[3][0], score[3][1]],
            [score[3][2], score[3][3]]
        ]
        for player in players:
            for line in tab_score:
                if player.identity == line[0]:
                    player.score = (float(player.score) + float(line[1]))
        return players