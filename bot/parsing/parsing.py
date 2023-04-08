from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime, date

from database.db_connection import Database


def validation(club, team_tag):
    url = f'https://www.sports.ru/{team_tag}/calendar'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    now = datetime.now()
    dates = parse_date(soup)

    scores = parse_score(soup)
    scores = check_place(soup, scores)
    opps = parse_opp(soup)
    is_finish = finish_game(soup)

    games_dates = []
    for i, date_time in enumerate(dates):
        # Формат на сайте лежит в виде "Дата | Время" или "Дата"
        date_time = date_time.split('|')
        if len(date_time) > 1 or not date_time[0].isalpha():
            elems = date_time[0].split('.')
            if not elems[0].isalpha():
                cur_day, cur_month, cur_year = map(int, elems)
                parsed_date = date(cur_year, cur_month, cur_day)
                if (parsed_date.month == now.month and parsed_date.day >= now.day) or \
                        (parsed_date.month > now.month and parsed_date.year >= now.year):
                    # now_time = datetime.now().strftime("%H:%M")
                    if date_time[1][:2:] <= datetime.now().time().hour:
                        if not is_finish:
                            return f"Матч идет!\nСчет - {club} [{scores[i + 1]}] {opps[i]}"
                        if is_finish:
                            return f"Крайний матч завершен!\nСчет - {club} [{scores[i + 1]}] {opps[i]}\n\n" \
                                   f"Ближайшая игра клуба {club} против {opps[i]} состоится " \
                                   f"{parsed_date.strftime('%d.%m.%Y')} в {date_time[1]} (По МСК)"
                    elif len(date_time) > 1:
                        return f"Ближайшая игра клуба {club} против {opps[i]} состоится {parsed_date.strftime('%d.%m.%Y')} в {date_time[1]} (По МСК)"
                    else:
                        return f"Ближайшая игра клуба {club} против {opps[i]} состоится {parsed_date.strftime('%d.%m.%Y')}"
    return games_dates[0]


def parse_date(soup):
    dates = []
    for date_ in soup.find_all('td', class_='name-td alLeft bordR'):
        if not date_.text.isalpha():
            dates.append(date_.text.strip())

    return dates


def parse_opp(soup):
    opps = []
    for opp in soup.find_all('div', class_='hide-field'):
        opps.append(opp.text.strip())
    new_opps = []
    for i in range(len(opps)):
        if i % 2 == 1:
            new_opps.append(opps[i])
    return new_opps


def parse_score(soup):
    scores = []
    for score in soup.find_all('td', class_='score-td'):
        scores.append(score.text.strip())
    return scores


def finish_game(soup):
    is_finish = False
    for st in soup.find('div', class_='score-descr'):
        if st.text.strip() == 'завершен':
            is_finish = True
    return is_finish


def check_place(soup, scores):
    where_game = []
    for place in soup.find_all('td', class_='alRight padR20'):
        if place.text.strip():
            where_game.append(place.text.strip())
    for i, place in enumerate(where_game):
        if place == 'В гостях':
            scores[i + 1] = scores[i + 1][::-1]
    return scores


def send_date_of_match(club, team_tag) -> str:
    return validation(club, team_tag)
