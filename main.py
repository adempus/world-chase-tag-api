import uvicorn
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
def post_team(team: CreateTeamInput):
    return {'new_team': create_team(team)}


@app.get("/teams", response_model=TeamsOutput)
def get_teams():
    return {'teams': read_teams()}


@app.post("/athlete", response_model=CreateAthleteOutput or HTTPException)
def post_athlete(athlete: CreateAthleteInput):
    return {"new_athlete": create_athlete(athlete)}


@app.get("/athletes", response_model=AthletesOutput)
def get_athletes():
    return {"athletes": read_athletes()}


@app.post("/match")
def post_match(match: CreateMatchInput):
    return create_match(match)


@app.get("/matches")
def get_matches():
    return {"matches": read_matches()}


@app.get("/match/{match_id}")
def get_match(match_id: int):
    print(f"match id: {match_id}")
    return {"match": read_matches(match_id)}


@app.put("/chases")
def put_chases():
    return {"chases": create_chases()}


@app.get("/chases/{match_id}")
def get_chases(match_id: int):
    return {"match_id": match_id, "chases": read_chases(match_id)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

