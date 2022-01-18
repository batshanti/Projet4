from tinydb import TinyDB, Query
from models.player import Player
import time

db = TinyDB("db.json")
tournament_table = db.table("tournaments")
tournament_query = Query()


class Tournament:

    def __init__(
        self,
        name="",
        place="",
        start_date="",
        end_date="",
        nb_of_rounds=4,
        rounds=[],
        players=[],
        time_control="",
        description=""
    ):

        self.name = name
        self.place = place
        self.start_date = time.strftime("%d/%m/%Y")
        self.end_date = end_date
        self.nb_of_rounds = nb_of_rounds
        self.rounds = rounds
        self.players = players
        self.players_object = Tournament.make_players_object(self.players)
        self.time_control = time_control
        self.description = description
        self.db = TinyDB("db.json")
        self.tournament_table = self.db.table("tournaments")
        self.tournament_query = Query()

    def save_tournament(self, choice=0):
        """Serialize tournament and save in database.
            "choice" argument : Save new tournamemt creation.
                                Update an existing tournament.    
        """
        serialized_players = []
        for line in self.players_object:
            liste = {
                'name': line.name,
                'first_name': line.first_name,
                'birth_date': line.birth_date,
                'gender': line.gender,
                'rank': line.rank,
                'score': line.score
            }
            serialized_players.append(liste)

        serialized_tournament = {

            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'nb_of_rounds': self.nb_of_rounds,
            'rounds': self.rounds,
            'players': serialized_players,
            'time_control': self.time_control,
            'description': self.description
        }

        if choice == 0:
            self.tournament_table.insert(serialized_tournament)

        else:
            tournament_table.update(serialized_tournament, tournament_query.name == self.name)
            self.players_object = Tournament.make_players_object(self.players)

    def sort_player_name(self):
        self.players_object = sorted(self.players_object, key=lambda t: t.name)
        return self.players_object

    def sort_player_rank(self):
        self.players_object = sorted(self.players_object, key=lambda t: t.rank)
        return self.players_object

    def sort_player_score(self):
        self.players_object = sorted(self.players_object, key=lambda t: (t.score, t.rank), reverse=True)
        return self.players_object

    def check_round(self):
        """Get all round in self.rounds and extract the nmber of the last round played"""
        if not self.rounds:
            return 0
        else:
            round = []
            for line in self.rounds:
                round.append(line[0])
            round_number = round[-1]
            return int(round_number[6])

    def add_players(self, players):
        """Add players in tournament and save"""
        self.players = players
        self.players_object = Tournament.make_players_object(self.players)
        self.save_tournament(1)

    def save_rep(self):
        """Serialize tournament data player for reports"""
        list_players_name = ''
        for line in self.players_object:
            identity = line.identity
            list_players_name = list_players_name + identity+'\n'
        return [
            self.name,
            self.place,
            self.start_date,
            self.end_date,
            list_players_name,
            self.time_control,
            self.description
        ]

    @staticmethod
    def load_tournament_list():
        for line in tournament_table:
            print(line.doc_id, ' - ', line['name'])

    @staticmethod
    def get_tournament(choice):
        """Use doc.id element to get tournament information and return a tournament object"""
        tournament_info = tournament_table.get(doc_id=int(choice))
        name = tournament_info['name']
        place = tournament_info['place']
        start_date = tournament_info['start_date']
        end_date = tournament_info['end_date']
        nb_of_rounds = tournament_info['nb_of_rounds']
        rounds = tournament_info['rounds']
        players = tournament_info['players']
        time_control = tournament_info['time_control']
        description = tournament_info['description']

        return Tournament(
            name=name,
            place=place,
            start_date=start_date,
            end_date=end_date,
            nb_of_rounds=nb_of_rounds,
            rounds=rounds,
            players=players,
            time_control=time_control,
            description=description
        )

    @staticmethod
    def make_players_object(players):
        """Return list of players object"""
        liste_p = []
        for line in players:
            player = Player(
                line['name'],
                line['first_name'],
                line['birth_date'],
                line['gender'],
                line['rank'],
                line['score']
            )
            liste_p.append(player)
        return liste_p

    @staticmethod
    def all_tournaments_database():
        tournaments = tournament_table.all()
        return tournaments

