from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime, date


class Team:

    def __init__(self, sport, name, tag):
        self.sport = sport
        self.name = name
        self.tag = tag


def parse_clubs(clubs: list, sport: str):
    for n in range(1, 4):
        url = f'https://www.sports.ru/{sport}/club/?page={n}'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        td = [x.text for x in soup.find_all('a', class_='name')]
        links = [x['href'][22:-1] for x in soup.find_all('a', class_='name')]
        [clubs.append((sport, td[i], links[i])) for i in range(len(td))]
    return clubs


def validation(team):
    url = f'https://www.sports.ru/{team}/calendar'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    now = datetime.now()
    dates = parse_date(soup)

    games_dates = []
    for dat in dates:
        # Формат "Дата | Время"
        dat = dat.split('|')
        if len(dat) > 1 or not dat[0].isalpha():
            elems = dat[0].split('.')
            if not elems[0].isalpha():
                cur_day, cur_month, cur_year = map(int, elems)
                parsed_date = date(cur_year, cur_month, cur_day)
                if (parsed_date.month == now.month and parsed_date.day >= now.day) or \
                        (parsed_date.month > now.month and parsed_date.year >= now.year):
                    if len(dat) > 1:
                        games_dates.append(parsed_date.strftime("%d.%m.%Y в ") + dat[1])
                    else:
                        games_dates.append(parsed_date.strftime("%d.%m.%Y"))

    return games_dates[0]


def parse_date(soup):
    dates = []
    for date in soup.find_all('td', class_='name-td alLeft bordR'):
        if not date.text.isalpha(): dates.append(date.text.strip())

    return dates


def parse_opp(soup):
    opps = []
    for opp in soup.find_all('td', class_='name-td alLeft'):
        opps.append(opp.text.strip())

    return opps


def parse_score(soup):
    scores = []
    for score in soup.find_all('td', class_='score-td'):
        scores.append(score.text.strip())

    return scores


def send_date_of_match(team_on_russian: str) -> str:
    football_clubs = []
    parse_clubs(football_clubs, 'football')
    new_football_clubs = []
    [new_football_clubs.append(Team(case[0], case[1], case[2])) for case in football_clubs]

    input_club = team_on_russian.strip().lower()

    for i in new_football_clubs:
        if i.name.lower() == input_club:
            return f"Ближайшая игра клуба {i.name} состоится {validation(i.tag)} (МСК)"
