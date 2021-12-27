# from terminaltables import AsciiTable, DoubleTable, SingleTable
# from tinydb import TinyDB, Query
# from models.player import Player
# from models.tournament import Tournament
# db = TinyDB("database.json")
# player_table = db.table("players")

# title = 'TOURNAMENT'

# table_data = [
#     ['Name', 'first_name', 'birth_date', 'sex', 'rank'],
# ]


# all_players = player_table.all()
# print(all_players)

# list_players = []
# for line in all_players:
#     player = Player(line['name'], line['first_name'], line['birth_date'], line['sex'], line['rank'])
#     list_players.append(player)

# sort_players = sorted(list_players, key=lambda t: t.rank)

# for line in sort_players:
#     table_data.append(line.save_rep())



# table = SingleTable(table_data, title)
# print(table.table)


while True:
    try:
        salary = float(input("whats ur salary\n"))
    except ValueError:
        print("I did not understood that")
        continue
    else:
        break



        while True:
            choice = View.manage_player_view()
            if choice not in ('0', '1', '2'):
                print("Not an appropriate choice.")
                continue
            else:    
                func = getattr(Controller, choices[choice])
                func()
                break        