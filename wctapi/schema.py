from pony.orm import *
from datetime import date
from decimal import Decimal
from .utils import get_db_credentials
from dotenv import load_dotenv


db = Database()


class Group(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    teams = Set('Team')


class Country(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    flag_url = Required(str, unique=True)  # url of country flag image
    teams = Set('Team')


class Team(db.Entity):
    id = PrimaryKey(int, sql_type='bigint', auto=True)
    name = Required(str, 75, unique=True)
    group = Optional(Group)
    logo_url = Optional(str, unique=True)
    country = Required(Country)
    athletes = Set('Athlete')
    matches = Set('Match', reverse='team_A')
    matches_against = Set('Match', reverse='team_B')
    matches_won = Set('Match', reverse='winning_team')
    matches_lost = Set('Match', reverse='loosing_team')
    points = Optional('Points')


class Athlete(db.Entity):
    id = PrimaryKey(int, sql_type='bigint', auto=True)
    team = Required(Team)
    first_name = Required(str, 50)
    last_name = Required(str, 50)
    birth_date = Optional(date)
    image_url = Optional(str, unique=True, default='null')
    sm_handle = Optional(str, 50, unique=True, default='null')
    chaser_in_chases = Set('Chase', reverse='chaser')
    evader_in_chases = Set('Chase', reverse='evader')


class Match(db.Entity):
    id = PrimaryKey(int, sql_type='bigint', auto=True)
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
    id = PrimaryKey(int, sql_type='bigint', auto=True)
    match = Required(Match)
    chase_no = Required(int)
    chaser = Required(Athlete, reverse='chaser_in_chases')
    evader = Required(Athlete, reverse='evader_in_chases')
    tag_made = Required(bool)
    tag_time = Optional(float)
    sudden_death = Required(bool)


class Points(db.Entity):
    id = PrimaryKey(int, auto=True)
    team = Required(Team)
    played = Optional(int, default=0)
    won = Optional(int, default=0)
    tied = Optional(int, default=0)
    sd_points = Optional(int)  # points won via sudden death chases
    points = Optional(int, default=0)
    evasion = Optional(int)


load_dotenv()

credentials = get_db_credentials()
db.bind(**credentials)
db.generate_mapping(create_tables=True)

