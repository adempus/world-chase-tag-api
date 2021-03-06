"""
Contains CRUD operations invoked from route requests.
"""

import pendulum
from wctapi.database import *
from wctapi.models import *
from pony.orm import db_session, commit
from fastapi import HTTPException


@db_session
def read_countries():
    for c in Country.select():
        yield dict(CountryModel.from_orm(c))


@db_session
def read_groups():
    for g in Group.select():
        yield dict(GroupModel.from_orm(g))


@db_session
def create_team(team: TeamInput):
    if Team.exists(lambda t: t.name.lower() == team.name.lower()):
        raise HTTPException(status_code=409, detail=f"Team name taken.")

    new_team = Team(
        name=team.name,
        group=Group[team.group_id],
        logo_url=team.logo_url,
        country=Country[team.country_id]
    )
    commit()
    return dict(TeamModel.from_orm(new_team))


@db_session
def read_teams():
    for t in Team.select():
        yield dict(TeamModel.from_orm(t))


@db_session
def create_athlete(athlete: AthleteInput):
    if Athlete.exists(lambda a: a.sm_handle.lower() == athlete.sm_handle.lower()):
        raise HTTPException(status_code=409, detail=f"Social media handle already in use.")

    new_athlete = Athlete(
        team=Team[athlete.team_id],
        first_name=athlete.first_name,
        last_name=athlete.last_name,
        birth_date=pendulum.parse(athlete.birth_date, exact=True),
        image_url=athlete.img_url,
        sm_handle=athlete.sm_handle
    )
    commit()
    return dict(AthleteModel.from_orm(new_athlete))


@db_session
def read_athletes():
    for a in Athlete.select():
        yield dict(AthleteModel.from_orm(a))
