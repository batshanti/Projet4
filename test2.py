from terminaltables import AsciiTable, DoubleTable, SingleTable
from tinydb import TinyDB, Query
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import Tournament_controller
from models.round import Round
db = TinyDB("database.json")
player_table = db.table("players")

tr = Tournament_controller(1)

print(tr.tournament.rounds[0][0])
print(tr.tournament.rounds[0][1])
print(tr.tournament.rounds[0][2])
print(tr.tournament.rounds[0][3])

r = Round(tr.tournament.rounds[0][0],
        tr.tournament.rounds[0][1],
        tr.tournament.rounds[0][2],
        tr.tournament.rounds[0][3]
    )

rr = r.save_rep()
print(rr[3])