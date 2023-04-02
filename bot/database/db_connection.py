import sqlite3


class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Database.__instance:
            Database.__instance = super(Database, cls).__new__(cls)
        return Database.__instance

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `nickname`) VALUES (?, ?)", (user_id, nickname,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    async def set_favourite_team(self, user_id, favourite_team,):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `favourite_team` = ? WHERE `user_id` = ?", (favourite_team, user_id,))

    def get_user_id(self, nickname):
        with self.connection:
            result = self.cursor.execute("SELECT `user_id` FROM `users` WHERE `nickname` = ?", (nickname,)).fetchall()
            for row in result:
                userid = int(row(0))
            return userid

    async def get_types(self):
        with self.connection:
            query = self.cursor.execute("SELECT DISTINCT `kind_of_sport` FROM `teams`").fetchall()
            result = []
            [result.append(*res) for res in query]
            return result

    async def get_leagues(self, type):
        with self.connection:
            query = self.cursor.execute("SELECT DISTINCT `league` FROM `teams` WHERE `kind_of_sport` = ?", (type,)).fetchall()
            result = []
            [result.append(*res) for res in query]
            return result

    async def get_teams(self, league):
        with self.connection:
            query = self.cursor.execute("SELECT DISTINCT `team` FROM `teams` WHERE `league` = ?", (league,)).fetchall()
            result = []
            [result.append(*res) for res in query]
            return result
