from views.view import View
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import Tournament_controller
from models.round import Round
from tinydb import TinyDB, Query
from terminaltables import SingleTable

db = TinyDB("db.json")
player_table = db.table("players")





tr = Tournament.get_tournament(1)


title_round = "Round_1"



# print(tr.rounds[0][3])
round = Round(tr.rounds[0][0], tr.rounds[0][1], tr.rounds[0][2], tr.rounds[0][3])

a = round.reports_match()

for line in a:
	print(line.player1)
