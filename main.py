from fastapi import FastAPI
from wct_api.functions import *

app = FastAPI()


def get_connection():
    return db.get_connection()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/countries", response_model=CountryOutput)
def read_countries():
    return {"countries": get_all_countries()}


@app.get("/groups", response_model=GroupOutput)
def read_groups():
    return {"groups": get_all_groups()}


@app.post("/team", response_model=CreateTeamOutput or HTTPException)
def create_team(team: TeamInput):
    return {'new_team': add_new_team(team)}

