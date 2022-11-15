import json

import pytest


@pytest.fixture
def date():
    with open("date.json", "r") as my_file:
        date_json = my_file.read()
        date = json.loads(date_json)
        return date

@pytest.fixture
def adrress(date):
    adr = date["address"]
    adrress = adr["house_number"] + "+" + adr["road"].replace(" ", "+") + "+" + adr["city"] + "+" + adr[
        "county"] + "+" + adr["state"]
    return adrress

@pytest.fixture
def lat(date):
    lat = date["lat"]
    return lat

@pytest.fixture
def lon(date):
    lon = date["lon"]
    return lon


@pytest.fixture
def place_id(date):
    place_id = date["place_id"]
    return place_id