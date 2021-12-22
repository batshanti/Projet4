from tinydb import TinyDB, Query

db = TinyDB("db.json")
player_table = db.table("players")
player_query = Query()


class Player:

    def __init__(self, name="", first_name="", birth_date="", sex="", rank=None, score=None):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        self.score = score
        self.db = TinyDB("db.json")
        self.player_table = self.db.table("players")
        self.identity = self.name+' '+self.first_name

    def save(self):
        serialized_player = {

            'name': self.name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'sex': self.sex,
            'rank': self.rank,
        }

        self.player_table.insert(serialized_player)

    def save_p(self):
        serialized_player = {

            'name': self.name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'sex': self.sex,
            'rank': self.rank,
        }

        self.player_table.update(serialized_player, player_query.name == self.name)

    
    def save_rep(self):
        return [self.name, self.first_name, self.birth_date, self.sex, self.rank]
        

    def change_rank(self, rank):
        self.rank = rank
        self.save_p() 


    @staticmethod 
    def load_players_rank():
        for line in player_table:
            print(line.doc_id, ' - ', line['first_name'], line['name'], line['rank'])

    

    @staticmethod
    def load_players_register():
        for line in player_table:
            print(line.doc_id,' - ',line['first_name'],line['name'],line['birth_date'], line['sex'])

    @staticmethod
    def get_players_by_id(id):
        p_info = player_table.get(doc_id=id)
        return Player(p_info['name'], p_info['first_name'], p_info['birth_date'], p_info['sex'], p_info['rank'])

    @staticmethod
    def get_8_players(liste_id):
        players8 = []
        for line in liste_id:
            dict_players = dict(player_table.get(doc_id=int(line)))
            dict_players.update({'score':0})
            players8.append(dict_players)

        return players8

    @staticmethod
    def all_players_database():
        players = player_table.all()
        return players
