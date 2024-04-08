import uuid
from fastapi import FastAPI

from models.course import Course, CourseResponse
from models.player import Player, PlayerResponse


app = FastAPI()

#dict[uuid.UUID, Player] = 
players = {}
courses = {}
# dict[uuid.UUID, Course] 

@app.get("/players")
async def get_player() -> list[Player]:
    return players.values()
    
@app.get("/courses")
async def get_course() -> list[Course]:
    return courses.values()

@app.put("/players/{player_id}")
async def update_player(player_id: uuid.UUID, updated_player: Player) -> PlayerResponse:
    players[player_id] = updated_player
    return PlayerResponse(id=player_id)
    
@app.put("/courses/{course_id}")
async def update_course(course_id: uuid, updated_course: Course) -> CourseResponse:
    courses[course_id] = updated_course
    return CourseResponse(id=course_id)

@app.post("/players")
async def create_player(player: Player) -> PlayerResponse:
    player_id = uuid.uuid4()
    players[player_id] = player
    return PlayerResponse(id=player_id)

@app.post("/courses")
async def create_course(course: Course) -> CourseResponse:
    course_id = uuid.uuid4()
    courses[course_id] = course
    return course_id

@app.delete("/players/{player_id}")
async def delete_player(player_id: uuid.UUID) -> None:
    players.pop(player_id)

@app.delete("/courses/{course_id}")
async def delete_course(course_id: uuid.UUID) -> None:
    courses.pop(course_id)
