import typer
import shlex
import subprocess
from wctapi.schema import db
from wctapi.seeds import *


app = typer.Typer()


@app.command()
def start_server():
    cmd = shlex.split("uvicorn main:app --host 0.0.0.0 --port 8000 --reload")
    typer.echo(subprocess.run(cmd))


@app.command()
def create_db_tables():
    typer.echo("database tables created")


@app.command()
def drop_db_tables():
    db.generate_mapping()
    db.drop_all_tables()
    typer.echo(f"dropped database tables")


@app.command()
def seed_tables():
    seed_country_table()
    seed_group_table()


@app.command()
def backup_db(db_container: str):
    cmd = shlex.split(
        f'docker exec -t {db_container} pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql'
    )
    typer.echo(subprocess.run(cmd))


@app.command()
def restore_db_backup(sql_dump_file: str, db_container: str):
    cmd = shlex.split(f'cat {sql_dump_file} | docker exec -i {db_container} psql -U postgres')
    typer.echo(subprocess.run(cmd))


if __name__ == "__main__":
    app()

