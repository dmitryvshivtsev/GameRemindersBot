import os
import psycopg2
from psycopg2 import Error


class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Database.__instance:
            Database.__instance = super(Database, cls).__new__(cls)
        return Database.__instance

    def __init__(self):
        try:
            self.connection = psycopg2.connect(os.getenv('DB_CONNECT'))
            self.cursor = self.connection.cursor()
        except:
            print('Cant establish connection to database')

    def add_user(self, tg_id, tg_username):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (tg_id, tg_username) VALUES (%s, %s);", (tg_id, tg_username,))

    async def user_exists(self, tg_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE tg_id = %s;", (tg_id,))
            result = len(self.cursor.fetchall())
            return bool(result)

    async def set_favourite_team(self, tg_id, favourite_team):
        with self.connection:
            return self.cursor.execute("UPDATE users SET team_id = (SELECT id FROM teams WHERE team = %s) "
                                       "WHERE tg_id = %s;", (favourite_team, tg_id,))

    async def get_favourite_team(self, tg_id):
        with self.connection:
            return self.cursor.execute("SELECT team FROM teams WHERE tg_id = %s;", (tg_id,))

    async def get_user_id(self, tg_username):
        with self.connection:
            self.cursor.execute("SELECT tg_id FROM users WHERE tg_username = %s;", (tg_username,))
            result = self.cursor.fetchall()
            for row in result:
                userid = int(row(0))
            return userid

    async def get_types(self):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT kind_of_sport FROM teams;")
            result = []
            query = self.cursor.fetchall()
            [result.append(*res) for res in query]
            return result

    async def get_leagues(self, kind):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT league FROM teams WHERE kind_of_sport = %s;", (kind,))
            query = self.cursor.fetchall()
            result = []
            [result.append(*res) for res in query]
            return result

    async def get_teams(self, league):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT team FROM teams WHERE league = %s;", (league,))
            result = []
            query = self.cursor.fetchall()
            [result.append(*res) for res in query]
            return result

    def get_tag(self, tg_id):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT team, team_tag FROM teams WHERE id = (SELECT team_id FROM users WHERE tg_id = %s);", (tg_id,))
            result = []
            query = self.cursor.fetchall()
            [result.append(i) for res in query for i in res]
            return result

    def get_tg_id(self):
        with self.connection:
            self.cursor.execute("SELECT tg_id FROM users;")
            result = []
            query = self.cursor.fetchall()
            [result.append(*res) for res in query]
            return result