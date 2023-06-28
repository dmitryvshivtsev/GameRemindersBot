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
You can get game results for your favorite teams (including games going on right now!): \
<img src="/images/get_date_1.png" alt="example_bot" width="600"/> \
You will also get results every day at 9 a.m. and 9 p.m: \
<img src="/images/get_date_2.png" alt="example_bot2" width="600"/> \
You can check, delete, or add any team at any time: \
<img src="/images/edit_team.png" alt="example_bot3" width="600"/>
The bot has user-friendly keyboard for this purpose: \
<img src="/images/edit_team_1.png" alt="example_bot4" width="600"/> \

Plans to implement:
* Automatic notification with the result of the game after its completion;
* Pagination and improved navigation when selecting a team.

Stack:
* Python3.10
* PostgreSQL 15
* Aiogram 3.0.0b6
* Requests + bs4
* Docker
