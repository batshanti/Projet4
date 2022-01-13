from views.view import View
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import Tournament_controller
from models.round import Round
from tinydb import TinyDB, Query
from terminaltables import SingleTable


# def score_input(player_1, player_2):

#     player_1_message = player_1+" -> Enter score : "
#     player_2_message = player_2+" -> Enter score : "
#     score = [0, 0.5, 1]
#     while True:
#         try:
#             player_1_score = float(input(player_1_message))
#             player_2_score = float(input(player_2_message))
#         except ValueError:
#             print('il faut indiquer 0 ou 1 ou 0.5')
#             continue
#     if player_1_score not in score or player_2_score not in score:
#             print("il faut indiquer 0 ou 1 ou 0.5")
#             pass
#     else:
#         a = [player_1_score, player_2_score]
#         print(a)
        

# player_1 = "teddy"
# player_2 = "marc"

# score_input(player_1, player_2)








def score_input(player_1, player_2):

    player_1_message = player_1+" -> Enter score : "
    player_2_message = player_2+" -> Enter score : "
    score = [0, 0.5, 1]
    while True:
        try:
            player_1_score = float(input(player_1_message))
            player_2_score = float(input(player_2_message))
            assert player_1_score in score and player_2_score in score
        except AssertionError:
            print("mauvais nombre")
        except ValueError:
            print("pas de lettre")    
            pass
        else:
            a = [player_1_score, player_2_score]
            print(a)
            break




player_1 = "teddy"
player_2 = "marc"

score_input(player_1, player_2)