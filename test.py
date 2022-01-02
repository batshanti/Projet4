from views.view import View
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import Tournament_controller
from tinydb import TinyDB, Query
db = TinyDB("db.json")
player_table = db.table("players")
# from tinydb.table import Document

# tr = Tournament_controller(1)

# a = tr.tournament.check_round()
# print(a)
# tr.tournament.players_object[0].score = 11111
# tr.tournament.save_tournament()

# tr.tournament.save_bis()

# for line in tr.tournament.players_object:
#     print(line.identity, line.rank)

# tr.tournament.sort_player_rank()

# tr.play_tournament_view.players_tournament(tr.tournament.sort_player_rank())

# print(tr.tournament.rounds)

# a = tr.tournament.check_round()
# print(a)



View.mess(str(1))