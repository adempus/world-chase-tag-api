"""
Contains CRUD operations invoked from route requests.
"""

import pendulum
from wctapi.schema import *
from wctapi.models import *
from pony.orm import db_session, commit
from fastapi import HTTPException
from pony.orm.serialization import to_dict


@db_session
def read_countries():
    for c in Country.select():
        yield dict(CountryModel.from_orm(c))


@db_session
def read_groups():
    for g in Group.select():
        yield dict(GroupModel.from_orm(g))


@db_session
def create_team(team: CreateTeamInput) -> dict:
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
def create_athlete(athlete: CreateAthleteInput):
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


@db_session
def create_match(match: CreateMatchInput):
    new_match = Match(
        team_A=match.team_A_id,
        team_B=match.team_B_id,
        winning_team=match.winning_team_id,
        loosing_team=match.loosing_team_id,
        team_A_points=match.team_A_points,
        team_B_points=match.team_B_points,
        date=match.date,
        video_url=match.video_url
    )
    commit()
    return {
        'new_match': dict(MatchModel.from_orm(new_match)),
        'chases': create_chases(new_match.id, match.chases)
    }


@db_session
def read_matches(match_id: int = None):
    if match_id is None:
        for m in Match.select():
            yield MatchModel.from_orm(m)
    else:
        if not Match.exists(lambda m: m.id == match_id):
            return None
        match = Match[match_id]
        yield MatchModel.from_orm(match)


@db_session
def create_chases(match_id: int, chases: List[CreateChaseInput]):
    new_chases = [
        Chase(
            match=match_id,
            chase_no=c.chase_no,
            chaser=c.chaser_id,
            evader=c.evader_id,
            tag_made=c.tag_made,
            tag_time=c.tag_time,
            sudden_death=c.sudden_death
        )
        for c in chases
    ]
    commit()
    res = []
    # omit superfluous match data
    for chase in new_chases:
        c = dict(ChaseModel.from_orm(chase))
        c['match_id'] = match_id
        c.pop('match')
        res.append(c)
    return res


@db_session
def read_chases(match_id: int):
    for c in Chase.select(lambda chase: chase.match.id == match_id):
        c_obj = dict(ChaseModel.from_orm(c))
        c_obj.pop('match')
        yield c_obj
