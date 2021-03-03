import typer
import shlex
import subprocess
from wct_api.database import db
from wct_api.seeds import *


app = typer.Typer()


@app.command()
def start_server():
    cmd = shlex.split("uvicorn main:app --reload")
    typer.echo(subprocess.run(cmd))


@app.command()
def create_db_tables():
    db.generate_mapping(create_tables=True)
    typer.echo("database tables created")


@app.command()
def drop_db_tables():
    db.generate_mapping()
    db.drop_all_tables(with_all_data=True)
    typer.echo(f"dropped database tables")


@app.command()
def seed_tables():
    db.generate_mapping()
    seed_country_table()
    seed_group_table()


if __name__ == "__main__":
    app()
