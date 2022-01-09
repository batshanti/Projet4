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
pls = tr.sort_player_score()
title = tr.name
data_result = [['#', 'Players', 'Score', 'Rank'], ]
for i,player in enumerate(pls):
	i = i + 1
	r = player.result()
	r.insert(0, i)
	data_result.append(r)
table1 = SingleTable(data_result, title)
print(table1.table)





