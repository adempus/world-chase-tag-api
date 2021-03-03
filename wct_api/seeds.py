import httpx
from wct_api.database import db, Country, Group
from pony.orm import db_session, commit


@db_session
def seed_country_table():
    print("seeding country table")
    url = "https://flagcdn.com/en/codes.json"
    res = httpx.get(url).json()
    countries = [(v, f"https://flagcdn.com/{k}.svg") for k, v in res.items() if 'us-' not in k]
    country_ids = []
    for country in countries:
        c = Country(name=country[0], flag_url=country[1])
        country_ids.append(c)
    commit()
    print(f"countries: {country_ids}")


@db_session
def seed_group_table():
    print("seeding group table")
    groups = ('A', 'B', 'C', 'D')
    group_ids = []
    for group in groups:
        g = Group(name=group)
        group_ids.append(g)
    commit()
    print(f"groups: {group_ids}")

