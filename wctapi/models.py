"""
Contains pydantic models for enforcing entity integrity, through validations on request and response data.
"""

from __future__ import annotations
from typing import List, Optional, ForwardRef
from pony.orm.core import SetInstance
from pydantic import BaseModel
from datetime import date
from pydantic.class_validators import Any
from pydantic.utils import GetterDict


class PonyGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, SetInstance):
            return list(res)
        return res


class GroupModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class GroupInput(BaseModel):
    name: str


class GroupsOutput(BaseModel):
    groups: List[GroupModel]


class CountryModel(BaseModel):
    id: int
    name: str
    flag_url: str

    class Config:
        orm_mode = True


class CountriesOutput(BaseModel):
    countries: List[CountryModel]


AthleteRef = ForwardRef('AthleteModel')


class TeamModel(BaseModel):
    id: int
    name: str
    group: GroupModel
    logo_url: Optional[str]
    country: CountryModel

    class Config:
        orm_mode = True
        getter_dict = PonyGetterDict


class CreateTeamInput(BaseModel):
    name: str
    group_id: Optional[int]
    logo_url: Optional[str]
    country_id: int


class CreateTeamOutput(BaseModel):
    new_team: TeamModel


class TeamsOutput(BaseModel):
    teams: List[TeamModel]


class AthleteModel(BaseModel):
    id: int
    team: TeamModel
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
    image_url: Optional[str] = None
    sm_handle: Optional[str] = None

    class Config:
        orm_mode = True


TeamModel.update_forward_refs()


class CreateAthleteInput(BaseModel):
    team_id: int
    first_name: str
    last_name: str
    birth_date: Optional[str] = None
    image_url: Optional[str] = None
    sm_handle: Optional[str] = None


class CreateAthleteOutput(BaseModel):
    new_athlete: AthleteModel


class AthletesOutput(BaseModel):
    athletes: List[AthleteModel]


class AthleteOutput(BaseModel):
    team_id: int
    first_name: str
    last_name: str
    birth_date: Optional[str] = None
    image_url: Optional[str] = None
    sm_handle: Optional[str] = None


ChaseModelRef = ForwardRef('ChaseModel')


class MatchModel(BaseModel):
    id: int
    team_A: TeamModel
    team_B: TeamModel
    winning_team: TeamModel
    loosing_team: TeamModel
    team_A_points: int
    team_B_points: int
    date: date
    video_url: Optional[str] = None
    # chases: List[ChaseModel] = []

    class Config:
        orm_mode = True
        getter_dict = PonyGetterDict


class ChaseModel(BaseModel):
    id: int
    match: MatchModel
    chase_no: int
    chaser: AthleteModel
    evader: AthleteModel
    tag_made: bool
    tag_time: float
    sudden_death: bool

    class Config:
        orm_mode = True
        getter_dict = PonyGetterDict


MatchModel.update_forward_refs()


CreateChaseInputRef = ForwardRef('CreateChaseInput')


class CreateMatchInput(BaseModel):
    team_A_id: int
    team_B_id: int
    winning_team_id: int
    loosing_team_id: int
    team_A_points: int
    team_B_points: int
    date: date
    video_url: Optional[str] = None
    chases: List[CreateChaseInputRef]


class CreateChaseInput(BaseModel):
    match_id: Optional[int] = None
    chase_no: int
    chaser_id: int
    evader_id: int
    tag_made: bool = False
    tag_time: float
    sudden_death: bool = False


CreateMatchInput.update_forward_refs()


class CreateMatchOutput(BaseModel):
    id: int
    team_A: TeamModel
    team_B: TeamModel
    winning_team: TeamModel
    loosing_team: TeamModel
    team_A_points: int
    team_B_points: int
    date: date
    video_url: Optional[str]
    chases: List[ChaseModel]


class CreateChaseOutput(BaseModel):
    id: int
    match: Optional[MatchModel]
    chase_no: int
    chaser: AthleteModel
    evader: AthleteModel
    tag_made: bool
    tag_time: float
    sudden_death: bool

