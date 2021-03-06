from fastapi import FastAPI
from wctapi.crud_ops import *

app = FastAPI()


def get_connection():
    return db.get_connection()


@app.get("/")
def get_root():
    return {"Word Chase Tag": "Keep Chasing! Don't Get Caught!"}


@app.get("/countries", response_model=CountriesOutput)
def get_countries():
    return {"countries": read_countries()}


@app.get("/groups", response_model=GroupsOutput)
def get_groups():
    return {"groups": read_groups()}


@app.post("/team", response_model=CreateTeamOutput or HTTPException)
def post_team(team: TeamInput):
    return {'new_team': create_team(team)}


@app.get("/teams", response_model=TeamsOutput)
def get_teams():
    return {'teams': read_teams()}


@app.post("/athlete", response_model=CreateAthleteOutput or HTTPException)
def post_athlete(athlete: AthleteInput):
    return {"new_athlete": create_athlete(athlete)}


@app.get("/athletes", response_model=AthletesOutput)
def get_athletes():
    return {"athletes": read_athletes()}

