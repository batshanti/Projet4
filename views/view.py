#! /usr/bin/env python3
# coding: utf-8

from models.player import Player
from models.tournament import Tournament
from terminaltables import SingleTable

HOME_PIC =  "\n   |\\_\n  /  .\\_\n |   ___)     CHESS TOURNAMENT\n |    \\\n |    |\n /_____\\\n[_______]\n"

HOMEPAGE_MENU = [

   "1 : Tournament",
   "2 : Manage player",
   "3 : Reports",
   "0 : Quit"
]

MANAGE_PLAYERS_MENU = [

    "1 : Create player",
    "2 : Change rancking player",
    "0 : Return"
]

TOURNAMENT_MENU = [

    "1 : Create tournament",
    "2 : Play tournament",
    "0 : Return"
]

REPORTS_MENU = [

    "1 : All Players",
    "2 : All players in Tournament",
    "3 : All Tournaments",
    "4 : Rounds in Tournament",
    "5 : Matchs in Tournament",
    "0 : Return"
]

MESSAGES = {

    "1": "\nBad informations player, please retry\n",
    "2": "\nthe player is created\n"
}


class View:

    def __init__(self):
        pass

    @staticmethod
    def home_page():
        print("\n"*20)
        print(HOME_PIC)
        for line in HOMEPAGE_MENU:
            print(line)
        choice = input("choose an action : ")
        return choice

    @staticmethod
    def mess(number):
        print(MESSAGES[number])

    @staticmethod
    def create_player_view():
        name = input("Enter name :")
        first_name = input("Enter First Name :")
        birth_date = input("Enter birth date (Format : dd/mm/yy) :")
        gender = input("Enter Gender (F or H) :")
        rank = int(input("Enter Rank (positive number) :"))
        infos_player = [name.upper(), first_name.capitalize(), birth_date, gender.upper(), rank]
        return infos_player

    @staticmethod
    def manage_player_view():
        for line in MANAGE_PLAYERS_MENU:
            print(line)
        choice = input("choose an action : ")
        return choice

    @staticmethod
    def change_ranking_view(players):
        title_all_p_rank = 'ALL PLAYERS BY RANK'
        data_r = [['ID', 'Name', 'Fist Name', 'Birth date', 'gender', 'Rank'], ]
        for line in players:
            pl = [line.doc_id, line['name'], line['first_name'], line['birth_date'], line['gender'], line['rank']]
            data_r.append(pl)
        table1 = SingleTable(data_r, title_all_p_rank)
        print(table1.table)
        choice = int(input('choose player : '))
        choice_rank = int(input('choose new rank : '))
        return [choice, choice_rank]

    @staticmethod
    def tournament_menu_view():
        for line in TOURNAMENT_MENU:
            print(line)
        choice = input("choose an action : ")
        return choice

    @staticmethod
    def create_tournament_view():
        name = input("Enter name tournament: ")
        place = input("Enter place tournament: ")
        end_date = input("Enter end date  :")
        time_control = input("Enter time control (bullet, blitz, coup rapide) :")
        description = input("Enter tournament description :")
        return name, place, end_date, time_control, description

    @staticmethod
    def choose_tournament_view():
        Tournament.load_tournament_list()
        choice = int(input('choose tounament :'))
        return choice

    @staticmethod
    def next_round():
        print("Play next round ?")
        next = input("1 > yes\n0 > return\n")
        return next

    @staticmethod
    def choice_player_tournament_view(all_players):
        list_player = []
        for line in all_players:
            print(line.doc_id, ' - ', line['name'], line['first_name'], line['birth_date'], line['rank'])

        i = 1
        while len(list_player) < 8:
            choice = input('choose player '+str(i)+': ')
            if choice in list_player:
                print("player already registered")
            else:
                list_player.append(choice)
                player = Player.get_players_by_id(int(choice))
                print("player "+str(i)+" is "+player.identity)
                i = i + 1
        return list_player

    @staticmethod
    def reports_menu():
        print("\n"*20)
        for line in REPORTS_MENU:
            print(line)
        choice = input("choose an action : ")
        return choice

    @staticmethod
    def all_players(players_name, players_rank):
        title_all_p = 'ALL PLAYERS BY NAME'
        title_all_p_rank = 'ALL PLAYERS BY RANK'
        data_p = [['Name', 'Fist Name', 'Birth date', 'gender', 'Rank'], ]
        data_r = [['Name', 'Fist Name', 'Birth date', 'gender', 'Rank'], ]
        for line in players_name:
            data_p.append(line.save_rep())
        table1 = SingleTable(data_p, title_all_p)
        print("\n")
        print(table1.table)
        print("\n")

        for line in players_rank:
            data_r.append(line.save_rep())
        table2 = SingleTable(data_r, title_all_p_rank)
        print(table2.table)
        print("\n")
        print("Enter 0 to return")

    @staticmethod
    def all_players_in_tournament(tournament):
        title_all_p = "ALL PLAYERS IN TOURNAMENT BY NAME"
        title_all_p_rank = "ALL PLAYERS IN TOURNAMENT BY RANK"
        data_p = [['Name', 'Fist Name', 'Birth date', 'gender', 'Rank'], ]
        data_r = [['Name', 'Fist Name', 'Birth date', 'gender', 'Rank'], ]
        for line in tournament.sort_player_name():
            data_p.append(line.save_rep())
        table1 = SingleTable(data_p, title_all_p)
        print("\n")
        print('Tournament: '+tournament.name)
        print("\n")
        print(table1.table)
        print("\n")

        for line in tournament.sort_player_rank():
            data_r.append(line.save_rep())
        table2 = SingleTable(data_r, title_all_p_rank)
        print(table2.table)
        print("\n")
        print("Enter 0 to return")

    @staticmethod
    def all_tournaments(tournaments):
        title_tournament = "ALL TOURNAMENTS"
        data_t = [['Name', 'Place', 'Start', 'End', 'Players', 'Time control', 'Description'], ]
        for line in tournaments:
            data_t.append(line.save_rep())

        table1 = SingleTable(data_t, title_tournament)
        table1.justify_columns[4] = 'right'
        print(table1.table)
        print("\n")
        print("Enter 0 to return")

    @staticmethod
    def all_rounds(rounds, tournament):
        title_rounds = "ALL ROUNDS IN TOURNAMENT: ", tournament.name
        data_r = [['Round Name', 'Start date round', 'End date round', 'matchs'], ]
        for line in rounds:
            data_r.append(line.save_rep())
        table1 = SingleTable(data_r, title_rounds)
        table1.justify_columns[3] = 'right'
        print(table1.table)
        print("\n")
        print("Enter 0 to return")

    @staticmethod
    def choose(message):
        choice = int(input(message))
        return choice
