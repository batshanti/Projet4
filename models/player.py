from tinydb import TinyDB, Query

db = TinyDB("db.json")
player_table = db.table("players")
player_query = Query()

class Player:

    def __init__(self, name="", first_name="", birth_date="", gender="", rank=None, score=None):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.db = TinyDB("db.json")
        self.player_table = self.db.table("players")
        self.identity = self.name+' '+self.first_name

    def save(self):
        '''Save player in database.'''
        serialized_player = {

            'name': self.name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'rank': self.rank,
        }

        self.player_table.insert(serialized_player)

    def update(self):
        '''Update information for existing player in database.'''
        serialized_player = {

            'name': self.name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'rank': self.rank,
        }

        self.player_table.update(serialized_player, player_query.name == self.name)

    def info_rep(self):
        '''Return list of player information for report.'''
        return [self.name, self.first_name, self.birth_date, self.gender, self.rank]

    def result(self):
        return [self.identity, self.score, self.rank]

    def change_rank(self, rank):
        """Change ranking player with new value.

        Parameters
        ----------
        rank : int
        rank value
        """
        self.rank = rank
        self.update()

    @staticmethod
    def get_players_by_id(id):
        """Get specific player from database and return player object.
        
        Parameters
        ----------    
        id : int
        Doc.id database value.

        Returns
        -------
        object
            player object
        """
        p_info = player_table.get(doc_id=id)
        return Player(p_info['name'],
         p_info['first_name'], p_info['birth_date'], p_info['gender'], p_info['rank'])

    @staticmethod
    def get_8_players(liste_id):
        """Get players informations from database with a doc.id's.
        
        Parameters
        ----------
        liste_id : list
        list of doc.ids

        Returns
        -------
        list
            list of dict contains player information.
        """
        players8 = []
        for line in liste_id:
            dict_players = dict(player_table.get(doc_id=int(line)))
            dict_players.update({'score': 0})
            players8.append(dict_players)
        return players8

    @staticmethod
    def all_players_database():
        '''Return all players from the database.'''
        players = player_table.all()
        return players
