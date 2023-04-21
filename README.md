# GameRemindersBot

Bot helps not to miss the game of your favorite team from some sports and informs about the next game. \
In this version, the bot has the following functionality:
* At the request of the user and the name of the team informs about the next game;
* Automatically add the user to the database when you start the bot;
* The ability to select your favorite sport, league and team via menu;
* Automatically remind about the game of your favorite team 2 times a day;
* Getting the score during the match;
* Receiving the score after the end of the match.

Example: \
<img src="/images/edit_team_1.png" alt="example_bot" width="600"/> \
<img src="/images/edit_team_2.png" alt="example_bot2" width="600"/> \
<img src="/images/get_date.png" alt="example_bot3" width="600"/>

Plans to implement:
* Adding several favorite clubs;
* Automatic notification of results after the end of the game;
* Pagination and improved navigation when selecting teams.

Stack:
* PostgreSQL 15
* Aiogram 3.0.0b6
* Requests + bs4
* Docker
