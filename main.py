import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from wctapi.crud_ops import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/group/{group_id}/teams")
def get_group_teams(group_id: int):
    return {"group_teams": read_group_teams(group_id)}


@app.get("/group/{group_id}/matches")
def get_group_matches(group_id: int):
    return {"group_matches": read_group_matches(group_id)}


@app.post("/team", response_model=CreateTeamOutput or HTTPException)
def post_team(team: CreateTeamInput):
    return {'new_team': create_team(team)}


@app.get("/teams", response_model=TeamsOutput)
def get_teams():
    return {'teams': read_teams()}


@app.get("/team/{team_id}")
def get_team(team_id: int):
    return {"team": read_teams(team_id)}


@app.get("/team/{team_id}/athletes")
def get_team_athletes(team_id: int):
    return {"team_athletes": read_team_athletes(team_id)}


@app.get("/team/{team_id}/matches")
def get_team_matches(team_id: int):
    return {"team_matches": list(read_team_matches(team_id))}


@app.post("/athlete", response_model=CreateAthleteOutput or HTTPException)
def post_athlete(athlete: CreateAthleteInput):
    return {"new_athlete": create_athlete(athlete)}


@app.get("/athletes", response_model=AthletesOutput)
def get_athletes():
    return {"athletes": read_athletes()}


@app.get("/athlete/{athlete_id}")
def get_athlete(athlete_id: int):
    return {"athlete": read_athletes(athlete_id)}


@app.get("/athlete/{athlete_id}/chases")
def get_athlete_chases(athlete_id: int):
    return {"athlete_chases": read_athlete_chases(athlete_id)}


@app.get("/athlete/{athlete_id}/chases/chaser")
def get_athlete_chases_chasing(athlete_id: int):
    return {"athlete_chasing": read_athlete_chases(athlete_id, is_chaser=True)}


@app.get("/athlete/{athlete_id}/chases/evader")
def get_athlete_chases_evading(athlete_id: int):
    return {"athlete_evading": read_athlete_chases(athlete_id, is_evader=True)}


@app.get("/athlete/{athlete_id}/stats", response_model=AthleteStatsOutput or HTTPException)
def get_athlete_stats(athlete_id: int):
    return read_athlete_stats(athlete_id)


@app.post("/match")
def post_match(match: CreateMatchInput):
    return create_match(match)


@app.get("/matches")
def get_matches():
    return {"matches": read_matches()}


@app.get("/match/{match_id}")
def get_match(match_id: int):
    return {"match": read_matches(match_id)}


@app.get("/match/{match_id}/chases")
def get_match_chases(match_id: int):
    return {"match_id": match_id, "chases": read_chases(match_id)}


@app.put("/chases")
def put_chases():
    return {"chases": create_chases()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
