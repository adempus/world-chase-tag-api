"""
Contains pydantic models for enforcing entity integrity, through validations on request and response data.
"""

from typing import List, Optional
from pydantic import BaseModel
from pendulum import date


#
# class AthleteInput(BaseModel):
#     team_id: int
#     first_name: str
#     last_name: str
#     birth_date: date
#     img_url: Optional[str] = None
#     sm_handle: Optional[str] = None
#
#
# class ChaseInput(BaseModel):
#     match_id: int
#     chase_no: int
#     chaser_id: int
#     evader_id: int
#     tag_made: bool
#     tag_time: float
#     sudden_death: bool
#
#
# class MatchInput(BaseModel):
#     team_A_id: int
#     team_B_id: int
#     winning_team_id: int
#     loosing_team_id: int
#     team_A_points: int
#     team_B_points: int
#     date: date
#     video_url: Optional[str] = None


class GroupModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class GroupInput(BaseModel):
    name: str


class GroupOutput(BaseModel):
    groups: List[GroupModel]


class CountryModel(BaseModel):
    id: int
    name: str
    flag_url: str

    class Config:
        orm_mode = True


class CountryOutput(BaseModel):
    countries: List[CountryModel]


class TeamModel(BaseModel):
    id: int
    name: str
    group: GroupModel
    logo_url: Optional[str]
    country: CountryModel

    class Config:
        orm_mode = True


class TeamInput(BaseModel):
    name: str
    group_id: Optional[int]
    logo_url: Optional[str]
    country_id: int


class CreateTeamOutput(BaseModel):
    new_team: TeamModel


# class AthleteOutput(BaseModel):
#     id: int
#     team: TeamOutput
#     first_name: str
#     last_name: str
#     birth_date: date
#     img_url: Optional[str]
#     sm_handle: Optional[str]
#
#
# class ChaseOutput(BaseModel):
#     id: int
#     match_id: int
#     chase_no: int
#     chaser: AthleteOutput
#     evader: AthleteOutput
#     tag_made: bool
#     tag_time: float
#     sudden_death: bool
#
#
# class MatchOutput(BaseModel):
#     id: int
#     team_A: TeamOutput
#     team_B: TeamOutput
#     winning_team: TeamOutput
#     loosing_team: TeamOutput
#     team_A_points: int
#     team_B_points: int
#     date: date
#     video_url: Optional[str]
#     chases: Optional[List[ChaseOutput]]
#
