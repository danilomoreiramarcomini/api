from fastapi import FastAPI

app = FastAPI()
members = {
    1: {"Name": "Serj Tankian", "Occupation": "Vocal"},
    2: {"Name": "Daron Malakian", "Occupation": "Guitar"},
    3: {"Name": "Shavo Odadjian", "Occupation": "Bass"},
    4: {"Name": "John Dolmayan", "Occupation": "Drums"}}


@app.get("/")
def home():
    return "We are On-line"


@app.get("/members/")
def get_members():
    return members


@app.get("/member/{id_member}")
def get_member(id_member: int):
    if id_member in members:
        return f"Name: {members[id_member]['Name']}    Occupation: {members[id_member]['Occupation']}"
    else:
        return "ID don't exist"

