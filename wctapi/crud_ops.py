"""
Contains CRUD operations invoked from route requests.
"""

import pendulum
from itertools import chain
from statistics import fmean
from fastapi import HTTPException
from wctapi.schema import *
from wctapi.models import *


@db_session
def read_countries():
    return read_one_or_many(Country, CountryModel)


@db_session
def read_groups():
    return read_one_or_many(Group, GroupModel)


@db_session
def read_group_teams(group_id: int):
    return read_one_or_many(Group[group_id].teams, TeamModel)


@db_session
def read_group_matches(group_id: int):
    matches = []
    for team in Group[group_id].teams:
        for match in team.matches:
            if match.team_A.group == match.team_B.group:
                matches.append(chain.from_iterable(read_matches(match.id)))
    return matches


@db_session
def create_team(team: CreateTeamInput):
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
def read_teams(team_id: int = None):
    return read_one_or_many(Team, TeamModel, team_id)


@db_session
def read_team_athletes(team_id: int):
    return read_one_or_many(Team[team_id].athletes, AthleteModel)


@db_session
def read_team_matches(team_id: int):
    matches = read_one_or_many(Team[team_id].matches, MatchModel)
    matches_against = read_one_or_many(Team[team_id].matches_against, MatchModel)
    return chain(matches, matches_against)


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
def read_athletes(athlete_id: int = None):
    return read_one_or_many(Athlete, AthleteModel, athlete_id)


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


def read_matches(match_id: int = None):
    return read_one_or_many(Match, MatchModel, match_id)


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
    for chase in new_chases:
        c = dict(ChaseModel.from_orm(chase))
        c['match_id'] = match_id
        c.pop('match')
        res.append(c)
    return res


@db_session
def read_chases(match_id: int):
    for c in Chase.select(lambda chase: chase.match.id == match_id):
        yield exclude_superfluous(c)


@db_session
def read_athlete_chases(athlete_id: int,  as_chaser=False, as_evader=False):
    if as_evader == as_chaser:
        for c in Chase.select(lambda chase: chase.evader.id == athlete_id or chase.chaser.id == athlete_id):
            yield exclude_superfluous(c)
    elif as_evader:
        for c in Chase.select(lambda chase: chase.evader.id == athlete_id):
            yield exclude_superfluous(c)
    else:
        for c in Chase.select(lambda chase: chase.chaser.id == athlete_id):
            yield exclude_superfluous(c)


def read_athlete_stats(athlete_id: int):
    athlete = list(read_athletes(athlete_id=athlete_id))
    if len(athlete) == 0:
        raise HTTPException(status_code=404, detail=f"No athlete with specified ID found.")

    c_stats = calc_athlete_stats(read_athlete_chases(athlete_id, as_chaser=True), as_chaser=True)
    e_stats = calc_athlete_stats(read_athlete_chases(athlete_id, as_evader=True))
    athlete_stats = {
        'id': athlete_id,
        'name': f"{athlete[0].first_name} {athlete[0].last_name}",
        'chaser': ChaserStats(
            tag_attempts=c_stats['attempted'], tags_made=c_stats['made'], average_time=c_stats['time'],
            tag_percentage=c_stats['percentage'], z_score=c_stats['z_score']),
        'evader': EvaderStats(
            evasion_attempts=e_stats['attempted'], evasions_made=e_stats['made'], average_time=e_stats['time'],
            evade_percentage=e_stats['percentage'], z_score=e_stats['z_score'])
    }
    return AthleteStatsOutput(**athlete_stats)


def calc_athlete_stats(athlete_chases, as_chaser=False):
    chases = list(athlete_chases)
    stats = {'attempted': 0, 'made': 0, 'time': 0, 'percentage': 0, 'z_score': 0}
    if len(chases) > 0:
        wct_avg = 13.2
        stats['attempted'] = len(chases)
        stats['made'] = len([c for c in chases if c['tag_made'] is as_chaser])
        stats['time'] = round(fmean([20.0 if c['tag_time'] == 0.0 else c['tag_time'] for c in chases]), 1)
        stats['percentage'] = round((stats['made'] / stats['attempted']) * 100)
        stats['z_score'] = round(
            ((wct_avg - stats['time']) / wct_avg) * 100 if as_chaser else ((stats['time'] - wct_avg) / wct_avg) * 100
        )
    return stats


def exclude_superfluous(chase):
    """Replaces verbose nested object with object ids. """
    c_obj = dict(ChaseModel.from_orm(chase))
    c_obj['match_id'] = c_obj['match'].id
    c_obj.pop('match')
    return c_obj


@db_session
def read_one_or_many(entity, entity_model, entity_id: int = None):
    if entity_id is None:
        for obj in entity.select():
            yield entity_model.from_orm(obj)
    else:
        if not entity.exists(lambda obj: obj.id == entity_id):
            return None
        res = entity[entity_id]
        yield entity_model.from_orm(res)
