from pony.orm import *
from datetime import date
from decimal import Decimal
from .utils import get_db_credentials
from dotenv import load_dotenv


db = Database()


class Group(db.Entity):
    id = PrimaryKey(int, size=32, auto=True)
    name = Required(str, unique=True)
    teams = Set('Team')


class Country(db.Entity):
    id = PrimaryKey(int, size=8, auto=True)
    name = Required(str, unique=True)
    flag_url = Required(str, unique=True)  # url of country flag image
    teams = Set('Team')


class Team(db.Entity):
    id = PrimaryKey(int, size=8, sql_type='bigint', auto=True)
    name = Required(str, 75, unique=True)
    group = Optional(Group)
    logo_url = Optional(str, unique=True)
    country = Required(Country)
    athletes = Set('Athlete')
    matches = Set('Match', reverse='team_A')
    matches_against = Set('Match', reverse='team_B')
    matches_won = Set('Match', reverse='winning_team')
    matches_lost = Set('Match', reverse='loosing_team')


class Athlete(db.Entity):
    id = PrimaryKey(int, size=8, sql_type='bigint', auto=True)
    team = Required(Team)
    first_name = Required(str, 50)
    last_name = Required(str, 50)
    birth_date = Required(date)
    image_url = Optional(str, unique=True, default='null')
    sm_handle = Optional(str, 50, unique=True, default='null')
    chases = Set('Chase', reverse='chaser')
    evader_in_chases = Set('Chase', reverse='evader')


class Match(db.Entity):
    id = PrimaryKey(int, size=8, sql_type='bigint', auto=True)
    team_A = Required(Team, reverse='matches')
    team_B = Required(Team, reverse='matches_against')
    winning_team = Required(Team, reverse='matches_won')
    loosing_team = Required(Team, reverse='matches_lost')
    team_A_points = Required(int)
    team_B_points = Required(int)
    date = Required(date)
    video_url = Optional(str, sql_default='null')
    chases = Set('Chase')


class Chase(db.Entity):
    id = PrimaryKey(int, size=8, sql_type='bigint', auto=True)
    match = Required(Match)
    chase_no = Optional(int)
    chaser = Required(Athlete, reverse='chases')
    evader = Required(Athlete, reverse='evader_in_chases')
    tag_made = Required(bool)
    tag_time = Optional(Decimal, precision=2)
    sudden_death = Required(bool)


load_dotenv()
credentials = get_db_credentials()
db.bind(**credentials)

