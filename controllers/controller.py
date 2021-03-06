#! /usr/bin/env python3
# coding: utf-8

from views.view import View, MESSAGES
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import Tournament_controller
from models.round import Round


class Controller:

    def __init__(self):

        pass

    @staticmethod
    def start():
        '''Display home page menu and ask the user to choose to navigate.'''
        choices = {
            "1": "manage_tournament",
            "2": "manage_player",
            "3": "reports_menu",
            "0": "quit"
        }
        while True:
            choice = View.home_page()
            if choice not in ('0', '1', '2', '3'):
                print("Not an appropriate choice.")
            else:
                func = getattr(Controller, choices[choice])
                func()
                break

    @staticmethod
    def manage_player():
        '''Display manage player menu and ask the user to choose to navigate.'''
        choices = {
            "1": "create_player",
            "2": "change_ranking_player",
            "0": "start"
        }
        while True:
            try:
                choice = View.manage_player_view()
                func = getattr(Controller, choices[choice])
                func()
                break
            except KeyError:
                View.mess("4")
                pass

    @staticmethod
    def manage_tournament():
        '''Display manage tournament menu and ask the user to choose to navigate.'''
        choices = {
            "1": "create_tournament",
            "2": "play_tournament_controller",
            "0": "start"
        }
        while True:
            try:
                choice = View.tournament_menu_view()
                func = getattr(Controller, choices[choice])
                func()
                break
            except KeyError:
                View.mess("4")
                continue

    @staticmethod
    def reports_menu():
        '''Display reports tournament menu and ask the user to choose to navigate.'''
        choices = {
            "1": "all_players",
            "2": "all_players_in_tournament",
            "3": "all_tournaments",
            "4": "rounds_in_tournament",
            "5": "matches_in_tounament",
            "0": "start"
        }
        while True:
            try:
                choice = View.reports_menu()
                func = getattr(Controller, choices[choice])
                func()
                break
            except KeyError:
                View.mess("4")
                continue

    @staticmethod
    def quit():
        '''End the program.'''
        pass

    @staticmethod
    def create_player():
        '''Request player information and save in database.'''
        infos = View.create_player_view()
        if Controller.valid_information(infos) is False:
            View.mess(str(1))
            Controller.manage_player()
        else:
            player1 = Player(*infos)
            player1.save()
            View.mess(str(2))
            Controller.manage_player()

    @staticmethod
    def create_tournament():
        '''Request tournament information and save in database.'''
        infos = View.create_tournament_view()
        if Controller.valid_information(infos) is False:
            View.mess(str(1))
            Controller.manage_tournament()
        else:
            tournament1 = Tournament(
                name=infos[0],
                place=infos[1],
                end_date=infos[2],
                time_control=infos[3],
                description=infos[4]
            )
            tournament1.save_tournament()
            View.mess('2')
            Controller.manage_tournament()

    @staticmethod
    def change_ranking_player():
        '''ask and save new rank player in database.'''
        all_players = Player.all_players_database()
        choice_player = View.change_ranking_view(all_players)
        player = Player.get_players_by_id(choice_player[0])
        player.change_rank(choice_player[1])
        Controller.manage_player()

    @staticmethod
    def play_tournament_controller():
        """play tournament round.
        Determines if players are in tournament.
        Add players in tournament.
        Determines which round to play : First or round.
        Shows the result when all rounds are played.
        """
        choice = View.choose_tournament_view()
        play_tournament = Tournament_controller(choice)
        if play_tournament.check_players() is False:
            list_player = View.choice_player_tournament_view(Player.all_players_database())
            players8 = Player.get_8_players(list_player)
            play_tournament.tournament.add_players(players8)

        if play_tournament.tournament.check_round() == 0:
            next = play_tournament.first()
            if next == 0:
                Controller.manage_tournament()
            else:
                Controller.play_round(choice)

        if play_tournament.tournament.check_round() >= 1 and play_tournament.tournament.check_round() < 4:
            Controller.play_round(choice)

        if play_tournament.tournament.check_round() == 4:
            Controller.result(play_tournament.tournament)

    @staticmethod
    def play_round(choice):
        """Play round.

        Parameters
        ----------
        choice : int
        Doc.id of tournament in database
        """
        play_tournament = Tournament_controller(choice)
        next = play_tournament.round()
        if next == 3:
            Controller.result(play_tournament.tournament)
        if next == 0:
            Controller.manage_tournament()
        if next == 1 and play_tournament.tournament.check_round() == 4:
            Controller.manage_tournament()
        if next == 1:
            play_tournament.round()

    @staticmethod
    def result(tournament):
        '''Display result at the end of the tournament.'''
        View.result(tournament)
        Controller.choose(MESSAGES['3'], [0])
        Controller.manage_tournament()

    @staticmethod
    def all_players():
        '''Get all players from database and show them listed by Name and Rank.'''
        all_players = Player.all_players_database()
        list_players = []
        for line in all_players:
            player = Player(
                line['name'],
                line['first_name'],
                line['birth_date'],
                line['gender'],
                line['rank']
            )
            list_players.append(player)

        sort_players_name = sorted(list_players, key=lambda t: t.name)
        sort_players_rank = sorted(list_players, key=lambda t: t.rank)
        View.all_players(sort_players_name, sort_players_rank)
        Controller.choose(MESSAGES['3'], [0])
        Controller.reports_menu()

    @staticmethod
    def all_players_in_tournament():
        '''Get all players in database for specific tournament and display.'''
        choice_tr = View.choose_tournament_view()
        tr = Tournament.get_tournament(choice_tr)
        View.all_players_in_tournament(tr)
        Controller.choose(MESSAGES['3'], [0])
        Controller.reports_menu()

    @staticmethod
    def all_tournaments():
        '''Get all tournament from database and display.'''
        all_tournaments = Tournament.all_tournaments_database()
        list_tournaments = []
        for line in all_tournaments:
            tournament = Tournament(
                line['name'],
                line['place'],
                line['start_date'],
                line['end_date'],
                line['nb_of_rounds'],
                line['rounds'],
                line['players'],
                line['time_control'],
                line['description'])
            list_tournaments.append(tournament)
            print(tournament.name)
        View.all_tournaments(list_tournaments)
        Controller.choose(MESSAGES['3'], [0])
        Controller.reports_menu()

    @staticmethod
    def rounds_in_tournament():
        '''Get all rounds informartion for specific tournament and display.'''
        choice_tr = View.choose_tournament_view()
        tr = Tournament.get_tournament(choice_tr)
        list_rounds = []
        for line in tr.rounds:
            round = Round(line[0], line[1], line[2], line[3])
            list_rounds.append(round)
        View.all_rounds(list_rounds, tr)
        Controller.choose(MESSAGES['3'], [0])
        Controller.reports_menu()

    @staticmethod
    def matches_in_tounament():
        '''Get all matches informartion for specific tournament and display.'''
        choice_tr = View.choose_tournament_view()
        tr = Tournament.get_tournament(choice_tr)
        list_rounds = []
        for line in tr.rounds:
            round = Round(line[0], line[1], line[2], line[3])
            list_rounds.append(round)
        View.all_matches(list_rounds)
        Controller.choose(MESSAGES['3'], [0])
        Controller.reports_menu()

    @staticmethod
    def valid_information(info):
        '''Check if the input informations Player / Tournament is not empty.'''
        for line in info:
            if line:
                valid = True
            else:
                valid = False
                return valid
        return valid

    @staticmethod
    def choose(message, menu):
        while True:
            choice = View.choose(message)
            if choice not in menu:
                View.mess("4")
                continue
            else:
                break
