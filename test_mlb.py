from __future__ import print_function
import mlbgame
import datetime

today = datetime.date.today()
year = today.year
month = today.month
day = today.day
games = mlbgame.day(year, month, day)
msg = ""
for game in games:
    game_txt = "{}".format(game)
    msg += game_txt
