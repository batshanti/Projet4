#! /usr/bin/env python3
# coding: utf-8

from views.view import View
from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import Tournament_controller

class Controller:

    def __init__(self):
        # self.lastTournament = None
        pass


    # def basicMenu(self):
    #     if self.lastTournament is not None:
    #         self.displayTournamentMenu()
    #     else:
    #         self.start()

    @staticmethod
    def start():
        choices = {
            "1" : "manage_tournament_controller",
            "2" : "manage_player_controller",
            "3" : "reports_menu",
            "0" : "quit"
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
    def manage_player_controller():
        choices = {
            "1" : "create_player",
            "2" : "change_ranking_player",
            "0" : "start"
        }
        while True:
            choice = View.manage_player_view()
            if choice not in ('0', '1', '2'):
                print("Not an appropriate choice.")
            else:    
                func = getattr(Controller, choices[choice])
                func()
                break

    @staticmethod
    def manage_tournament_controller():
        choices = {
            "1" : "create_tournament",
            "2" : "play_tournament_controller",
            "0" : "start"
        }
        choice = View.tournament_menu_view()
        func = getattr(Controller, choices[choice])
        func()

    # @staticmethod
    # def next_round_menu(next):
    #     choices = {
    #         "1" : "play_round",
    #         "0" : "manage_tournament_controller"
    #     }
    #     choice = 2
    #     while choice != 0 or choice != 1:
    #         choice = View.tournament_menu_view()
    #     func = getattr(Controller, choices[choice], next)
    #     func()

    
    @staticmethod
    def reports_menu():
        pass

    @staticmethod
    def quit():
        pass

    @staticmethod
    def create_player():
        infos_player_tab = View.create_player_view()
        player1 = Player(*infos_player_tab)
        player1.save()
        Controller.manage_player_controller()

    @staticmethod
    def change_ranking_player():
        choice_player = View.change_ranking_view()
        player = Player.get_players_by_id(choice_player(0))
        
        Controller.manage_player_controller()

    @staticmethod  
    def create_tournament():
        infos_tounament_tab = View.create_tournament_view()
        tournament1 = Tournament(name=infos_tounament_tab[0], place=infos_tounament_tab[1], end_date=infos_tounament_tab[2], time_control=infos_tounament_tab[3], description=infos_tounament_tab[4])
        tournament1.save_tournament()
        Controller.start()

    @staticmethod
    def play_tournament_controller():
        choice = View.choose_tournament_view()
        play_tournament = Tournament_controller(choice)
        if play_tournament.check_players() == False:
            list_player = View.choice_player_tournament_view()
            players8 = Player.get_8_players(list_player)
            play_tournament.tournament.add_players(players8)

        if play_tournament.tournament.check_round() == 0:
            next = play_tournament.first()
            if next == 0:
                Controller.manage_tournament_controller()
            else:
                Controller.play_round(choice)

        if play_tournament.tournament.check_round() >= 1 and play_tournament.tournament.check_round() < 4:
            Controller.play_round(choice)

        else:
            Controller.manage_tournament_controller()
            
                

    @staticmethod
    def play_round(choice):
        play_tournament = Tournament_controller(choice)
        next = play_tournament.round()
        if next == 0:
            Controller.manage_tournament_controller()
        if next == 1 and play_tournament.tournament.check_round() == 4:
            Controller.manage_tournament_controller()
        if next == 1:
            play_tournament.round()

            











