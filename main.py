import uuid
from fastapi import FastAPI

from models.course import Course
from models.player import Player


app = FastAPI()

players = dict[uuid.UUID, Player] = {}
courses = dict[uuid.UUID, Course] = {}

@app.get("/players")
async def get_player():
    pass

@app.get("/courses")
async def get_course():
    pass

@app.put("/players/{player_id}")
async def update_player(player_id: uuid):
    pass

@app.put("/courses/{course_id}")
async def update_course(course_id: uuid):
    pass

@app.post("/players")
async def create_player():
    pass

@app.post("/courses")
async def create_course():
    pass

@app.delete("/players/{player_id}")
async def delete_player(player_id: uuid):
    pass

@app.delete("/courses/{course_id}")
async def delete_course(coursse_id: uuid):
    pass
