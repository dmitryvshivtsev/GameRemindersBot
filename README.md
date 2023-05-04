# GameRemindersBot

Bot helps not to miss the game of your favorite team from some sports and informs about the next game. \
In this version, the bot has the following functionality:
* Automatically add a user to the database when you start the bot;
* The ability to select favorite sports clubs through the menu;
* Automatic reminder of favorite teams' games 2 times a day;
* Getting the current score during the match;
* Getting the final score after the end of the match;
* Adding several favorite teams (and removing them);

Example: \
<img src="/images/edit_team_1.png" alt="example_bot" width="600"/> \
<img src="/images/edit_team_2.png" alt="example_bot2" width="600"/> \
<img src="/images/get_date.png" alt="example_bot3" width="600"/>

Plans to implement:
* Automatic notification with the result of the game after its completion;
* Pagination and improved navigation when selecting a team.

Stack:
* Python3.10
* PostgreSQL 15
* Aiogram 3.0.0b6
* Requests + bs4
* Docker
