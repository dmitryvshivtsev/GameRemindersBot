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

    def add_user(self, tg_id: int, tg_username: str):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (tg_id, tg_username) VALUES (%s, %s);", (tg_id, tg_username,))

    async def user_exists(self, tg_id: int):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE tg_id = %s;", (tg_id,))
            result = len(self.cursor.fetchall())
            return bool(result)

    async def set_favourite_team(self, tg_id: int, favourite_team: str):
        with self.connection:
            return self.cursor.execute("UPDATE users SET team_id = (SELECT id FROM teams WHERE team = %s) "
                                       "WHERE tg_id = %s;", (favourite_team, tg_id,))

    async def get_favourite_team(self, tg_id: int):
        with self.connection:
            return self.cursor.execute("SELECT team FROM teams WHERE tg_id = %s;", (tg_id,))

    async def get_user_id(self, tg_username: str):
        with self.connection:
            self.cursor.execute("SELECT tg_id FROM users WHERE tg_username = %s;", (tg_username,))
            result = self.cursor.fetchall()
            for row in result:
                userid = int(row(0))
            return userid

    async def get_all_types(self):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT kind_of_sport FROM teams ORDER BY kind_of_sport;")
            result = []
            query = self.cursor.fetchall()
            [result.append(*res) for res in query]
            return result

    async def get_all_leagues(self, kind: str):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT league FROM teams WHERE kind_of_sport = %s ORDER BY league;", (kind,))
            query = self.cursor.fetchall()
            result = []
            [result.append(*res) for res in query]
            return result

    async def get_all_teams(self, league: str):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT team FROM teams WHERE league = %s ORDER BY team;", (league,))
            result = []
            query = self.cursor.fetchall()
            [result.append(*res) for res in query]
            return result

    def get_all_tags(self, tg_id: int):
        with self.connection:
            self.cursor.execute("SELECT DISTINCT team, team_tag FROM teams WHERE id = (SELECT team_id FROM users WHERE tg_id = %s);", (tg_id,))
            result = []
            query = self.cursor.fetchall()
            [result.append(i) for res in query for i in res]
            return result

    def get_all_tg_id(self):
        with self.connection:
            self.cursor.execute("SELECT tg_id FROM users;")
            result = []
            query = self.cursor.fetchall()
            [result.append(*res) for res in query]
            return result

    def get_arrs(self):
        with self.connection:
            self.cursor.execute("SELECT team_id_arr FROM users;")
            result = []
            query = self.cursor.fetchall()
            [result.append(*res) for res in query]
            return result

    def add_to_arr(self, idx, tg_id):
        with self.connection:
            self.cursor.execute("UPDATE users SET team_id_arr = (SELECT team_id_arr FROM users WHERE tg_id = %s) || %s"
                                " WHERE tg_id = %s", (tg_id, idx, tg_id))

    # def add_commands(self, sport, league, team, tag):
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO teams (kind_of_sport, league, team, team_tag)
    #         VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING;", (sport, league, team, tag))
