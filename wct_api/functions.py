from wct_api.database import *
from wct_api.models import *
from pony.orm import db_session, commit
from fastapi import HTTPException


@db_session
def get_all_countries():
    for c in Country.select():
        yield dict(CountryModel.from_orm(c))


@db_session
def get_all_groups():
    for g in Group.select():
        yield dict(GroupModel.from_orm(g))


@db_session
def add_new_team(team: TeamInput):
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

